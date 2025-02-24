Sensor Comparison Test

1. Overview

This repository contains the methodology and evaluation criteria for comparing two IMU sensors used in autonomous robots. The comparison focuses on noise characteristics, stability, and confidence intervals of Auto Spectral Density (ASD) estimates.

2. Auto Spectral Density (ASD) Analysis

ASD represents the amplitude distribution of a signal in the frequency domain and is used to analyze the noise characteristics of sensor data.

Fourier Transform is applied to finite-time data to estimate ASD.

Chi-squared distribution is used to determine the confidence interval, evaluating the reliability of ASD estimates.

3. Sensor Comparison Test Methodology

Collect data from two IMU sensors simultaneously during autonomous navigation.

Analyze noise characteristics across frequency bands using ASD.

Use rqt_plot for visual representation of data variations.

4. Performance Evaluation Criteria

Metric

High-Performance Sensor

Low-Performance Sensor

Standard Deviation

Lower (More stable measurements)

Higher (More noise)

IQR Outliers Count

Fewer (Less sudden changes)

More (Highly sensitive to environment)

Outlier Percentage (%)

Close to 0% (Stable readings)

High (Frequent sudden variations)

ASD Graph Characteristics

Lower values in high frequencies (Less vibration/noise)

Higher values in high frequencies (More noise)

Confidence Interval

Narrow (Consistent data distribution)

Wide (High variability in measurements)

5. Conclusion

ASD and confidence interval analysis provide an objective comparison of sensor performance.

High-frequency noise and confidence intervals are key indicators for selecting a reliable sensor.

Final evaluation is supported by graphical and quantitative metrics
