# Signal Visualizer

A collection of Python experiments for building intuition about signals, LTI systems, frequency response, Bode plots, and first-order low-pass filtering.

The project connects mathematical models with numerical calculations and visualizations in both the time and frequency domains.

## Concepts

- Complex exponentials and their real and imaginary components
- Time delay and phase shift
- Complex exponentials as eigenfunctions of LTI systems
- Magnitude and phase of a frequency response
- Wrapped and unwrapped phase
- First-order low-pass filters
- Decibels and Bode plots
- High-frequency slope in dB per decade
- Filtering a signal composed of multiple sinusoidal components

## Features

- Visualizes the real and imaginary parts of a complex exponential
- Compares an original sinusoid with its delayed version
- Verifies the eigenfunction property of complex exponentials for an LTI delay system
- Displays magnitude, wrapped phase, and unwrapped phase
- Calculates the response of a first-order low-pass filter
- Identifies the frequency sample closest to the cutoff frequency
- Displays magnitude in decibels on a logarithmic frequency axis
- Measures the low-pass slope between two frequencies
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

First-order low-pass filter:

```text
H(f) = 1 / (1 + jf/fc)
```

Magnitude in decibels:

```text
M_dB(f) = 20 log10(|H(f)|)
```

Slope between two frequencies:

```text
s = (M2 - M1) / log10(f2/f1)
```

## Project Structure

- `frequency_explorer.py` - visualizes the real and imaginary parts of a complex exponential
- `delay_phase_explorer.py` - compares an original signal with a delayed signal
- `lti_eigenfunction_explorer.py` - verifies that a complex exponential keeps its form through an LTI delay system
- `frequency_response_explorer.py` - visualizes the magnitude and wrapped and unwrapped phase of a pure delay
- `low_pass_frequency_response.py` - analyzes the magnitude and phase of a first-order low-pass filter
- `low_pass_bode_explorer.py` - displays the Bode response and measures the high-frequency slope
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

Composite-signal filtering:

```bash
python low_pass_signal_filter.py
```

## Expected Results

For a first-order low-pass filter at the cutoff frequency:

```text
|H(fc)| ≈ 0.707
M(fc) ≈ -3.01 dB
phase(fc) ≈ -45°
```

Far above the cutoff frequency, the magnitude approaches a slope of:

```text
-20 dB/decade
```

For the composite filtering experiment with `fc = 2 Hz`:

- the 1 Hz component is only moderately attenuated and phase shifted
- the 20 Hz component is strongly attenuated and shifted close to -90°
- the output keeps both original frequencies because an LTI system changes their amplitudes and phases, not their frequencies

## Learning Progress

This project contains the practical work from lessons 14 through 20 of the PolyMath curriculum:

- Complex exponentials
- Delay and phase
- LTI eigenfunctions
- Frequency response
- First-order low-pass response
- Decibels and Bode plots
- Filtering a composite signal
