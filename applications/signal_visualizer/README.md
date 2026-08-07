# Signal Visualizer

A collection of Python experiments for building intuition about signals, LTI systems, frequency response, Bode plots, and first-order filtering.

The project connects mathematical models with numerical calculations and visualizations in both the time and frequency domains.

## Concepts

- Complex exponentials and their real and imaginary components
- Time delay and phase shift
- Complex exponentials as eigenfunctions of LTI systems
- Magnitude and phase of a frequency response
- Wrapped and unwrapped phase
- First-order low-pass filters
- First-order high-pass filters
- Cutoff frequency and the -3 dB point
- Decibels and Bode plots
- Logarithmic frequency axes
- Frequency-response slope in decibels per decade
- Complementary low-pass and high-pass magnitude responses
- Filtering a signal composed of multiple sinusoidal components

## Features

- Visualizes the real and imaginary parts of a complex exponential
- Compares an original sinusoid with its delayed version
- Verifies the eigenfunction property of complex exponentials for an LTI delay system
- Displays magnitude, wrapped phase, and unwrapped phase
- Calculates the response of a first-order low-pass filter
- Calculates the response of a first-order high-pass filter
- Identifies the frequency sample closest to the cutoff frequency
- Displays magnitude in decibels on a logarithmic frequency axis
- Measures the low-pass slope between two frequencies
- Compares low-pass and high-pass magnitude responses on the same Bode plot
- Numerically verifies complementary magnitude responses using `np.allclose`
- Applies magnitude attenuation and phase shift to individual sinusoidal components
- Reconstructs and compares composite input and filtered output signals

## Mathematical Models

Complex exponential:

```text
x(t) = exp(j2πft)
```

Pure time delay:

```text
y(t) = x(t - τ)
H(f) = exp(-j2πfτ)
```

Normalized frequency ratio:

```text
r = f / fc
```

First-order low-pass filter:

```text
H_LP(f) = 1 / (1 + jr)
```

First-order high-pass filter:

```text
H_HP(f) = jr / (1 + jr)
```

Low-pass magnitude:

```text
|H_LP(f)| = 1 / sqrt(1 + r²)
```

High-pass magnitude:

```text
|H_HP(f)| = r / sqrt(1 + r²)
```

Magnitude in decibels:

```text
M_dB(f) = 20 log10(|H(f)|)
```

Low-pass phase:

```text
phase_LP(f) = -arctan(r)
```

High-pass phase:

```text
phase_HP(f) = 90° - arctan(r)
```

Slope between two frequencies:

```text
s = (M2 - M1) / log10(f2/f1)
```

Complementary magnitude-response identity:

```text
|H_LP(f)|² + |H_HP(f)|² = 1
```

## Project Structure

- `frequency_explorer.py` - visualizes the real and imaginary parts of a complex exponential
- `delay_phase_explorer.py` - compares an original signal with a delayed signal
- `lti_eigenfunction_explorer.py` - verifies that a complex exponential keeps its form through an LTI delay system
- `frequency_response_explorer.py` - visualizes the magnitude and wrapped and unwrapped phase of a pure delay
- `low_pass_frequency_response.py` - analyzes the magnitude and phase of a first-order low-pass filter
- `low_pass_bode_explorer.py` - displays the low-pass Bode response and measures the high-frequency slope
- `high_pass_bode_explorer.py` - displays the high-pass Bode response, compares it with the low-pass response, and verifies their complementary magnitudes
- `low_pass_signal_filter.py` - filters a composite signal by processing its sinusoidal components separately

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
pip install numpy matplotlib
```

## Run

Open a terminal in `applications/signal_visualizer` and run any experiment separately.

Complex exponential:

```bash
python frequency_explorer.py
```

Delay and phase shift:

```bash
python delay_phase_explorer.py
```

LTI eigenfunction:

```bash
python lti_eigenfunction_explorer.py
```

Pure-delay frequency response:

```bash
python frequency_response_explorer.py
```

First-order low-pass response:

```bash
python low_pass_frequency_response.py
```

Low-pass Bode plot and slope measurement:

```bash
python low_pass_bode_explorer.py
```

High-pass Bode plot and low-pass comparison:

```bash
python high_pass_bode_explorer.py
```

Composite-signal filtering:

```bash
python low_pass_signal_filter.py
```

## Expected Results

For a first-order low-pass filter at the cutoff frequency:

```text
|H_LP(fc)| ≈ 0.707
M_LP(fc) ≈ -3.01 dB
phase_LP(fc) ≈ -45°
```

For a first-order high-pass filter at the cutoff frequency:

```text
|H_HP(fc)| ≈ 0.707
M_HP(fc) ≈ -3.01 dB
phase_HP(fc) ≈ 45°
```

For the high-pass Bode experiment, the numerical verification should return:

```text
Complementary magnitude responses: True
```

The low-pass and high-pass magnitude responses satisfy:

```text
|H_LP(f)|² + |H_HP(f)|² = 1
```

Far above the cutoff frequency, the low-pass magnitude approaches a slope of:

```text
-20 dB/decade
```

Far below the cutoff frequency, the high-pass magnitude approaches a slope of:

```text
+20 dB/decade
```

The limiting behavior of the high-pass filter is:

```text
f << fc: |H_HP| approaches 0 and phase approaches 90°
f >> fc: |H_HP| approaches 1 and phase approaches 0°
```

For the composite filtering experiment with `fc = 2 Hz`:

- the 1 Hz component is only moderately attenuated and phase shifted
- the 20 Hz component is strongly attenuated and shifted close to -90°
- the output keeps both original frequencies because an LTI system changes their amplitudes and phases, not their frequencies

## Learning Progress

This project contains the practical work from lessons 14 through 20 of the PolyMath curriculum:

- Complex exponentials
- Delay and phase shift
- LTI eigenfunctions
- Frequency response
- First-order low-pass response
- Decibels and Bode plots
- Low-pass slope measurement
- Filtering a composite signal
- First-order high-pass response
- Complementary low-pass and high-pass magnitude responses