# Sensor Calibration Lab

## Overview

This project was developed as part of **PolyMath Lesson #125 — Sensors and Physical Transducers**.

The goal is to understand how physical quantities are converted into electrical signals, how measurement errors affect sensor readings, and how calibration can improve measurement accuracy.

The lab uses Python and NumPy to simulate a temperature sensor with systematic errors and random Gaussian noise.

## Learning Objectives

- Understand the operating principles of physical sensors and transducers.
- Distinguish sensitivity, resolution, accuracy, and measurement range.
- Identify offset errors, gain errors, and random noise.
- Perform two-point linear sensor calibration.
- Analyze measurement statistics.
- Visualize calibrated sensor readings.
- Investigate how averaging reduces random measurement uncertainty.

## Sensor Types

| Sensor | Physical Quantity | Electrical Output | Unit |
|---|---|---|---|
| NTC Thermistor | Temperature | Resistance change | °C or K |
| LDR | Illuminance | Resistance change | lux |
| Accelerometer | Acceleration | Analog voltage or digital data | m/s² or g |

NTC thermistors decrease their resistance as temperature increases. LDRs typically decrease their resistance as illumination increases.

## Mathematical Model

The simulated sensor follows a linear measurement model:

$$
M = aT + b + \varepsilon
$$

Where:

- `M` is the measured temperature.
- `T` is the true temperature.
- `a` is the gain coefficient.
- `b` is the offset.
- `ε` is additive random noise.

The calibration formula is:

$$
T_{\text{corrected}} = \frac{M-b}{a}
$$

The coefficients are estimated using NumPy's `polyfit()` function.

## Calibration Experiment

Two calibration points were used:

| True Temperature | Measured Temperature |
|---|---|
| 10 °C | 13 °C |
| 30 °C | 37 °C |

The estimated calibration coefficients were:

- Gain: `a = 1.2`
- Offset: `b = 1.0`

The resulting measurement model is:

$$
M = 1.2T + 1
$$

After calibration:

| Raw Measurement | Corrected Temperature |
|---|---|
| 13 °C | 10 °C |
| 25 °C | 20 °C |
| 37 °C | 30 °C |
| 49 °C | 40 °C |
| 61 °C | 50 °C |

The calibration successfully removes the modeled systematic errors.

## Noise Simulation

A constant temperature of 25 °C was simulated using 1,000 measurements with additive Gaussian noise.

Simulation parameters:

- True temperature: `25 °C`
- Number of measurements: `1000`
- Noise mean: `0`
- Noise standard deviation: `0.6`
- Random seed: `42`

The simulated measurements were calibrated using the previously estimated coefficients.

### Results

| Metric | Result |
|---|---|
| True temperature | 25.0000 °C |
| Mean calibrated temperature | 24.9856 °C |
| Standard deviation | 0.4944 °C |
| Absolute error of the sample mean | 0.0144 °C |

The theoretical standard deviation after calibration is:

$$
\sigma_{\text{corrected}} = \frac{0.6}{1.2} = 0.5\ ^\circ C
$$

The simulated result agrees closely with the theoretical prediction.

## Measurement Averaging

Averaging different numbers of calibrated measurements produced the following results:

| Number of Measurements | Mean Temperature | Absolute Error |
|---|---|---|
| 5 | 24.90047 °C | 0.09953 °C |
| 20 | 24.98353 °C | 0.01647 °C |
| 200 | 24.98477 °C | 0.01523 °C |
| 1000 | 24.98555 °C | 0.01445 °C |

For independent, identically distributed measurements with zero-mean random noise:

$$
\sigma_{\text{mean}} = \frac{\sigma}{\sqrt{N}}
$$

Averaging reduces the statistical uncertainty of the sample mean but does not eliminate systematic errors.

## Visualization

Matplotlib is used to visualize the calibrated sensor readings alongside the true temperature.

The plot demonstrates that individual measurements fluctuate due to random noise even when the actual temperature remains constant.

## Technologies

- Python
- NumPy
- Matplotlib

## Project Structure

```text
sensor_lab/
├── sensor_calibration.py
└── README.md
```

## How to Run

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the experiment:

```bash
python sensor_calibration.py
```

## Key Takeaways

1. Sensor sensitivity determines how strongly the output responds to changes in the measured physical quantity.
2. High resolution does not necessarily imply high accuracy.
3. Linear calibration can compensate for systematic gain and offset errors.
4. Calibration does not eliminate random measurement noise.
5. Averaging independent measurements can reduce random uncertainty.
6. Calibration models must be validated over the intended measurement range.
7. Real sensors may exhibit nonlinear behavior that cannot be corrected using a simple linear model.

## Conclusion

This lesson demonstrated the fundamental principles of sensor calibration through mathematical modeling, numerical simulation, and measurement analysis.

The experiment established a foundation for future work involving analog front-end circuits, data acquisition, ADCs, and physical measurement systems.


## Lesson #126 — Analog Front-End and Dynamic Range

### Objective

Investigate sensor signal amplification, linearity, output saturation, and gain selection using LTspice.

### Simulation Setup

- Sensor voltage: 50–250 mV
- Load resistance: 10 kOhm
- Initial gain: 10
- Output voltage limit: 3.3 V
- Analysis: DC sweep

### Experiments

1. An ideal voltage-controlled amplifier with gain 10 produced a linear output from 0.5 V to 2.5 V.
2. Increasing the gain to 20 and limiting the output to 3.3 V produced clipping above an input voltage of 165 mV.
3. For an extended sensor range reaching 400 mV, a gain of 7 was selected, producing a maximum output of 2.8 V and leaving 0.5 V of headroom.

### Interpretation

Excessive gain causes saturation and irreversible information loss.

Ideal amplification increases both signal and existing noise by the same factor, leaving their ratio unchanged. Real amplifiers can introduce additional noise.

The saturation experiment used a behavioral voltage source rather than a physical operational amplifier model.

The numerical dynamic range was not measured because no minimum detectable signal or noise floor was specified.

### Conclusion

The analog front-end must provide sufficient amplification while preserving signal integrity across the expected sensor range.

## Lesson #127 — Operational and Instrumentation Amplifiers

### Objective

Investigate differential amplification, negative feedback, common-mode rejection, and the effect of resistor mismatch using LTspice.

### Simulation Setup

- Software: LTspice
- Operational amplifiers: 3 × UniversalOpamp2
- Supply voltage: ±5 V
- Initial inputs: V1 = 1.002 V, V2 = 0.998 V
- Differential input voltage: 4 mV
- Analysis: DC operating point (.op)

The circuit uses three operational amplifiers in a custom differential configuration. It is not the conventional three-op-amp instrumentation amplifier topology.

### Experiment 1 — Differential Amplification

With matched resistor ratios, the circuit produced:

- Differential input: 4 mV
- Output voltage: -0.399919 V
- Effective differential gain: approximately -99.98
- Current through the 200-ohm resistor: approximately 20 µA

The simulation demonstrated amplification of a small differential voltage using negative feedback.

### Experiment 2 — Common-Mode Rejection

Both input voltages were increased by 300 mV:

- V1 = 1.302 V
- V2 = 1.298 V
- Differential input: 4 mV
- Output voltage: -0.399919 V

The output remained unchanged at the displayed precision.

This demonstrated common-mode rejection in the simulated matched circuit.

### Experiment 3 — Resistor Mismatch

One resistor was changed from 1 MΩ to 990 kΩ, representing a 1% decrease.

Results:

- Matched configuration: -0.399919 V
- Modified configuration: -0.412897 V
- Output difference: -12.978 mV
- Relative output deviation: approximately 3.25%

The experiment demonstrated the sensitivity of differential amplification to resistor matching.

A separate common-mode sweep with fixed resistor values would be necessary to quantify the CMRR after the mismatch.

### Engineering Interpretation

The experiments demonstrated that:

1. Negative feedback enables controlled amplification.
2. Differential amplifiers can reject signals shared by both inputs.
3. Accurate resistor ratios are important for common-mode rejection.
4. Small component tolerances can produce measurable output errors.
5. A high CMRR does not guarantee operation outside the amplifier's allowed input common-mode range.
6. Real instrumentation amplifiers must be designed with input voltage range, supply limits, and component tolerances in mind.

### Conclusion

This laboratory demonstrated the practical principles of differential amplification and common-mode rejection.

The LTspice experiments established a foundation for precision sensor measurements and biomedical signal acquisition.
