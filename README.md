# Sensor Comparison Test

## 1. Overview
This repository contains the methodology and evaluation criteria for comparing two IMU sensors used in autonomous robots. The comparison focuses on noise characteristics, stability, and confidence intervals of Auto Spectral Density (ASD) estimates.

## 2. Auto Spectral Density (ASD) Analysis
ASD represents the amplitude distribution of a signal in the frequency domain and is used to analyze the noise characteristics of sensor data.

- **Fourier Transform** is applied to finite-time data to estimate ASD.
- **Chi-squared distribution** is used to determine the confidence interval, evaluating the reliability of ASD estimates.

## 3. Sensor Comparison Test Methodology
- Collect data from two IMU sensors **simultaneously** during autonomous navigation.
- Analyze **noise characteristics across frequency bands** using ASD.
- Use **rqt_plot** for visual representation of data variations.

## 4. Performance Evaluation Criteria

| **Metric** | **High-Performance Sensor** | **Low-Performance Sensor** |
| --- | --- | --- |
| **Standard Deviation** | Lower (More stable measurements) | Higher (More noise) |
| **IQR Outliers Count** | Fewer (Less sudden changes) | More (Highly sensitive to environment) |
| **Outlier Percentage (%)** | Close to 0% (Stable readings) | High (Frequent sudden variations) |
| **ASD Graph Characteristics** | Lower values in high frequencies (Less vibration/noise) | Higher values in high frequencies (More noise) |
| **Confidence Interval** | Narrow (Consistent data distribution) | Wide (High variability in measurements) |

## 5. ROS1 Setup and Dependencies

### Required Packages
To run the ASD test script in ROS1, ensure the following dependencies are installed:

#### 1. **ROS1 Core Packages**
```bash
sudo apt update
sudo apt install ros-noetic-ros-base ros-noetic-sensor-msgs
```
(For GUI tools like RViz, install `ros-noetic-desktop-full` instead of `ros-base`)

#### 2. **Python Libraries**
```bash
pip3 install numpy matplotlib scipy tf-transformations
```
- `numpy`: Numerical computations and array operations
- `matplotlib`: Data visualization
- `scipy`: Statistical analysis and FFT computation
- `tf-transformations`: Quaternion to Euler angle conversion (ROS `tf` support for Python)

#### 3. **ROS `tf` Package**
Check if `tf` is installed:
```bash
roscd tf
```
If not installed, run:
```bash
sudo apt install ros-noetic-tf
```

#### 4. **Python3 ROS Environment Setup**
```bash
sudo apt install python3-catkin-tools python3-rosdep
rosdep update
```

## 6. Conclusion


## 요약정리

# IMU 센서 성능 비교 테스트

## 1. Auto Spectral Density (ASD) 개념
Auto Spectral Density (ASD)는 신호의 주파수별 진폭 분포를 나타내며, 센서 데이터의 노이즈 특성을 분석하는 데 사용됩니다.  
유한 시간 데이터를 기반으로 푸리에 변환을 적용하여 ASD를 추정하며, **Chi-squared 분포**를 이용해 신뢰 구간을 설정하여 측정값의 신뢰도를 평가합니다.

## 2. 센서 비교 테스트 방법
자율 주행 중 두 개의 IMU 센서 데이터를 동시에 수집하여 비교합니다.  
센서 성능을 평가하기 위해 다음과 같은 방법을 사용합니다:
- 주파수 분석을 통해 노이즈 특성 평가 (특히 **고주파 대역**에서의 차이 확인).
- `rqt_plot`을 활용하여 데이터 변동을 **시각적으로 분석**.

## 3. 성능 평가 기준
센서의 성능을 정량적으로 평가하기 위해 다음 기준을 사용합니다:

| **항목**                         | **성능이 좋은 센서**          | **성능이 나쁜 센서**          |
|----------------------------------|----------------------------|----------------------------|
| **표준편차 (Standard Deviation)** | 작음 (데이터 일정)          | 큼 (노이즈 많음)           |
| **IQR Outliers 개수**            | 적음 (급격한 변화 적음)    | 많음 (환경 변화에 민감)   |
| **Outlier 비율**                 | 0%에 가까움                | 높음 (측정값 급변)        |
| **ASD 그래프 특성**              | 고주파에서 값 낮음 (노이즈 영향 적음) | 고주파에서 값 높음 (노이즈 많음) |
| **신뢰구간 (Confidence Interval)** | 좁음 (데이터 일정)          | 넓음 (측정값 변동 심함)   |

## 4. 결론
- **ASD와 신뢰구간 분석을 통해 센서의 성능 차이를 객관적으로 평가**합니다.
- **고주파 노이즈 및 신뢰구간을 기준으로 신뢰도 높은 센서를 선정**합니다.
- 최종 결과는 **시각적 그래프와 정량적 지표를 활용하여 비교**합니다.

- **ASD and confidence interval analysis provide an objective comparison of sensor performance.**
- **High-frequency noise and confidence intervals are key indicators for selecting a reliable sensor.**
- **Final evaluation is supported by graphical and quantitative metrics.**

