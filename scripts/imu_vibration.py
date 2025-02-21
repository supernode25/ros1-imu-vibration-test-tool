#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import deque
import tf

# 변수 설정
sampling_rate = 500  # 샘플링 주파수 (Hz)
duration = 30  # 측정 시간 (초)
buffer_size = 10000  # 수집할 데이터 포인트 수 (버퍼 크기)
# 데이터를 저장할 버퍼
data_buffer = deque(maxlen=buffer_size)

# IMU 데이터를 받는 콜백 함수
def imu_callback(msg):
    # IMU 데이터에서 가속도 또는 각속도 또는 오일러각을 추출
    #1. 가속도 테스트: (주석을 해제하고 아래 라인을 사용)
    acceleration = msg.linear_acceleration.x  # x축 가속도 (원하는 축으로 변경 가능)
    data_buffer.append(acceleration)  # 데이터를 버퍼에 저장

    # 2. 각속도 테스트: (주석을 해제하고 아래 라인을 사용)
    # angular_velocity = msg.angular_velocity.z  # z축 각속도 (원하는 축으로 변경 가능)
    # data_buffer.append(angular_velocity)  # 데이터를 버퍼에 저장

    # 3. 오일러각 테스트: (쿼터니언을 오일러각으로 변환)
    # quaternion = msg.orientation  # quaternion 값 받기
    # euler_angle = tf.transformations.euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])  # 쿼터니언 -> 오일러각 변환
    # data_buffer.append(euler_angle[2])  # 오일러각에서 z축 값만 받아서 버퍼에 저장 (roll, pitch, yaw 중 yaw 값)

# 1. ROS 노드 초기화
rospy.init_node('imu_asd_test', anonymous=True)

# 2. IMU 토픽 구독
rospy.Subscriber("/imu", Imu, imu_callback)

# 3. 데이터 수집 (실제 테스트에서는 일정 시간 동안 데이터를 받아야 함)
rospy.loginfo("IMU 데이터를 수집 중입니다...")

# 수집된 데이터를 일정 시간 동안 기다린 후 ASD 계산
rospy.sleep(duration)

# 4. 수집된 데이터 배열로 변환
sensor_signal = np.array(data_buffer)

# 5. Fast Fourier Transform (FFT) 적용
n = len(sensor_signal)
frequencies = np.fft.fftfreq(n, 1 / sampling_rate)  # 주파수 벡터 생성
fft_signal = np.fft.fft(sensor_signal)  # FFT 변환

# 6. Power Spectral Density (PSD) 계산
psd = np.abs(fft_signal)**2 / n  # 주파수에 대한 파워 스펙트럼 밀도

# 7. Auto Spectral Density (ASD) 계산
asd = psd / (sampling_rate)  # 단위 변환 (ASD는 PSD를 샘플링 주파수로 나눈 값)

# 8. 신뢰 구간 계산 (Chi-squared 분포 사용)
confidence_level = 0.9  # 90% 신뢰 구간
chi_squared_value = stats.chi2.ppf(confidence_level, 2)  # Chi-squared 임계값 (자유도 2로 설정)

# 신뢰 구간 계산
lower_bound = asd * (1 - chi_squared_value / 2)
upper_bound = asd * (1 + chi_squared_value / 2)

# 성능 평가 지표 계산

# 1. 표준편차 (Standard Deviation) 계산
std_dev = np.std(sensor_signal)
rospy.loginfo(f"Standard Deviation: {std_dev}")
# 표준편차 (Standard Deviation): np.std(sensor_signal)을 사용하여 신호의 표준편차를 계산합니다. 
# 이는 신호의 변동성을 나타내며, 높은 값은 많은 노이즈를 시사합니다.

# 2. 상자 수염 그래프 (IQR) 기반 이상치 탐지
Q1 = np.percentile(sensor_signal, 25)  # 1사분위수
Q3 = np.percentile(sensor_signal, 75)  # 3사분위수
IQR = Q3 - Q1
lower_bound_iqr = Q1 - 1.5 * IQR  # 하위 이상치 경계
upper_bound_iqr = Q3 + 1.5 * IQR  # 상위 이상치 경계
outliers_iqr = sensor_signal[(sensor_signal < lower_bound_iqr) | (sensor_signal > upper_bound_iqr)]
rospy.loginfo(f"IQR Outliers: {len(outliers_iqr)}")
#상자 수염 그래프 (IQR, Interquartile Range): 신호 값의 1사분위수(Q1)와 3사분위수(Q3)를 사용하여 이상치 범위를 설정하고,
# 이 범위를 벗어나는 값들을 이상치로 식별합니다.

# 3. 이상치 비율 (Outlier Percentage) 계산
outlier_percentage = len(outliers_iqr) / len(sensor_signal) * 100
rospy.loginfo(f"Outlier Percentage: {outlier_percentage:.2f}%")

#이상치 비율 (Outlier Percentage): IQR 방법을 사용하여 이상치가 전체 데이터에서 차지하는 비율을 계산합니다. 
#이 값이 높을수록 신호에 노이즈가 많다는 것을 의미합니다.

# 9. 결과 출력
plt.figure(figsize=(10, 6))
plt.loglog(frequencies[:n//2], asd[:n//2], label='ASD')
plt.fill_between(frequencies[:n//2], lower_bound[:n//2], upper_bound[:n//2], alpha=0.3, label='Confidence Interval')
plt.title('Auto Spectral Density (ASD) and Confidence Interval')
plt.xlabel('Frequency (Hz)')

# 10. 가속도, 각속도, 오일러각에 맞게 y축 레이블을 설정
# 가속도 테스트일 경우:
plt.ylabel('ASD (m^2/s^4/Hz)')  # 가속도에 대한 ASD 단위로 변경

# 각속도 테스트일 경우:
#plt.ylabel('ASD (rad^2/s^4/Hz)')  # 각속도에 대한 ASD 단위로 변경

# 오일러각 테스트일 경우:
# plt.ylabel('ASD (rad^2/s^4/Hz)')  # 오일러각에 대한 ASD 단위로 변경

plt.legend()
plt.grid(True)
plt.show()

# 11. 종료 메시지
rospy.loginfo("ASD 계산 완료.")
