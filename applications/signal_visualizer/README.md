# Signal Visualizer

A collection of Python experiments for building intuition about signals, LTI systems, impulse response, convolution, frequency response, Bode plots, and first-order filtering.

The project connects mathematical models with numerical calculations and visualizations in both the time and frequency domains.

## Concepts

- Complex exponentials and their real and imaginary components
- Time delay and phase shift
- Complex exponentials as eigenfunctions of LTI systems
- Unit impulses and shifted impulses
- Impulse response of an LTI system
- Discrete-time convolution
- Input-side convolution as a sum of shifted and scaled impulse responses
- Commutativity of convolution
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
- Creates shifted and scaled unit impulses
- Visualizes several discrete-time impulse responses
- Calculates the response of a first-order low-pass filter
- Calculates the response of a first-order high-pass filter
- Identifies the frequency sample closest to the cutoff frequency
- Displays magnitude in decibels on a logarithmic frequency axis
- Measures the low-pass slope between two frequencies
- Compares low-pass and high-pass magnitude responses on the same Bode plot
- Numerically verifies complementary magnitude responses using `np.allclose`
- Applies magnitude attenuation and phase shift to individual sinusoidal components
- Reconstructs and compares composite input and filtered output signals
- Implements discrete-time convolution manually using nested loops
- Verifies manual convolution against `np.convolve`
- Verifies the commutative property of convolution
- Visualizes the input, impulse response, and convolution output
- Decomposes the output into shifted and scaled impulse-response contributions
- Reconstructs the output by summing all individual contributions

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

Shifted unit impulse:

```text
δ[n - n0] = 1,  n = n0
δ[n - n0] = 0,  n ≠ n0
```

Example impulse responses:

```text
h1[n] = 2δ[n]
h2[n] = δ[n - 1]
h3[n] = δ[n] + 0.5δ[n - 1]
```

Discrete-time convolution:

```text
y[n] = x[n] * h[n]
y[n] = sum_k x[k]h[n - k]
```

Input-side contribution produced by one input sample:

```text
c_k[n] = x[k]h[n - k]
y[n] = sum_k c_k[n]
```

Output length for finite signals:

```text
N_y = N_x + N_h - 1
```

Commutativity of convolution:

```text
x[n] * h[n] = h[n] * x[n]
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
- `impulse_response.py` - creates and visualizes shifted and scaled discrete-time impulse responses
- `convolution.py` - implements manual discrete-time convolution and visualizes every shifted and scaled contribution

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

Impulse-response visualization:

```bash
python impulse_response.py
```

Manual discrete-time convolution:

```bash
python convolution.py
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

The impulse-response experiment visualizes:

```text
h1[n] = 2δ[n]
h2[n] = δ[n - 1]
h3[n] = δ[n] + 0.5δ[n - 1]
```

For the convolution experiment with `x = [1, 2, 4, 7]` and `h = [1, -1]`:

```text
Manual convolution: [ 1.  1.  2.  3. -7.]
NumPy convolution: [ 1  1  2  3 -7]
Matching: True
Convolution is commutative: True
Contribution sum: [ 1.  1.  2.  3. -7.]
Matching: True
```

The contribution matrix is:

```text
[[ 1. -1.  0.  0.  0.]
 [ 0.  2. -2.  0.  0.]
 [ 0.  0.  4. -4.  0.]
 [ 0.  0.  0.  7. -7.]]
```

Each row is one shifted and scaled copy of the impulse response. Summing the rows reconstructs the complete output:

```text
y[n] = [1, 1, 2, 3, -7]
```

For `h = [1, -1]`, the system calculates the difference between consecutive input samples:

```text
y[n] = x[n] - x[n - 1]
```

Samples outside the finite input sequence are treated as zero.

## Learning Progress


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
- Unit impulses and impulse response
- Discrete-time convolution
- Input-side construction using shifted and scaled impulse responses
- Convolution commutativity and numerical verification