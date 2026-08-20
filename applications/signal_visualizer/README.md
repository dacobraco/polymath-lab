# Signal Visualizer

A collection of Python and MATLAB experiments for building intuition about signals, LTI systems, impulse response, convolution, the convolution theorem, FFT-based filtering, frequency response, Bode plots, first-order filtering, Fourier series, Fourier transforms, Fourier-transform properties, time shifting, time scaling, modulation, signal energy, Parseval's theorem, rectangular pulses, sinc spectra, time-bandwidth relationships, harmonic reconstruction, quantitative reconstruction error, signal symmetry, line spectra, and the transition from discrete to continuous spectra.

The project connects mathematical models with numerical calculations and visualizations in both the time and frequency domains.

## Concepts

* Complex exponentials and their real and imaginary components
* Time delay and phase shift
* Complex exponentials as eigenfunctions of LTI systems
* Unit impulses and shifted impulses
* Impulse response of an LTI system
* Discrete-time convolution
* Input-side convolution as a sum of shifted and scaled impulse responses
* Output-side convolution
* Commutativity of convolution
* Convolution theorem
* Linear and circular convolution
* Fast Fourier transform and inverse fast Fourier transform
* Zero-padding for FFT-based linear convolution
* Equivalence of time-domain convolution and frequency-domain multiplication
* Moving-average filtering
* Floating-point error in FFT-based convolution verification
* Magnitude and phase of a frequency response
* Wrapped and unwrapped phase
* First-order low-pass filters
* First-order high-pass filters
* Cutoff frequency and the -3 dB point
* Decibels and Bode plots
* Logarithmic frequency axes
* Frequency-response slope in decibels per decade
* Complementary low-pass and high-pass magnitude responses
* Filtering a signal composed of multiple sinusoidal components
* Fourier series representation of periodic signals
* Fundamental frequency and harmonics
* Harmonic reconstruction of a square wave
* Odd harmonics and the Gibbs phenomenon
* Inner products of real signals over one period
* Orthogonal sinusoidal basis functions
* Orthogonal and orthonormal bases
* Signal projection onto sine and cosine basis functions
* Signal reconstruction from projection coefficients
* Trigonometric Fourier coefficients
* DC, cosine, and sine coefficients
* Signal symmetry and vanishing Fourier coefficients
* Even, odd, and half-wave symmetry
* Symbolic and numerical integration
* Numerical approximation error
* Periodic extension and normalized-time wrapping
* Fourier-series reconstruction of a sawtooth signal
* Alternating Fourier sine coefficients
* Partial sums using consecutive harmonics
* Root mean square reconstruction error
* Convergence at periodic discontinuities
* Discrete line spectra of periodic signals
* Harmonic amplitude and phase spectra
* Conversion from trigonometric coefficients to amplitude-phase form
* Fourier transform representation of nonperiodic signals
* Continuous frequency spectra
* Relationship between the Fourier series and Fourier transform
* Spectral-line spacing and its dependence on the period
* Rectangular pulses and sinc-shaped spectra
* Time-width and frequency-width relationship
* Transition from a discrete line spectrum to a continuous spectrum
* Fourier-transform integrals as limits of Fourier-series sums
* MATLAB vectors and one-based indexing
* Row and column vectors in MATLAB
* Matrix and element-wise operations in MATLAB
* Signal generation and visualization in MATLAB
* Equivalent signal workflows in MATLAB and NumPy
* Definition of the continuous-time Fourier transform
* Inverse Fourier transform
* Linearity of the Fourier transform
* Duality of the Fourier transform
* Double Fourier transformation and time reversal
* Numerical Fourier-transform approximation from the defining integral
* Gaussian signals as test functions for Fourier-transform properties
* Numerical verification of transform properties in Python and MATLAB
* Time shifting and linear phase
* Time scaling and reciprocal frequency scaling
* Compression in time and expansion in frequency
* Complex exponential modulation
* Frequency translation of a spectrum
* Cosine modulation
* Positive- and negative-frequency spectral copies
* Relationship between real modulation and complex exponentials
* Signal energy
* Squared signal magnitude and energy integrals
* Relationship between signal energy and the inner product
* Parseval's theorem
* Conservation of energy between time and frequency representations
* Numerical integration using SciPy
* Floating-point error in numerical energy verification
* Pulse width
* Frequency bandwidth
* First-null bandwidth
* Main lobes and side lobes
* First spectral nulls
* Band-limited and non-band-limited signals
* Inverse time-bandwidth relationship
* Time-bandwidth product
* DC value of a rectangular-pulse spectrum
* Relationship between pulse area and `X(0)`

## Features

* Visualizes the real and imaginary parts of a complex exponential
* Compares an original sinusoid with its delayed version
* Verifies the eigenfunction property of complex exponentials for an LTI delay system
* Displays magnitude, wrapped phase, and unwrapped phase
* Creates shifted and scaled unit impulses
* Visualizes several discrete-time impulse responses
* Calculates the response of a first-order low-pass filter
* Calculates the response of a first-order high-pass filter
* Identifies the frequency sample closest to the cutoff frequency
* Displays magnitude in decibels on a logarithmic frequency axis
* Measures the low-pass slope between two frequencies
* Compares low-pass and high-pass magnitude responses on the same Bode plot
* Numerically verifies complementary magnitude responses using `np.allclose`
* Applies magnitude attenuation and phase shift to individual sinusoidal components
* Reconstructs and compares composite input and filtered output signals
* Implements discrete-time convolution manually using nested loops
* Accepts interactive comma-separated input sequences
* Verifies manual convolution against `np.convolve`
* Verifies the commutative property of convolution
* Visualizes the input, impulse response, and convolution output
* Decomposes the output into shifted and scaled impulse-response contributions
* Reconstructs the output by summing all individual contributions
* Includes pytest tests for a known result, commutativity, and output length
* Verifies the convolution theorem using direct convolution and FFT multiplication
* Uses zero-padding with `N = N_x + N_h - 1` to reproduce linear convolution
* Demonstrates the difference between linear and circular convolution
* Applies a five-sample moving-average filter to a signal containing 2 Hz and 20 Hz components
* Compares time-domain and frequency-domain filtering results
* Measures the maximum numerical difference between both methods
* Visualizes the input signal, overlapping filtered outputs, and absolute error
* Reconstructs a square wave using odd Fourier harmonics
* Generates partial sums for maximum harmonics `K = 1, 3, 5, and 9`
* Stores harmonic reconstructions generated by nested loops
* Compares Fourier approximations with an ideal square wave
* Visualizes Gibbs oscillations near signal discontinuities
* Calculates numerical inner products over one period
* Verifies the orthogonality of different sinusoidal basis functions
* Projects a composite signal onto sine and cosine basis functions
* Recovers the coefficients of the original signal components
* Reconstructs the signal and verifies the result using `np.allclose`
* Calculates the Fourier coefficients of a square wave symbolically with SymPy
* Approximates the same Fourier coefficients using numerical integration
* Compares symbolic and numerical coefficients in a formatted table
* Calculates the absolute error between both methods
* Verifies the expected symmetry and odd-harmonic coefficient pattern
* Visualizes symbolic and numerical sine coefficients on the same stem plot
* Constructs an ideal periodically repeated sawtooth signal using normalized-time wrapping
* Reconstructs the sawtooth using all harmonics from 1 through `N`
* Compares partial sums for `N = 1, 3, 5, and 20`
* Calculates RMSE between the ideal signal and every reconstruction
* Verifies that reconstruction error decreases as more harmonics are included
* Displays the ideal sawtooth and four Fourier reconstructions in a 2-by-2 subplot layout
* Visualizes narrowing Gibbs oscillations near the periodic discontinuities
* Calculates the first ten Fourier coefficients of an odd sawtooth signal
* Converts cosine and sine coefficients into harmonic amplitudes and phases
* Displays the sawtooth amplitude and phase spectra using stem plots
* Demonstrates the presence of both even and odd sawtooth harmonics
* Visualizes alternating harmonic phases of -90 and 90 degrees
* Integrates square-wave and sawtooth Fourier analysis into one interactive application
* Allows the user to select the signal type and number of harmonics
* Separates reusable mathematical functions from input and visualization logic
* Generates the ideal signal and its Fourier reconstruction
* Calculates Fourier coefficients, RMSE, harmonic amplitudes, and phases
* Displays the reconstruction, amplitude spectrum, and phase spectrum together
* Validates unsupported signal types, nonpositive harmonic counts, and incompatible array shapes
* Includes 15 automated unit tests for numerical results and input validation
* Calculates the continuous sinc spectrum of a rectangular pulse
* Calculates Fourier-series coefficients for periodically repeated pulses
* Scales the coefficients using `T C_k` for direct comparison with the Fourier transform
* Compares the continuous spectrum with discrete samples at harmonic frequencies
* Displays the comparison for `T = 2, 4, 8, and 16 s`
* Demonstrates that the line spacing `Δf = 1/T` decreases as the period increases
* Visualizes the transition from a discrete line spectrum to a continuous spectrum
* Displays all four transition stages in a 2-by-2 subplot layout
* Generates and plots a sinusoidal signal in MATLAB
* Demonstrates MATLAB vector creation, indexing, and element-wise operations
* Reproduces the same sinusoidal signal using NumPy and Matplotlib
* Compares basic MATLAB signal-processing syntax with its NumPy equivalent
* Implements the continuous-time Fourier-transform integral numerically in Python
* Implements the same numerical Fourier-transform calculation in MATLAB
* Verifies Fourier-transform linearity using two Gaussian signals
* Verifies Fourier-transform duality using a shifted Gaussian signal
* Demonstrates that applying the Fourier transform twice produces a reflected signal
* Measures the maximum numerical error of the MATLAB linearity and duality checks
* Verifies that time shifting changes spectral phase while preserving spectral magnitude
* Verifies reciprocal time and frequency scaling using a Gaussian signal
* Demonstrates that compressing a signal in time expands its spectrum
* Verifies complex modulation as a frequency-domain translation
* Verifies cosine modulation as the creation of two shifted spectral copies
* Measures numerical errors for all Fourier shifting, scaling, and modulation properties
* Displays four time-domain and frequency-domain signal-spectrum pairs in a 4-by-2 layout
* Calculates the energy of a Gaussian signal in the time domain
* Calculates the same energy from the Fourier-transform magnitude
* Uses SciPy Simpson integration for numerical energy calculations
* Numerically verifies Parseval's theorem
* Compares numerical energy with the analytical Gaussian result
* Measures Parseval error near machine precision
* Generates rectangular pulses with several pulse widths
* Calculates their analytical sinc spectra
* Calculates first-null bandwidth using `B = 1/τ`
* Marks positive and negative first spectral nulls
* Compares pulse width and spectral width in a 4-by-2 Python explorer
* Reproduces the time-bandwidth explorer in MATLAB
* Demonstrates that shorter pulses require larger bandwidth
* Demonstrates that longer pulses produce narrower main lobes
* Verifies that the spectrum peak satisfies `X(0) = τ`
* Demonstrates the constant first-null time-bandwidth product `τB = 1`
* Shows that rectangular pulses are not strictly band-limited because sinc side lobes extend indefinitely

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
δ[n - n0] = 1, n = n0
δ[n - n0] = 0, n ≠ n0
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

Convolution theorem:

```text
y[n] = x[n] * h[n]
Y[k] = X[k]H[k]
y[n] = IFFT{FFT{x[n]} FFT{h[n]}}
```

Minimum FFT length for reproducing linear convolution:

```text
N_FFT = N_x + N_h - 1
```

Zero-padding both finite sequences to `N_FFT` prevents circular wrap-around and makes FFT multiplication reproduce the complete linear-convolution result.

Five-sample moving-average filter:

```text
h[n] = [1/5, 1/5, 1/5, 1/5, 1/5]
```

For a sampling frequency of `100 Hz`, a `20 Hz` sinusoid has five samples per period:

```text
samples_per_period = 100 / 20 = 5
```

Averaging one complete period strongly suppresses the 20 Hz component while preserving the slower 2 Hz component.

Square-wave Fourier series:

```text
x(t) = (4/π) sum_{k=1,3,5,...} sin(kω0t) / k
```

Partial reconstruction up to the highest odd harmonic `K`:

```text
x_K(t) = (4/π) sum_{k=1,3,5,...,K} sin(kω0t) / k
```

Fundamental frequency and angular frequency:

```text
f0 = 1 / T
ω0 = 2πf0
```

Harmonic frequencies of a periodic signal:

```text
f_n = nf0
ω_n = nω0
```

Amplitude of the odd square-wave harmonic `k`:

```text
A_k = 4 / (πk)
```

Continuous-time inner product over one period:

```text
<x, y> = integral from 0 to T of x(t)y(t) dt
```

Numerical approximation of the inner product:

```text
<x, y> ≈ dt sum_n x[n]y[n]
```

Orthogonality condition:

```text
<x, y> = 0
```

Projection coefficient onto a basis function:

```text
c = <x, b> / <b, b>
```

Signal reconstruction from basis functions:

```text
x_reconstructed(t) = sum_k c_k b_k(t)
```

Trigonometric Fourier series:

```text
x(t) = a0/2 + sum_n [a_n cos(nω0t) + b_n sin(nω0t)]
```

Fourier coefficients over one period:

```text
a0 = (2/T) integral_T x(t) dt
a_n = (2/T) integral_T x(t)cos(nω0t) dt
b_n = (2/T) integral_T x(t)sin(nω0t) dt
```

Symmetry properties:

```text
Even signal:
x(-t) = x(t)
b_n = 0

Odd signal:
x(-t) = -x(t)
a0 = 0
a_n = 0

Half-wave symmetry:
x(t + T/2) = -x(t)
DC and even harmonics vanish
```

Sine coefficients of the odd square wave:

```text
b_n = 4/(nπ), n odd
b_n = 0,       n even
```

Absolute coefficient error:

```text
absolute_error = |symbolic_b_n - numerical_b_n|
```

Normalized periodic wrapping into the interval `[-π, π)`:

```text
t_wrapped = (t + π) mod (2π) - π
```

Normalized sawtooth signal over one period:

```text
x(t) = t / π, -π < t < π
```

Fourier sine coefficients of the normalized sawtooth:

```text
a0 = 0
a_n = 0
b_n = 2(-1)^(n + 1) / (πn)
```

Sawtooth reconstruction using the first `N` consecutive harmonics:

```text
x_N(t) = (2/π) sum from n=1 to N of [(-1)^(n + 1) / n] sin(nt)
```

Root mean square reconstruction error:

```text
RMSE = sqrt(mean((x_ideal - x_N)²))
```

Fourier-series value at a jump discontinuity:

```text
x_N(t_jump) approaches (x_left + x_right) / 2
For a jump from 1 to -1, the limiting value is 0.
```

Amplitude-phase form of one harmonic:

```text
a_n cos(nω0t) + b_n sin(nω0t)
= A_n cos(nω0t + phase_n)
```

Harmonic amplitude:

```text
A_n = sqrt(a_n² + b_n²)
```

Harmonic phase:

```text
phase_n = atan2(-b_n, a_n)
```

Amplitude and phase of the normalized sawtooth harmonics:

```text
A_n = 2 / (πn)

phase_n = -90°, n odd
phase_n = 90°,  n even
```

Fourier transform:

```text
X(f) = integral from -∞ to ∞ of x(t)exp(-j2πft) dt
```

Inverse Fourier transform:

```text
x(t) = integral from -∞ to ∞ of X(f)exp(j2πft) df
```

Fourier-transform linearity:

```text
If:
x1(t) <-> X1(f)
x2(t) <-> X2(f)

Then:
a x1(t) + b x2(t) <-> a X1(f) + b X2(f)
```

Fourier-transform duality:

```text
If:
x(t) <-> X(f)

Then:
X(t) <-> x(-f)
```

Applying the Fourier transform twice:

```text
F{F{x(t)}} = x(-t)
```

Shifted Gaussian used for the numerical duality test:

```text
x(t) = exp(-π(t - 1)²)
x(-t) = exp(-π(t + 1)²)
```

Numerical Fourier-transform approximation over a finite interval:

```text
X(f) ≈ integral over the sampled time interval of
       x(t)exp(-j2πft) dt
```

Fourier-transform time-shift property:

```text
x(t - t0) <-> X(f)exp(-j2πft0)
```

For a delay of `t0 = 2 s`:

```text
x(t - 2) <-> X(f)exp(-j4πf)
```

Time shifting preserves the magnitude spectrum:

```text
|X_shifted(f)| = |X(f)|
```

Fourier-transform time-scaling property:

```text
x(at) <-> (1/|a|)X(f/a)
```

For `a = 2`:

```text
x(2t) <-> (1/2)X(f/2)
```

Complex exponential modulation:

```text
x(t)exp(j2πf0t) <-> X(f - f0)
```

For `f0 = 2 Hz`:

```text
x(t)exp(j4πt) <-> X(f - 2)
```

Euler representation of a cosine:

```text
cos(2πf0t)
= (1/2)exp(j2πf0t) + (1/2)exp(-j2πf0t)
```

Cosine modulation:

```text
x(t)cos(2πf0t)
<-> (1/2)X(f - f0) + (1/2)X(f + f0)
```

For `f0 = 2 Hz`, the two spectral copies are centered at:

```text
f = -2 Hz
f = 2 Hz
```

Signal energy:

```text
E_x = integral from -∞ to ∞ of |x(t)|² dt
```

Energy as an inner product:

```text
E_x = <x, x>
```

Scaling of signal energy:

```text
If:
y(t) = a x(t)

Then:
E_y = |a|² E_x
```

Parseval's theorem for the Fourier-transform convention used in this project:

```text
X(f) = integral from -∞ to ∞ of x(t)exp(-j2πft) dt
```

is:

```text
integral from -∞ to ∞ of |x(t)|² dt
=
integral from -∞ to ∞ of |X(f)|² df
```

Therefore:

```text
E_time = E_frequency
```

Gaussian used for the Parseval experiment:

```text
x(t) = exp(-πt²)
```

Its squared magnitude is:

```text
|x(t)|² = exp(-2πt²)
```

Analytical Gaussian energy:

```text
E = integral from -∞ to ∞ of exp(-2πt²) dt
E = 1 / sqrt(2)
E ≈ 0.7071067811865476
```

Numerical Parseval error:

```text
parseval_error = |E_time - E_frequency|
```

Rectangular pulse of width `τ`:

```text
x(t) = 1, |t| <= τ/2
x(t) = 0, otherwise
```

Fourier transform of the rectangular pulse:

```text
X(f) = τ sinc(fτ)
```

Normalized sinc definition used by NumPy and MATLAB:

```text
sinc(u) = sin(πu) / (πu)
sinc(0) = 1
```

DC value of the rectangular-pulse spectrum:

```text
X(0) = τ sinc(0)
X(0) = τ
```

The same result follows from pulse area:

```text
X(0) = integral from -∞ to ∞ of x(t) dt
X(0) = pulse height × pulse width
X(0) = 1 × τ
X(0) = τ
```

First spectral nulls:

```text
f_null = ±1/τ
```

First-null bandwidth:

```text
B = 1/τ
```

Total main-lobe width:

```text
main_lobe_width = 2/τ
```

First-null time-bandwidth product:

```text
τB = 1
```

Inverse time-bandwidth relationship:

```text
τ decreases -> B increases
τ increases -> B decreases
```

The rectangular pulse is not strictly band-limited:

```text
X(f) != 0 for infinitely many frequencies beyond the first null.
```

NumPy uses the normalized sinc definition:

```text
np.sinc(u) = sin(πu) / (πu)
```

Harmonic frequencies and line spacing for a periodic signal:

```text
f_k = k / T
Δf = 1 / T
```

Fourier-series coefficients of a periodically repeated rectangular pulse:

```text
C_k = (τ/T) sinc(kτ/T)
```

Relationship between Fourier-series coefficients and Fourier-transform samples:

```text
C_k = (1/T)X(f_k)
C_k = Δf X(f_k)
T C_k = X(f_k)
```

Transition from the Fourier-series sum to the Fourier-transform integral:

```text
x(t) = sum_k X(f_k)exp(j2πf_k t)Δf

As T approaches ∞:
Δf approaches 0

x(t) = integral from -∞ to ∞ of X(f)exp(j2πft) df
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

Sinusoidal signal:

```text
x(t) = sin(2πft)
```

Signal period:

```text
T = 1 / f
```

For the introductory MATLAB example:

```text
f = 2 Hz
T = 0.5 s
```

## Project Structure

* `frequency_explorer.py` - visualizes the real and imaginary parts of a complex exponential
* `delay_phase_explorer.py` - compares an original signal with its delayed signal
* `lti_eigenfunction_explorer.py` - verifies that a complex exponential keeps its form through an LTI delay system
* `frequency_response_explorer.py` - visualizes the magnitude and wrapped and unwrapped phase of a pure delay
* `low_pass_frequency_response.py` - analyzes the magnitude and phase of a first-order low-pass filter
* `low_pass_bode_explorer.py` - displays the low-pass Bode response and measures the high-frequency slope
* `high_pass_bode_explorer.py` - displays the high-pass Bode response, compares it with the low-pass response, and verifies their complementary magnitudes
* `low_pass_signal_filter.py` - filters a composite signal by processing its sinusoidal components separately
* `impulse_response.py` - creates and visualizes shifted and scaled discrete-time impulse responses
* `convolution.py` - provides an interactive manual convolution laboratory and visualizes every shifted and scaled contribution
* `test_convolution.py` - tests a known convolution result, commutativity, and output length
* `fourier_series_explorer.py` - reconstructs a square wave using increasing numbers of odd Fourier harmonics
* `orthogonality_explorer.py` - verifies orthogonality, extracts projection coefficients, and reconstructs a composite signal
* `fourier_coefficients_explorer.py` - compares symbolic and numerical Fourier coefficients of an odd square wave
* `periodic_signal_reconstruction.py` - reconstructs a periodic sawtooth using consecutive harmonics and measures RMSE
* `line_spectrum_explorer.py` - calculates and visualizes the amplitude and phase spectra of the first ten sawtooth harmonics
* `fourier_utils.py` - provides reusable functions for signal generation, Fourier coefficients, reconstruction, RMSE, and spectrum calculation
* `fourier_series_visualizer.py` - integrates the Fourier-series workflow into one interactive application
* `test_fourier_series_visualizer.py` - contains 15 unit tests for Fourier calculations and validation behavior
* `fourier_transform_transition.py` - visualizes the transition from Fourier-series line spectra to a continuous Fourier-transform spectrum
* `matlab_signal_intro.m` - introduces MATLAB through the generation and visualization of a sinusoidal signal
* `matlab_numpy_intro.py` - reproduces the introductory MATLAB signal example using NumPy and Matplotlib
* `fourier_properties.py` - numerically verifies Fourier-transform linearity and duality in Python
* `fourier_properties_matlab.m` - implements the numerical Fourier-transform integral and verifies Fourier-transform linearity and duality in MATLAB
* `fourier_shift_scale_modulation.py` - verifies time shifting, time scaling, complex modulation, and cosine modulation while visualizing four signal-spectrum pairs
* `signal_energy_parseval.py` - calculates Gaussian signal energy in the time and frequency domains and numerically verifies Parseval's theorem
* `time_bandwidth_explorer.py` - compares rectangular pulses and sinc spectra for several pulse widths and first-null bandwidths
* `time_bandwidth_explorer_matlab.m` - reproduces the rectangular-pulse time-bandwidth explorer in MATLAB
* `convolution_theorem_explorer.py` - compares time-domain convolution with FFT-based frequency-domain filtering using correct zero-padding

## Requirements

* Python 3
* NumPy
* SciPy
* SymPy
* Matplotlib
* pytest
* MATLAB

Install the required Python libraries:

```bash
python -m pip install numpy scipy sympy matplotlib pytest
```

On Windows with the Python launcher:

```bash
py -m pip install numpy scipy sympy matplotlib pytest
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

Interactive discrete-time convolution:

```bash
python convolution.py
```

The program asks for the input signal and impulse response as comma-separated values:

```text
Enter x[n] as comma-separated values: 1, 2, 4, 7
Enter h[n] as comma-separated values: 1, -1
```

The manual convolution, NumPy result, commutativity check, contribution matrix, and graphical visualizations are then displayed.

Fourier-series square-wave reconstruction:

```bash
python fourier_series_explorer.py
```

The program compares an ideal square wave with Fourier partial sums whose highest included odd harmonics are:

```text
K = 1, 3, 5, 9
```

Orthogonality and signal projection:

```bash
python orthogonality_explorer.py
```

The program calculates inner products between sinusoidal basis functions, extracts the coefficients of a composite signal, and reconstructs the signal from its projections.

Symbolic and numerical Fourier coefficients:

```bash
python fourier_coefficients_explorer.py
```

The program calculates the first ten Fourier coefficients of an odd square wave, compares symbolic and numerical results, verifies the expected coefficient pattern, and displays both methods on the same stem plot.

Periodic sawtooth reconstruction:

```bash
python periodic_signal_reconstruction.py
```

The program periodically wraps normalized time into `[-π, π)`, reconstructs the sawtooth using all harmonics from 1 through `N` for `N = 1, 3, 5, and 20`, calculates RMSE, and compares all four reconstructions in a 2-by-2 subplot layout.

Sawtooth line spectrum:

```bash
python line_spectrum_explorer.py
```

The program calculates the first ten sawtooth Fourier coefficients, converts them into harmonic amplitudes and phases, and displays the amplitude and phase line spectra using two stem plots.

Fourier Series Visualizer v1:

```bash
python fourier_series_visualizer.py
```

The application asks the user to select a supported signal and the number of harmonics:

```text
Square or sawtooth signal? square
How many harmonics? 5
```

It then:

* generates the ideal periodic signal
* calculates its Fourier coefficients
* reconstructs the signal using the selected number of harmonics
* calculates RMSE
* calculates harmonic amplitudes and phases
* displays the reconstruction, amplitude spectrum, and phase spectrum

Fourier series to Fourier transform transition:

```bash
python fourier_transform_transition.py
```

The experiment:

* calculates the continuous sinc spectrum of a rectangular pulse
* generates harmonic frequencies for `T = 2, 4, 8, and 16 s`
* calculates the corresponding Fourier-series coefficients
* scales each coefficient using `T C_k`
* compares the scaled discrete lines with the continuous Fourier-transform curve
* displays the four periods in a 2-by-2 subplot layout
* demonstrates how the spectral-line spacing decreases as the period increases

MATLAB signal introduction:

```text
matlab_signal_intro.m
```

Run the script from MATLAB with `applications/signal_visualizer` set as the Current Folder.

The script:

* creates a time vector from `0` to `1 s`
* generates a `2 Hz` sinusoidal signal
* plots the signal
* labels the time and amplitude axes
* demonstrates the basic MATLAB workflow for signal visualization

NumPy comparison of the MATLAB example:

```bash
python matlab_numpy_intro.py
```

The Python experiment reproduces the same `2 Hz` sinusoidal signal using NumPy and Matplotlib so that the syntax and workflows of both environments can be compared directly.

Fourier-transform property verification in Python:

```bash
python fourier_properties.py
```

The experiment:

* approximates the continuous Fourier-transform integral numerically
* transforms two Gaussian signals
* verifies Fourier-transform linearity
* applies the transform twice to a shifted Gaussian
* verifies that the second transform produces the reflected signal `x(-t)`
* checks both properties using numerical tolerances

Fourier-transform property verification in MATLAB:

```text
fourier_properties_matlab.m
```

Run the script from MATLAB with `applications/signal_visualizer` set as the Current Folder.

The MATLAB experiment:

* uses a local `numerical_fourier_transform` function to approximate the transform integral with `trapz`
* verifies linearity using two Gaussian signals
* verifies duality using a Gaussian shifted to `t = 1`
* applies the transform twice
* compares the result with the reflected Gaussian centered at `t = -1`
* measures the maximum absolute numerical error

Fourier shift, scaling, and modulation experiment:

```bash
python fourier_shift_scale_modulation.py
```

The experiment:

* uses a Gaussian signal as the reference signal
* shifts the Gaussian by `2 s`
* verifies that time shifting preserves the magnitude spectrum and adds the predicted phase factor
* compresses the Gaussian in time using `x(2t)`
* verifies reciprocal expansion of the spectrum and the `1/2` amplitude factor
* modulates the signal with a complex exponential at `2 Hz`
* verifies translation of the spectrum to `+2 Hz`
* modulates the signal with a real cosine at `2 Hz`
* verifies the appearance of spectral copies centered at `-2 Hz` and `+2 Hz`
* calculates maximum numerical errors for all four properties
* displays four time-domain and frequency-domain signal-spectrum pairs

Signal energy and Parseval verification:

```bash
python signal_energy_parseval.py
```

On Windows with the Python launcher:

```bash
py signal_energy_parseval.py
```

The experiment:

* generates the Gaussian signal `x(t) = exp(-πt²)`
* calculates its time-domain energy using SciPy Simpson integration
* calculates its numerical Fourier transform
* integrates `|X(f)|²` over frequency
* compares time-domain and frequency-domain energies
* calculates the Parseval error
* verifies that both energy values agree to numerical precision

Python time-bandwidth explorer:

```bash
python time_bandwidth_explorer.py
```

On Windows with the Python launcher:

```bash
py time_bandwidth_explorer.py
```

The experiment:

* generates rectangular pulses with widths `τ = 0.25, 0.5, 1, and 2 s`
* calculates `X(f) = τ sinc(fτ)` for every pulse
* calculates the first-null bandwidth `B = 1/τ`
* displays each pulse next to its sinc spectrum
* marks the first spectral nulls at `±B`
* demonstrates the inverse relationship between pulse width and bandwidth
* shows that the sinc peak equals `τ`

MATLAB time-bandwidth explorer:

```text
time_bandwidth_explorer_matlab.m
```

Run the script from MATLAB with `applications/signal_visualizer` set as the Current Folder.

The MATLAB experiment:

* reproduces the four pulse-width cases from the Python explorer
* uses `linspace`, logical indexing, `sinc`, `for`, `subplot`, `xline`, and `sprintf`
* displays the rectangular pulse in the time domain
* displays its sinc spectrum in the frequency domain
* marks the positive and negative first spectral nulls
* demonstrates the same time-bandwidth relationship as the Python implementation

Convolution-theorem explorer:

```bash
python convolution_theorem_explorer.py
```

On Windows with the Python launcher:

```bash
py convolution_theorem_explorer.py
```

The experiment:

* verifies a small known convolution result in the time and frequency domains
* calculates the required FFT length using `N_x + N_h - 1`
* applies zero-padding through the FFT length argument
* multiplies the input and filter spectra element by element
* reconstructs the filtered signal with the inverse FFT
* generates a 2 Hz signal with 20 Hz interference at a 100 Hz sampling rate
* applies a five-sample moving-average filter
* compares direct convolution with FFT-based filtering
* measures their maximum absolute difference
* visualizes the input signal, both filtered outputs, and their numerical error

## Tests

Run the convolution tests from `applications/signal_visualizer`:

```bash
python -m pytest -v test_convolution.py
```

The test suite verifies:

* a manually calculated convolution result
* the commutative property of convolution
* the output-length formula

The expected result is:

```text
collected 3 items
test_convolution.py::test_manual_known_example PASSED
test_convolution.py::test_convolution_is_commutative PASSED
test_convolution.py::test_output_length PASSED
```

The final summary should report:

```text
3 passed
```

Run the Fourier Series Visualizer tests from `applications/signal_visualizer`:

```bash
python -m unittest -v test_fourier_series_visualizer.py
```

The test suite verifies:

* square-wave and sawtooth signal generation
* periodic wrapping of the sawtooth signal
* square-wave and sawtooth Fourier coefficients
* reconstruction of a known single-sine signal
* zero and nonzero RMSE cases
* known harmonic amplitude and phase
* unsupported signal types
* nonpositive harmonic counts
* incompatible signal and coefficient-array shapes

The final summary should report:

```text
Ran 15 tests

OK
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

* the 1 Hz component is only moderately attenuated and phase shifted
* the 20 Hz component is strongly attenuated and shifted close to -90°
* the output keeps both original frequencies because an LTI system changes their amplitudes and phases, not their frequencies

The impulse-response experiment visualizes:

```text
h1[n] = 2δ[n]
h2[n] = δ[n - 1]
h3[n] = δ[n] + 0.5δ[n - 1]
```

For the interactive convolution example with `x = [1, 2, 4, 7]` and `h = [1, -1]`:

```text
Manual convolution: [ 1.  1.  2.  3. -7.]
NumPy convolution: [ 1.  1.  2.  3. -7.]
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

The third manually calculated example is:

```text
x = [2, -1, 3]
h = [1, 2, -1]
y = [2, 3, -1, 7, -3]
```

For the Fourier-series experiment:

* `K = 1` produces a single sinusoidal approximation
* `K = 3` adds the third harmonic and improves the square-wave shape
* `K = 5` produces flatter regions and sharper transitions
* `K = 9` gives the closest displayed approximation to the ideal square wave
* every reconstruction keeps the fundamental period of `1 s`
* only odd harmonics are included
* oscillations near the discontinuities demonstrate the Gibbs phenomenon

For the orthogonality experiment:

```text
<sin(ω0t), cos(ω0t)> ≈ 0
<sin(ω0t), sin(2ω0t)> ≈ 0
<sin(ω0t), sin(ω0t)> ≈ 0.5
```

For the composite signal:

```text
x(t) = 3sin(ω0t) + 0.5cos(2ω0t)
```

The recovered coefficients are approximately:

```text
sin1 coefficient: 3.0
cos1 coefficient: 0.0
sin2 coefficient: 0.0
cos2 coefficient: 0.5
Reconstruction matches: True
```

For the Fourier-coefficient experiment:

```text
a0 ≈ 0
a_n ≈ 0
b_n ≈ 4/(nπ), n odd
b_n ≈ 0,      n even
```

The first coefficients are:

```text
b1 ≈ 1.2732395
b2 ≈ 0
b3 ≈ 0.4244131
b4 ≈ 0
b5 ≈ 0.2546477
```

All automatic checks should return:

```text
True
```

The symbolic and numerical sine coefficients should agree within an absolute tolerance of:

```text
1e-6
```

For the periodic sawtooth reconstruction, the measured RMSE values with 5000 normalized-time samples are:

```text
N = 1,  RMSE = 0.361476
N = 3,  RMSE = 0.239798
N = 5,  RMSE = 0.191667
N = 20, RMSE = 0.099401
```

The sawtooth experiment demonstrates that:

* every reconstruction uses all harmonics from `1` through `N`
* the coefficient sign alternates between consecutive harmonics
* larger `N` produces a more accurate linear slope and a smaller RMSE
* Gibbs oscillations become narrower near the discontinuities as `N` increases
* the relative Gibbs overshoot does not disappear completely
* exactly at a jump from `1` to `-1`, the Fourier series converges to `0`

For the sawtooth line-spectrum experiment, the first coefficients and amplitudes are:

```text
n = 1: b_n ≈ 0.636620,  A_n ≈ 0.636620, phase ≈ -90°
n = 2: b_n ≈ -0.318310, A_n ≈ 0.318310, phase ≈ 90°
n = 3: b_n ≈ 0.212207,  A_n ≈ 0.212207, phase ≈ -90°
n = 4: b_n ≈ -0.159155, A_n ≈ 0.159155, phase ≈ 90°
```

The line-spectrum experiment demonstrates that:

* odd symmetry eliminates all cosine coefficients
* both even and odd harmonics remain because the sawtooth does not have half-wave symmetry
* harmonic amplitudes decrease as `1/n`
* harmonic phases alternate between `-90°` and `90°`
* a periodic signal has discrete spectral lines at integer multiples of its fundamental frequency

For Fourier Series Visualizer v1 with five harmonics, the square-wave analysis should produce approximately:

```text
RMSE: 0.2578
Amplitudes: [1.2732, 0.0000, 0.4244, 0.0000, 0.2546]
Phases: [-90°, 0°, -90°, 0°, -90°]
```

Only odd square-wave harmonics are present. The reconstruction displays Gibbs oscillations near every discontinuity.

With five harmonics, the sawtooth analysis should produce approximately:

```text
RMSE: 0.1917
Amplitudes: [0.6366, 0.3183, 0.2122, 0.1592, 0.1273]
Phases: [-90°, 90°, -90°, 90°, -90°]
```

Both even and odd sawtooth harmonics are present, their amplitudes decrease as `1/n`, and their phases alternate between `-90°` and `90°`.

For the Fourier-series to Fourier-transform transition with `τ = 1 s`:

```text
X(f) = sinc(f)
X(0) = 1
```

The first zeros of the continuous spectrum occur at:

```text
f = ±1 Hz
```

The four visualized periods and their spectral-line spacings are:

```text
T = 2 s:  Δf = 0.5000 Hz
T = 4 s:  Δf = 0.2500 Hz
T = 8 s:  Δf = 0.1250 Hz
T = 16 s: Δf = 0.0625 Hz
```

The transition experiment demonstrates that:

* the harmonic frequencies are located at `f_k = k/T`
* increasing `T` reduces the line spacing `Δf`
* the unscaled Fourier-series coefficients decrease because they contain the factor `1/T`
* the scaled coefficients `T C_k` lie on the continuous Fourier-transform curve
* discrete spectral lines become increasingly dense as `T` grows
* in the limit `T → ∞`, the Fourier-series sum becomes the Fourier-transform integral
* the negative sinc lobes are valid because the signed spectrum `X(f)` is displayed rather than its magnitude `|X(f)|`

For the MATLAB and NumPy introductory signal example:

```text
f = 2 Hz
T = 0.5 s
time interval = 0 to 1 s
number of samples = 101
```

Both implementations produce the same sinusoidal signal with:

* amplitude `1`
* two complete periods over the displayed one-second interval
* maxima near `1`
* minima near `-1`
* identical physical interpretation despite different syntax

The MATLAB implementation uses one-based indexing, while the NumPy implementation uses zero-based indexing.

For the Python Fourier-transform property experiment:

```text
Linearity: True
Duality: True
```

The linearity test verifies:

```text
F{2x1(t) - 3x2(t)} ≈ 2X1(f) - 3X2(f)
```

The duality test uses:

```text
x(t) = exp(-π(t - 1)²)
```

and verifies that applying the Fourier transform twice produces:

```text
x(-t) = exp(-π(t + 1)²)
```

For the MATLAB Fourier-transform property experiment, the measured maximum errors are:

```text
linearity_error = 3.7470e-15
duality_error = 6.6615e-16
```

These values are effectively zero at numerical precision and confirm the theoretical linearity and duality properties.

For the Fourier shift, scaling, and modulation experiment, the measured numerical errors are:

```text
Magnitude error: 2.731148640577885e-14
Shift property error: 2.7531964119108606e-14
Scale error: 1.1443916996305594e-16
Modulation error: 4.47545209131181e-16
Cosine modulation error: 2.227212004505268e-16
```

These values are effectively zero at numerical precision.

The time-shift experiment demonstrates that:

* shifting the Gaussian from `t = 0` to `t = 2 s` does not change the magnitude spectrum
* the complete complex spectrum changes because the shift introduces a frequency-dependent phase factor
* the predicted phase factor is `exp(-j4πf)`

The time-scaling experiment demonstrates that:

* `x(2t)` is narrower than `x(t)` in the time domain
* its frequency spectrum is wider than the original spectrum
* the spectral amplitude is multiplied by `1/2`
* compression in one domain produces expansion in the other

The complex modulation experiment demonstrates that:

* multiplying by `exp(j2πf0t)` translates the spectrum
* for `f0 = 2 Hz`, the Gaussian spectrum moves from `0 Hz` to `2 Hz`
* the spectral shape is preserved

The cosine-modulation experiment demonstrates that:

* multiplication by a real cosine creates two shifted spectral copies
* for `f0 = 2 Hz`, the copies are centered at `-2 Hz` and `2 Hz`
* each separated copy has half the amplitude of the original spectrum
* the two copies arise from the positive- and negative-frequency complex exponentials in Euler's cosine identity

For the signal-energy and Parseval experiment:

```text
Time-domain energy: 0.7071067811865476
Frequency-domain energy: 0.7071067811865475
Parseval error: 1.1102230246251565e-16
```

The analytical Gaussian energy is:

```text
1 / sqrt(2) ≈ 0.7071067811865476
```

The experiment demonstrates that:

* squaring the signal magnitude prevents positive and negative signal values from canceling
* signal energy is the inner product of a signal with itself
* scaling a signal by a factor of `2` scales its energy by a factor of `4`
* the Gaussian has finite energy because it decays rapidly toward zero
* the energy calculated in the time domain matches the energy calculated from the Fourier-transform magnitude
* the measured Parseval error is at floating-point precision
* the Fourier transform changes the signal representation without changing its total energy

For the rectangular-pulse time-bandwidth explorers:

```text
τ = 0.25 s -> B = 4.0 Hz
τ = 0.50 s -> B = 2.0 Hz
τ = 1.00 s -> B = 1.0 Hz
τ = 2.00 s -> B = 0.5 Hz
```

For every case:

```text
B = 1/τ
τB = 1
main-lobe width = 2/τ
X(0) = τ
```

The first spectral nulls are:

```text
τ = 0.25 s -> f = ±4 Hz
τ = 0.50 s -> f = ±2 Hz
τ = 1.00 s -> f = ±1 Hz
τ = 2.00 s -> f = ±0.5 Hz
```

The time-bandwidth experiments demonstrate that:

* decreasing pulse width increases first-null bandwidth
* increasing pulse width decreases first-null bandwidth
* a pulse that is ten times shorter has ten times larger first-null bandwidth
* the central sinc peak equals the pulse width because `sinc(0) = 1`
* `X(0)` also equals the area of the rectangular pulse
* the total main-lobe width is twice the first-null bandwidth
* sinc side lobes continue beyond the first nulls
* a rectangular pulse therefore does not have a finite strict bandwidth
* the same physical relationship is reproduced independently in Python and MATLAB

For the convolution-theorem experiment with:

```text
x = [1, 2, 4, 7]
h = [1, -1]
N_FFT = 5
```

both methods produce:

```text
Time-domain result: [1, 1, 2, 3, -7]
Frequency-domain result: [1, 1, 2, 3, -7]
Maximum error: approximately 1e-15
```

For the moving-average filtering experiment:

```text
sample rate = 100 Hz
duration = 2 s
useful frequency = 2 Hz
interference frequency = 20 Hz
filter length = 5
input length = 200
filtered length = 204
required FFT length = 204
```

The time-domain and frequency-domain filtered outputs overlap visually. Their measured maximum difference is:

```text
Maximum filtering error: 5.551115123125783e-16
```

The experiment demonstrates that:

* FFT multiplication with correct zero-padding reproduces linear convolution
* insufficient FFT length would produce circular wrap-around
* a five-sample moving average strongly suppresses a 20 Hz component sampled at 100 Hz
* direct convolution and FFT-based filtering are numerically equivalent
* the remaining difference is caused only by floating-point rounding

## Learning Progress

This project contains practical work from lessons 14 through 37 and related practical explorations from the PolyMath curriculum:

* Complex exponentials
* Delay and phase shift
* LTI eigenfunctions
* Frequency response
* First-order low-pass response
* Decibels and Bode plots
* Low-pass slope measurement
* Filtering a composite signal
* First-order high-pass response
* Complementary low-pass and high-pass magnitude responses
* Unit impulses and impulse response
* Convolution intuition
* Manual discrete-time convolution
* Input-side construction using shifted and scaled impulse responses
* Output-side calculation of individual output samples
* Convolution commutativity and numerical verification
* Interactive Convolution Lab v1
* Automated convolution testing with pytest
* Fourier series intuition
* Fundamental frequency and harmonics
* Square-wave reconstruction using odd harmonics
* Gibbs phenomenon near discontinuities
* Inner products of signals
* Orthogonal and orthonormal basis functions
* Projection coefficients
* Signal reconstruction from orthogonal components
* Trigonometric Fourier coefficients
* DC, cosine, and sine coefficients
* Symmetry-based elimination of Fourier coefficients
* Symbolic integration with SymPy
* Numerical integration with NumPy
* Absolute-error comparison between both methods
* Automatic coefficient validation
* Periodic extension using normalized-time wrapping
* Sawtooth reconstruction using consecutive Fourier harmonics
* Alternating sine-coefficient signs
* Partial-sum comparison for 1, 3, 5, and 20 harmonics
* RMSE measurement of reconstruction quality
* Numerical verification that RMSE decreases with additional harmonics
* Fourier-series convergence to the midpoint at discontinuities
* Even, odd, and half-wave symmetry
* Discrete harmonic line spectra
* Harmonic amplitude and phase calculation
* Alternating sawtooth phase pattern
* Amplitude and phase spectrum visualization
* Separation of mathematical logic, visualization, and application control flow
* Reusable Fourier-analysis utility functions
* Integrated Fourier Series Visualizer v1
* Interactive signal-type and harmonic-count selection
* Automated testing with Python unittest
* Validation of numerical results and invalid inputs
* Fourier-transform intuition
* Continuous spectra of nonperiodic signals
* Rectangular-pulse sinc spectrum
* Relationship between pulse width and spectrum width
* Spectral-line spacing `Δf = 1/T`
* Relationship between `C_k`, `X(f_k)`, and `T C_k`
* Transition from discrete Fourier-series lines to a continuous Fourier-transform spectrum
* Interpretation of the Fourier-transform integral as the limit of Fourier-series sums
* MATLAB Command Window and script workflow
* MATLAB vectors and one-based indexing
* MATLAB row and column vectors
* MATLAB transpose operation
* Matrix and element-wise MATLAB operators
* MATLAB signal generation and plotting
* Comparison of MATLAB and NumPy syntax for the same sinusoidal signal
* Continuous-time Fourier-transform definition
* Inverse Fourier transform
* Frequency analysis as projection onto complex exponentials
* Fourier-transform linearity
* Fourier-transform duality
* Double Fourier transformation and signal reflection
* Numerical approximation of the Fourier-transform integral
* Gaussian test signals for transform-property verification
* Python verification of Fourier-transform linearity and duality
* MATLAB implementation of numerical Fourier transformation
* MATLAB `trapz` integration
* MATLAB verification of Fourier-transform linearity and duality
* Floating-point error interpretation in numerical transform verification
* Fourier-transform time-shift property
* Linear phase produced by a time delay
* Preservation of spectral magnitude under time shifting
* Reciprocal time and frequency scaling
* Time compression and spectral expansion
* Complex exponential modulation
* Frequency translation
* Real cosine modulation
* Positive- and negative-frequency spectral copies
* Numerical verification of shifting, scaling, and modulation properties
* Four signal-spectrum visual comparisons
* Signal-energy definition
* Energy as the squared norm of a signal
* Relationship between energy and inner products
* Energy scaling by the squared amplitude factor
* Parseval's theorem
* Time-domain and frequency-domain energy equivalence
* Numerical integration with SciPy `simpson`
* Analytical energy of a Gaussian signal
* Numerical Parseval verification
* Floating-point error interpretation in energy calculations
* Rectangular-pulse duration
* Sinc-shaped Fourier-transform spectra
* First spectral nulls
* First-null bandwidth
* Main-lobe and side-lobe interpretation
* Strictly band-limited versus non-band-limited signals
* Inverse pulse-width and bandwidth relationship
* First-null time-bandwidth product
* DC spectral value and pulse area
* Python parameter sweep over pulse width
* Python 4-by-2 time-bandwidth explorer
* MATLAB `linspace`
* MATLAB logical vectors
* MATLAB one-based indexing in a parameter sweep
* MATLAB `for` loops
* MATLAB `subplot`
* MATLAB `xline`
* MATLAB `sprintf`
* MATLAB `if` conditions
* MATLAB implementation of the time-bandwidth explorer
* Convolution theorem
* Equivalence of convolution and frequency-domain multiplication
* Fast Fourier transform and inverse fast Fourier transform
* Linear and circular convolution
* Circular wrap-around
* Zero-padding for linear convolution
* FFT-length calculation using `N_x + N_h - 1`
* Element-wise multiplication of spectra
* Moving-average filtering
* Suppression of periodic high-frequency interference
* Time-domain and frequency-domain filtering comparison
* Floating-point error in FFT-based convolution
* Three-panel convolution-theorem visualization
