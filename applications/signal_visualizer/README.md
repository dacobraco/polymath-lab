# Signal Visualizer

A collection of Python and MATLAB experiments for building intuition about signals, LTI systems, impulse response, convolution, the convolution theorem, FFT-based filtering, uniform sampling, the Nyquist-Shannon sampling theorem, boundary sampling cases, aliasing, apparent frequency, frequency ambiguity, continuous- and discrete-time signal representations, frequency response, Bode plots, first-order filtering, Fourier series, Fourier transforms, Fourier-transform properties, time shifting, time scaling, modulation, signal energy, Parseval's theorem, rectangular pulses, sinc spectra, time-bandwidth relationships, harmonic reconstruction, quantitative reconstruction error, signal symmetry, line spectra, and the transition from discrete to continuous spectra.

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

* Uniform sampling of a continuous-time signal
* Sampling frequency and sampling interval
* Sampling instants `t_n = nT_s`
* Relationship between `x(t)` and `x[n]`
* Physical sample time versus integer sample index
* Number of samples per signal period
* Dense numerical reference grids for continuous-time visualization

* Band-limited signals and maximum signal frequency
* Nyquist rate `2B`
* Nyquist frequency `f_s / 2`
* Safe, boundary, and unsafe sampling rates
* Practical sampling condition `f_s > 2B`
* Phase sensitivity at the exact Nyquist boundary
* Aliasing caused by undersampling
* Apparent alias frequency
* Frequency ambiguity between continuous-time signals
* Identical sample sequences produced by different cosine frequencies

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

* Generates a dense numerical reference representation of a continuous-time sinusoid
* Uniformly samples a 5 Hz signal at 40 Hz
* Calculates the sampling interval and number of samples per period
* Overlays sampled values on the continuous-time reference curve
* Displays the discrete sequence `x[n]` using integer sample indices
* Distinguishes the visualization reference rate from the physical sampling rate

* Compares a 5 Hz sinusoid sampled at 40, 12, 10, and 8 Hz
* Classifies sampling rates as safe, boundary, or unsafe
* Displays only measured sample points without implying values between them
* Demonstrates phase sensitivity when `f_s = 2f`
* Compares phase-zero and 90-degree boundary samples
* Compares dense reference cosines at 7 Hz and 3 Hz
* Samples both signals at 10 Hz
* Calculates the 5 Hz Nyquist frequency and the apparent 3 Hz alias
* Numerically verifies that both sampled sequences are equal
* Displays two different continuous-time signals with the same measured sample values

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
δ[n - n0] = 0, n ≠  n0
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

Uniform sampling interval:

```text
T_s = 1 / f_s
```

Sampling instants:

```text
t_n = nT_s
```

Discrete-time sequence obtained from a continuous-time signal:

```text
x[n] = x(t_n) = x(nT_s)
```

Number of samples per signal period:

```text
samples_per_period = f_s / f
```

For the sampling experiment:

```text
f = 5 Hz
f_s = 40 Hz
T_s = 0.025 s
samples_per_period = 8
```

Nyquist rate for a signal band-limited to `B`:
```text
f_N = 2B
```
Practical no-alias sampling condition:
```text
f_s > 2B
```
Nyquist frequency of a sampler:
```text
f_Nyquist = f_s / 2
```
At the exact boundary for a 5 Hz sine sampled at 10 Hz:
```text
x[n] = sin(2π * 5 * n / 10) = sin(πn) = 0
```
A 90-degree phase shift at the same sampling rate produces alternating samples:
```text
x[n] = 1, -1, 1, -1, ...
```

For the fixed aliasing example:
```text
f_true = 7 Hz
f_s = 10 Hz
f_Nyquist = f_s / 2 = 5 Hz
f_alias = |f_true - 1 * f_s| = 3 Hz
```
The alias-frequency calculation above is specific to the current `k = 1` example. At the sampling instants `t_n = n/f_s`:
```text
x_7[n] = cos(2π * 7n / 10)
x_3[n] = cos(2π * 3n / 10)
cos(2π * 7n / 10)
= cos(2πn - 2π * 3n / 10)
= cos(-2π * 3n / 10)
= cos(2π * 3n / 10)
```
The equality follows because adding or subtracting complete `2π` rotations does not change a cosine and because cosine is an even function.


Reconstruction of a uniformly sampled signal:
```text
T_s = 1 / f_s
t_n = nT_s
x[n] = x(t_n)
```
Zero-order hold keeps the previous sample value until the next sample arrives:
```text
x_hat_ZOH(t) = x[n], for nT_s <= t < (n + 1)T_s
```
Linear interpolation uses two adjacent samples and connects them with a straight line:
```text
alpha = (t - nT_s) / T_s
x_hat_linear(t) = (1 - alpha)x[n] + alpha x[n + 1]
```
Normalized sinc definition:
```text
sinc(u) = sin(pi u) / (pi u)
sinc(0) = 1
```
Ideal sinc reconstruction:
```text
x_hat_sinc(t) = sum_n x[n] sinc((t - nT_s) / T_s)
```
At the sampling instants, the centered sinc kernel equals one while the other shifted kernels equal zero. Ideal reconstruction assumes a band-limited signal, sampling above the Nyquist rate, and an infinite sequence of samples. A finite observation interval produces truncation and edge errors.
For the reconstruction experiment:
```text
signal frequency = 3 Hz
sampling frequency = 12 Hz
Nyquist rate = 6 Hz
sampling interval = 1/12 s
samples per period = 4
```
The measured reconstruction errors are:
```text
ZOH RMSE = 0.6019806900817339
Linear RMSE = 0.19878220567458754
Sinc RMSE = 0.06778145507145349
```
Therefore:
```text
Sinc RMSE < Linear RMSE < ZOH RMSE
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
* `sampling_explorer.py` - visualizes uniform sampling of a continuous-time sinusoid and distinguishes physical sample times from discrete sample indices

* `nyquist_sampling_explorer.py` - compares safe, boundary, and unsafe sampling rates and demonstrates phase sensitivity at the Nyquist boundary
* `aliasing_lab.py` - demonstrates how 7 Hz and 3 Hz cosines produce identical samples when sampled at 10 Hz
* `reconstruction_interpolation_lab.py` - compares zero-order hold, linear interpolation, and sinc reconstruction and reports their RMSE values
* `fourier_sampling_lab.py` - integrates sampling, aliasing, normalized FFT analysis, reconstruction, RMSE verification, and a 3-by-3 dashboard
* `test_fourier_sampling_lab.py` - tests classification, aliasing, FFT detection, sinc interpolation, and reconstruction error
* `fourier_sampling_validation.m` - independently validates the safe sampling experiment in MATLAB
* `rc_rl_system_models.py` - models first-order RC and RL circuits with symbolic ODE solutions, numerical verification, and response plots
* `first_order_numerical_solver.py` - solves a first-order RC initial-value problem with SciPy `solve_ivp`, compares numerical and analytical responses, measures solver error, and demonstrates the accuracy-cost tradeoff

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

Sampling explorer:

```bash
python sampling_explorer.py
```

On Windows with the Python launcher:

```bash
py sampling_explorer.py
```

The experiment:

* generates a dense reference representation of a 5 Hz sinusoid
* samples the signal uniformly at 40 Hz
* calculates the sampling interval and number of samples per period
* overlays the sampled values on the reference curve
* displays `x[n]` against integer sample indices
* distinguishes the visualization reference rate from the physical sampling rate

Nyquist sampling explorer:
```bash
python nyquist_sampling_explorer.py
```
On Windows with the Python launcher:
```bash
py nyquist_sampling_explorer.py
```
The experiment:
* generates a 5 Hz reference sinusoid
* compares sampling rates of 40, 12, 10, and 8 Hz
* classifies each case as safe, boundary, or unsafe
* reports samples per period and total sample count
* displays measured samples without connecting them
* demonstrates that phase-zero samples vanish at the exact 10 Hz boundary
* demonstrates alternating samples after a 90-degree phase shift

Aliasing lab:
```bash
python aliasing_lab.py
```
On Windows with the Python launcher:
```bash
py aliasing_lab.py
```
The experiment:
* generates dense reference cosines at 7 Hz and 3 Hz
* samples both signals at 10 Hz over the interval `[0, 1)`
* calculates a sampling interval of `0.1 s`
* calculates the 5 Hz Nyquist frequency
* calculates the apparent 3 Hz alias for the fixed `k = 1` example
* verifies the equality of both sampled sequences using `np.allclose`
* displays the true and apparent continuous-time signals in separate panels
* overlays the same measured samples on both continuous-time curves


Reconstruction and interpolation lab:
```bash
python reconstruction_interpolation_lab.py
```
On Windows with the Python launcher:
```bash
py reconstruction_interpolation_lab.py
```
The experiment:
* generates a dense reference representation of a 3 Hz sinusoid
* samples the signal at 12 Hz, giving four samples per period
* reconstructs the signal using zero-order hold
* reconstructs the signal using linear interpolation
* reconstructs the signal using a finite sinc sum
* verifies that sinc reconstruction passes through the known samples
* calculates RMSE for all three reconstruction methods
* demonstrates finite-window edge effects
* displays the original signal, samples, and all three reconstructions
* verifies that sinc reconstruction has the smallest RMSE

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

For the sampling experiment:

```text
Signal frequency: 5 Hz
Sampling frequency: 40 Hz
Sampling interval: 0.025 s
Reference points: 2000
Number of samples: 40
First sample index: 0
Last sample index: 39
Samples per period: 8.0
```

The experiment demonstrates that:

* a sampling frequency of 40 Hz produces 40 samples over the interval `[0, 1)`
* the last sample occurs at `0.975 s` because indexing starts at `n = 0`
* a 5 Hz sinusoid sampled at 40 Hz has eight samples per period
* increasing the reference rate changes only the visual smoothness of the reference curve
* the physical sampling rate determines the actual sample times and values
* `x(t)` is displayed against time, while `x[n]` is displayed against an integer index

For the Nyquist sampling experiment:
```text
Signal frequency: 5 Hz
Nyquist rate: 10 Hz
Sampling frequencies: [40, 12, 10, 8]
40 Hz: Safe, 8.0 samples per period, 40 total samples
12 Hz: Safe, 2.4 samples per period, 12 total samples
10 Hz: Boundary, 2.0 samples per period, 10 total samples
8 Hz: Unsafe, 1.6 samples per period, 8 total samples
Boundary samples with phase 0: approximately zero
Boundary samples with phase pi/2: [1, -1, 1, -1, ...]
```
The experiment demonstrates that:
* sampling above twice the maximum signal frequency is safe for an ideal band-limited signal
* the exact Nyquist boundary is phase-sensitive and fragile
* a phase-zero 5 Hz sine sampled at 10 Hz can produce only zero-valued samples
* changing only the phase by 90 degrees produces alternating positive and negative samples
* sampling below the Nyquist rate is unsafe and can create frequency ambiguity

For the aliasing experiment:
```text
True frequency: 7 Hz
Sampling frequency: 10 Hz
Nyquist frequency: 5.0 Hz
Alias frequency: 3 Hz
Number of samples: 10
Sample times: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
Matching: True
```
The experiment demonstrates that:
* the 7 Hz signal exceeds the 5 Hz Nyquist frequency of the sampler
* sampling the 7 Hz cosine at 10 Hz produces an apparent frequency of 3 Hz
* the 7 Hz and 3 Hz continuous-time curves are visibly different between sampling instants
* both curves have identical values at every measured sampling instant
* `np.allclose` confirms the equality of the two sampled sequences
* the samples alone cannot distinguish the true 7 Hz signal from its 3 Hz alias
* avoiding this ambiguity requires a valid band limit and a sufficiently high sampling frequency

## Learning Progress

This project contains practical work from lessons 14 through 40 and related practical explorations from the PolyMath curriculum:

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

* Uniform sampling of continuous-time signals
* Sampling frequency and sampling interval
* Sampling instants and integer sample indices
* Relationship between `x(t)` and `x[n]`
* Samples per signal period
* Dense reference visualization versus physical sampling
* Stem-plot representation of a discrete-time sequence
* Nyquist-Shannon sampling theorem
* Nyquist rate and Nyquist frequency
* Safe, boundary, and unsafe sampling cases
* Phase sensitivity at the Nyquist boundary
* Boundary sampling verification with phase 0 and phase pi/2
* Aliasing and apparent frequency
* Frequency ambiguity caused by undersampling
* Equality of discrete samples from different continuous-time cosine frequencies
* Numerical alias verification using `np.allclose`
* Two-panel visualization of a true signal and its apparent alias

## Fourier and Sampling Laboratory

`fourier_sampling_lab.py` integrates continuous-time signal generation, uniform sampling, Nyquist classification, alias-frequency calculation, FFT analysis, reconstruction, numerical verification, and visualization in one signal-processing workflow.

### Files

* `fourier_sampling_lab.py` - runs the complete Python laboratory and displays the 3-by-3 dashboard
* `test_fourier_sampling_lab.py` - verifies classification, aliasing, FFT detection, sinc interpolation, and RMSE behavior
* `fourier_sampling_validation.m` - independently validates the safe experiment in MATLAB

### Experiment cases

| Case | Original frequency | Sampling frequency | Nyquist frequency | Expected result |
| --- | ---: | ---: | ---: | --- |
| Safe | 3 Hz | 12 Hz | 6 Hz | FFT detects 3 Hz |
| Boundary | 5 Hz | 10 Hz | 5 Hz | Phase-zero sine produces no reliable detected frequency |
| Unsafe | 7 Hz | 10 Hz | 5 Hz | FFT detects the 3 Hz alias |

The unsafe experiment uses a phase of `pi / 2`, so the generated sine is equivalent to a cosine. The 7 Hz cosine and 3 Hz cosine produce identical samples at a 10 Hz sampling frequency.

### Signal chain

```text
continuous reference signal
-> uniform samples
-> sampling classification
-> alias calculation
-> normalized FFT spectrum
-> dominant-frequency detection
-> ZOH, linear, and sinc reconstruction
-> RMSE and known-result checks
```

### Sampling classification

```text
f0 < fs / 2  -> Safe
f0 = fs / 2  -> Boundary
f0 > fs / 2  -> Unsafe
```

The practical sampling condition is `fs > 2f0`. Equality is treated as a boundary because the measured sequence can depend completely on signal phase.

### Alias frequency

The program first wraps the original frequency into one sampling-frequency interval and then folds frequencies above `fs / 2` back into the observable range.

```text
wrapped = f0 mod fs

if wrapped > fs / 2:
    alias = fs - wrapped
else:
    alias = wrapped
```

For the unsafe experiment:

```text
f0 = 7 Hz
fs = 10 Hz
alias = |7 - 10| = 3 Hz
```

### FFT analysis

The real FFT calculates the nonnegative-frequency spectrum of the measured samples. The magnitude is normalized to produce a single-sided amplitude spectrum. A tolerance prevents floating-point noise from being reported as a real frequency in the boundary case.

Expected dominant frequencies:

```text
Safe: 3 Hz
Boundary: None
Unsafe: 3 Hz
```

### Reconstruction

The program compares three reconstruction methods:

* zero-order hold keeps each sample value until the next sample arrives
* linear interpolation connects adjacent samples with straight lines
* sinc interpolation sums shifted normalized sinc kernels

RMSE is calculated against the original dense reference signal:

```text
RMSE = sqrt(mean((reference - reconstruction)^2))
```

Expected results:

| Case | ZOH RMSE | Linear RMSE | Sinc RMSE |
| --- | ---: | ---: | ---: |
| Safe | 0.601981 | 0.198782 | 0.067781 |
| Boundary | 0.707107 | 0.707107 | 0.707107 |
| Unsafe | 1.102325 | 0.804434 | 0.982830 |

In the safe case, sinc reconstruction has the smallest error. In the boundary case, phase-zero samples are effectively all zero, so no method can recover the original sine. In the unsafe case, reconstruction follows the aliased information contained in the samples instead of recovering the original 7 Hz signal.

### Dashboard

The 3-by-3 dashboard shows:

* original signals and measured samples
* normalized sample spectra and detected frequencies
* ZOH, linear, and sinc reconstructions with RMSE values

### Known-result checks

The main program checks:

* safe, boundary, and unsafe classification
* expected alias frequencies
* FFT detection of 3 Hz in the safe case
* rejection of numerical noise in the boundary case
* FFT detection of the 3 Hz alias in the unsafe case
* `sinc RMSE < linear RMSE < ZOH RMSE` in the safe case
* sinc interpolation passing through every measured sample

Additional pytest coverage is provided by `test_fourier_sampling_lab.py`.

### Run the Python laboratory

From `applications/signal_visualizer`:

```bash
python fourier_sampling_lab.py
```

On Windows with the Python launcher:

```bash
py fourier_sampling_lab.py
```

### Run the tests

```bash
py -m pytest -q test_fourier_sampling_lab.py
```

### Run the MATLAB validation

Open and run:

```text
fourier_sampling_validation.m
```

The MATLAB script independently verifies the safe 3 Hz signal sampled at 12 Hz, its normalized spectrum, dominant frequency, three reconstructions, and RMSE values.

## Differential Equations as System Models
`rc_rl_system_models.py` models first-order RC and RL circuits using symbolic differential equations, analytical solutions, numerical parameter substitution, automatic verification, and response plots.
The laboratory demonstrates that physically different systems can have the same normalized first-order dynamics.
### RC system
The RC differential equation is:
```text
R C dv_C(t) / dt + v_C(t) = V_in
```
For an initially uncharged capacitor and a constant input voltage:
```text
v_C(t) = V_in (1 - exp(-t / tau_RC))
tau_RC = R C
```
The laboratory uses:
```text
R = 10000 ohm
C = 100 microfarad
V_in = 5 V
tau_RC = 1 s
```
Selected results are:
```text
v_C(0 s) = 0 V
v_C(1 s) = 3.160603 V
v_C(2 s) = 4.323324 V
v_C(5 s) = 4.966310 V
```
The capacitor voltage is the RC state variable. It represents stored electrical energy and contains information about the previous behavior of the circuit.
### RL system
The RL differential equation is:
```text
L di(t) / dt + R i(t) = V_in
```
For zero initial current and a constant input voltage:
```text
i(t) = (V_in / R) (1 - exp(-t / tau_RL))
tau_RL = L / R
```
The laboratory uses:
```text
R = 10 ohm
L = 0.5 H
V_in = 10 V
tau_RL = 0.05 s
I_final = 1 A
```
Selected results are:
```text
i(0 s) = 0 A
i(0.05 s) = 0.632121 A
i(0.10 s) = 0.864665 A
i(0.25 s) = 0.993262 A
```
The inductor current is the RL state variable. It represents stored magnetic energy and cannot change instantaneously in the ideal model.
### State and memory
A state variable is the minimum internal information required, together with the future input, to determine the future behavior of a system.
```text
RC state: capacitor voltage v_C(t)
RL state: inductor current i(t)
```
Initial conditions represent system memory. Identical circuits receiving the same future input can respond differently if they begin with different capacitor voltages or inductor currents.
An ideal resistor stores no energy and therefore does not independently introduce a state variable.
### Symbolic workflow
SymPy is used to:
- create symbolic parameters with `symbols`
- represent time-dependent unknowns with `Function`
- calculate symbolic derivatives with `diff`
- construct equations with `Eq`
- solve differential equations with `dsolve`
- apply initial conditions with `ics`
- substitute numerical values with `subs`
- verify solutions with `simplify`
- create NumPy-compatible functions with `lambdify`
The analytical solutions are substituted back into their original differential equations.
```text
RC equation residual: 0
RL equation residual: 0
```
A zero symbolic residual confirms that the analytical expression satisfies the corresponding equation exactly.
### Normalized first-order response
The responses are normalized using:
```text
normalized time = t / tau
normalized output = output / final output
```
Both RC and RL systems then follow:
```text
normalized output = 1 - exp(-normalized time)
```
Their normalized curves overlap even though their physical quantities, final values, and time constants differ.
This demonstrates that the same mathematical model can describe different physical systems.
### Automatic checks
The program verifies:
- zero symbolic residuals for both differential equations
- the RC time constant of 1 second
- the RL time constant of 0.05 second
- zero initial voltage and current
- equal normalized time axes
- equal normalized RC and RL responses
Successful execution prints:
```text
All RC/RL model checks passed.
```
### Visualizations
The program creates:
1. an RC step response showing capacitor voltage approaching 5 V
2. an RL step response showing inductor current approaching 1 A
3. a normalized comparison showing identical first-order response shapes
### Run
From the repository root:
```powershell
py applications/signal_visualizer/rc_rl_system_models.py
```

## Numerical Solution of a First-Order System
`first_order_numerical_solver.py` solves the transient response of a first-order RC system numerically with SciPy `solve_ivp` and compares the result with the known analytical solution.
The laboratory demonstrates how a differential equation can be used directly by a numerical solver without providing the closed-form solution.
### First-order RC model
The system is described by:
```text
dv(t) / dt = (V_in - v(t)) / tau
```
The laboratory uses:
```text
V_in = 5 V
tau = 1 s
v(0) = 0 V
```
The derivative function supplied to `solve_ivp` is therefore:
```text
dv / dt = (5 - v) / 1
```
At the beginning:
```text
v = 0 V
dv / dt = 5 V/s
```
When the capacitor voltage reaches 4 V:
```text
v = 4 V
dv / dt = 1 V/s
```
The rate of change decreases as the capacitor voltage approaches the final value of 5 V.
### Numerical solution
SciPy `solve_ivp` solves the initial-value problem from 0 to 5 seconds.
Selected numerical results with the default solver settings are:
```text
t = 0 s: 0.000000 V
t = 1 s: 3.161055 V
t = 2 s: 4.323786 V
t = 5 s: 4.965707 V
```
The analytical step response is:
```text
v(t) = V_in (1 - exp(-t / tau))
```
For the same times:
```text
t = 0 s: 0.000000 V
t = 1 s: 3.160603 V
t = 2 s: 4.323324 V
t = 5 s: 4.966310 V
```
The maximum absolute error with the default solver settings is approximately:
```text
6.03e-4 V
```
### Solver tolerances
The experiment is repeated with stricter numerical tolerances:
```text
rtol = 1e-9
atol = 1e-12
```
The maximum absolute error decreases to approximately:
```text
8.82e-10 V
```
This higher accuracy requires more evaluations of the differential-equation function:
```text
Default solver evaluations: 56
Strict solver evaluations: 386
```
This demonstrates an important numerical-computation tradeoff:
```text
higher accuracy -> more computation
```
### Evaluation times and internal solver steps
`t_eval` specifies the times at which results should be returned.
For example:
```text
t_eval = [0, 1, 2, 5]
```
does not mean that the numerical solver takes only four integration steps.
`solve_ivp` internally chooses its own adaptive step sizes while integrating the differential equation. The requested evaluation times only specify where the final solution should be reported.
### Dense-grid verification
The strict numerical solution is also evaluated at 501 points between 0 and 5 seconds.
The numerical and analytical curves are compared over the complete interval.
The maximum dense-grid error is approximately:
```text
9.44e-10 V
```
The program automatically verifies:
```text
solver success
maximum error < 1e-8 V
```
Successful execution prints:
```text
Dense-grid checks passed.
```
### Main numerical workflow
The laboratory follows this workflow:
```text
differential equation
        |
        v
derivative function
        |
        v
solve_ivp
        |
        v
numerical transient response
        |
        v
analytical reference
        |
        v
error calculation and automatic verification
```
The important idea is that the numerical solver does not need the analytical expression for the solution.
It only needs:
```text
1. the differential equation
2. the initial condition
3. the integration interval
```
This makes numerical ODE solvers useful for systems whose analytical solutions are difficult or impossible to obtain in closed form.
### Visualizations
The program creates two plots:
1. analytical and numerical capacitor-voltage responses
2. absolute numerical error over time
With strict tolerances, the analytical and numerical response curves visually overlap.
### Run
From the repository root:
```powershell
py applications/signal_visualizer/first_order_numerical_solver.py
```
## Second-Order Systems, Damping, and Resonance
`second_order_response.py` models a normalized second-order system directly from its differential equation and solves its step response numerically with SciPy `solve_ivp`.
The laboratory compares undamped, underdamped, critically damped, and overdamped responses. It also demonstrates how damping controls overshoot, settling time, and resonance.
`second_order_response_validation.m` independently verifies the main numerical results with MATLAB `ode45`.
### Second-order differential equation
The normalized second-order system is described by:
```text
y''(t) + 2 zeta omega_n y'(t) + omega_n^2 y(t)
= omega_n^2 u(t)
```
where:
```text
y(t) = system output
y'(t) = output rate
y''(t) = output acceleration
u(t) = input
omega_n = natural angular frequency
zeta = damping ratio
```
The laboratory uses:
```text
omega_n = 5 rad/s
u(t) = 1
y(0) = 0
y'(0) = 0
```
A second-order system requires two initial-state values because the same output can develop differently depending on its current rate of change.
### First-order state representation
SciPy `solve_ivp` solves systems of first-order differential equations.
The second-order equation is therefore rewritten using:
```text
y1 = y
y2 = y'
```
The two first-order equations are:
```text
y1' = y2
y2' = omega_n^2 (u - y1) - 2 zeta omega_n y2
```
The solver state is:
```text
state = [output, output rate]
```
The derivative function returns:
```text
[output rate, output acceleration]
```
This extends the first-order workflow from Lesson 44 from one state variable to two state variables.
### Meaning of the acceleration equation
The isolated acceleration is:
```text
y'' = omega_n^2 (u - y) - 2 zeta omega_n y'
```
The term:
```text
omega_n^2 (u - y)
```
moves the output toward the target.
The term:
```text
-2 zeta omega_n y'
```
opposes the current motion and removes energy from the response.
For `omega_n = 5 rad/s` and `zeta = 0.2`:
```text
y'' = 25(1 - y) - 2y'
```
Selected derivative values are:
```text
y = 0.0, y' = 0.0  ->  y'' = 25.0
y = 1.0, y' = 0.0  ->  y'' = 0.0
y = 1.2, y' = 0.0  ->  y'' = -5.0
y = 1.0, y' = 2.0  ->  y'' = -4.0
```
At the target with zero rate, the system is in equilibrium. If the system reaches the target with a positive rate, it continues moving past the target before damping slows it down. This produces overshoot.
### Damping cases
The program compares:
```text
zeta = 0.0
zeta = 0.2
zeta = 1.0
zeta = 2.0
```
Their behaviors are:
| Damping ratio | Classification | Behavior |
| ---: | --- | --- |
| 0.0 | Undamped | Permanent oscillations |
| 0.2 | Underdamped | Decaying oscillations and overshoot |
| 1.0 | Critically damped | Fastest response without overshoot |
| 2.0 | Overdamped | Slow response without oscillations |
The undamped system does not lose energy, so it never settles.
The underdamped system exchanges stored energy while damping gradually reduces the oscillations.
The critically damped system reaches the target as quickly as possible without oscillating.
The overdamped system does not oscillate, but excessive damping makes it slower than the critically damped system.
### Step-response results
The numerical step-response results are:
| Damping ratio | Peak output | Overshoot | Settling time |
| ---: | ---: | ---: | ---: |
| 0.0 | approximately 2.000000 | approximately 100% | Does not settle |
| 0.2 | 1.526610 | 52.660989% | 3.925 s |
| 1.0 | approximately 1.000000 | 0% | 1.170 s |
| 2.0 | approaches 1.000000 | 0% | 2.980 s |
Settling time is defined using a 2% tolerance:
```text
0.98 <= y(t) <= 1.02
```
The response is considered settled when it enters this interval and does not leave it again.
### Overshoot
For an underdamped second-order system, the theoretical percentage overshoot is:
```text
M_p = exp(-zeta pi / sqrt(1 - zeta^2)) * 100%
```
For `zeta = 0.2`:
```text
Python numerical overshoot = 52.660989042%
MATLAB numerical overshoot = 52.660989052%
Theoretical overshoot = 52.662059933%
```
The MATLAB numerical and theoretical difference is:
```text
0.001070881%
```
The close agreement verifies the numerical step response.
### Peak time
For an underdamped system, the damped angular frequency is:
```text
omega_d = omega_n sqrt(1 - zeta^2)
```
The first peak time is:
```text
t_p = pi / omega_d
```
For `omega_n = 5 rad/s` and `zeta = 0.2`:
```text
t_p is approximately 0.64 s
```
For the undamped case, repeated peaks have the same theoretical height. The program reports the first peak at:
```text
t_p = pi / omega_n
t_p is approximately 0.628319 s
```
### Resonance
Resonance occurs when a sinusoidal input frequency is close to the natural frequency and the output amplitude becomes larger than the input amplitude.
The normalized frequency ratio is:
```text
r = omega / omega_n
```
The steady-state magnitude is calculated using:
```text
M(r) = 1 / sqrt((1 - r^2)^2 + (2 zeta r)^2)
```
A pronounced resonance peak exists when:
```text
zeta < 1 / sqrt(2)
```
For `zeta = 0.2`, the numerical results are:
```text
Python resonance frequency = 4.802367694 rad/s
MATLAB resonance frequency = 4.802367694 rad/s
Theoretical resonance frequency = 4.795831523 rad/s
Maximum magnitude = 2.551499514
```
A magnitude of approximately `2.55` means that a sinusoidal input with amplitude `1` produces a steady-state output amplitude of approximately `2.55` near resonance.
Systems with `zeta = 1.0` and `zeta = 2.0` do not have pronounced resonance peaks.
The small difference between the numerical and theoretical resonance frequencies is caused by the finite frequency grid used by the programs.
### Python workflow
The Python program:
1. defines the second-order differential equation
2. converts it into two first-order state equations
3. solves the equations with `solve_ivp`
4. compares four damping ratios
5. calculates peak output, overshoot, and settling time
6. evaluates resonance magnitude over a frequency grid
7. verifies known numerical results
8. displays step-response and resonance plots
### MATLAB validation
MATLAB `ode45` independently solves the same second-order initial-value problems.
The validation checks:
* numerical and theoretical overshoot
* numerical and theoretical resonance frequency
* agreement within defined error tolerances
* equivalent step-response and resonance plots
Successful execution prints:
```text
MATLAB checks passed.
```
The MATLAB script saves:
```text
second_order_response_validation.png
```
### Visualizations
The programs create:
1. step responses for four damping ratios
2. resonance magnitude for three damping ratios
3. a marked natural-frequency ratio
The plots demonstrate:
```text
less damping -> more oscillation, overshoot, and resonance
critical damping -> fastest response without overshoot
excessive damping -> slower response
```
### Files
```text
second_order_response.py
second_order_response_validation.m
second_order_response_validation.png
```
### Run the Python laboratory
From the repository root:
```powershell
py applications/signal_visualizer/second_order_response.py
```
### Run the MATLAB validation
From the repository root:
```powershell
matlab -batch "run('applications/signal_visualizer/second_order_response_validation.m')"
```

## Laplace Transform Intuition
`laplace_intuition.py` introduces the Laplace transform as a method for converting differential equations in the time domain into algebraic equations in the s-domain.
The laboratory connects known time-domain signals with their Laplace transforms, demonstrates how initial conditions enter transformed derivatives, derives first- and second-order transfer functions, and connects the second-order model with the system from Lesson 45.
### Time domain and s-domain
A time-domain signal is written as:
```text
x(t)
```
Its Laplace transform is written as:
```text
X(s) = L{x(t)}
```
The transformation creates the mapping:
```text
time domain                 s-domain
x(t)                        X(s)
y(t)                        Y(s)
u(t)                        U(s)
differential equation       algebraic equation
```
The complete function `x(t)` is transformed into a new function `X(s)`. Time itself is not directly replaced by `s`.
### Complex Laplace variable
The Laplace variable is:
```text
s = sigma + j omega
```
The real part `sigma` describes exponential growth or decay.
The imaginary part `omega` describes oscillation.
Since:
```text
exp(-s t) = exp(-sigma t) exp(-j omega t)
```
the Laplace transform can analyze growth, decay, and oscillation together.
The Fourier transform is obtained along the special line:
```text
sigma = 0
s = j omega
```
The Laplace transform can therefore be understood as an extension of the Fourier transform.
### Definition
For causal signals considered from `t = 0`, the one-sided Laplace transform is:
```text
X(s) = integral from 0 to infinity of x(t) exp(-s t) dt
```
The transform exists only in the region where the integral converges.
### Basic transform pairs
The program verifies:
```text
1              ->  1 / s
exp(-2t)       ->  1 / (s + 2)
sin(3t)        ->  3 / (s^2 + 9)
```
The general exponential and sinusoidal pairs are:
```text
exp(-a t)      ->  1 / (s + a)
sin(omega t)   ->  omega / (s^2 + omega^2)
```
### Transform conditions
By default, SymPy `laplace_transform` returns:
```text
(transform, convergence boundary, additional condition)
```
For example:
```text
L{exp(-2t)} = (1 / (s + 2), -2, True)
```
The convergence boundary `-2` means:
```text
Re(s) > -2
```
The option:
```python
noconds=True
```
returns only the transformed expression and omits the convergence information and additional conditions.
### Derivatives and initial conditions
The Laplace transform converts derivatives into algebraic expressions:
```text
L{y'(t)} = sY(s) - y(0)
```
For the second derivative:
```text
L{y''(t)} = s^2 Y(s) - s y(0) - y'(0)
```
With zero initial conditions:
```text
y(0) = 0
y'(0) = 0
```
these expressions become:
```text
L{y'(t)} = sY(s)
L{y''(t)} = s^2 Y(s)
```
This explains why a second-order system requires both an initial output and an initial output rate.
### First-order system
The time-domain equation:
```text
y'(t) + 2y(t) = u(t)
```
with:
```text
y(0) = 0
```
becomes:
```text
sY(s) + 2Y(s) = U(s)
```
Factoring and solving for the output gives:
```text
Y(s)(s + 2) = U(s)
Y(s) = U(s) / (s + 2)
```
The transfer function is therefore:
```text
H(s) = Y(s) / U(s)
H(s) = 1 / (s + 2)
```
### Purpose of a transfer function
A transfer function describes how a system converts an input into an output:
```text
Y(s) = H(s) U(s)
```
where:
```text
U(s) = input
H(s) = system
Y(s) = output
```
The same transfer function can be used with different inputs. The system remains unchanged while `U(s)` changes.
Transfer functions are defined using zero initial conditions so that they describe only the input-output behavior of the system.
Nonzero initial conditions introduce an additional response caused by previously stored energy.
### DC gain
For very slow or constant inputs, the transfer function is evaluated at:
```text
s = 0
```
For:
```text
H(s) = 1 / (s + 2)
```
the DC gain is:
```text
H(0) = 1 / 2
```
A constant input with amplitude `1` therefore produces a final output of `0.5`.
### Frequency response
The frequency response is obtained by evaluating the transfer function along:
```text
s = j omega
```
Therefore:
```text
H(s)  ->  H(j omega)
```
The frequency response describes how the system changes the amplitude and phase of sinusoidal inputs.
### Second-order system
The second-order equation from Lesson 45 is:
```text
y'' + 2 zeta omega_n y' + omega_n^2 y
= omega_n^2 u
```
With zero initial conditions, its Laplace-domain equation is:
```text
s^2 Y + 2 zeta omega_n sY + omega_n^2 Y
= omega_n^2 U
```
Factoring `Y(s)` gives:
```text
Y(s)(s^2 + 2 zeta omega_n s + omega_n^2)
= omega_n^2 U(s)
```
The second-order transfer function is:
```text
H(s) = omega_n^2 / (s^2 + 2 zeta omega_n s + omega_n^2)
```
### Connection with Lesson 45
For:
```text
omega_n = 5 rad/s
zeta = 0.2
```
the transfer function becomes:
```text
H(s) = 25 / (s^2 + 2s + 25)
```
Its DC gain is:
```text
H(0) = 1
```
This means that a constant input is passed without changing its final value.
For a unit-step input:
```text
U(s) = 1 / s
```
the output is:
```text
Y(s) = H(s) U(s)
Y(s) = 25 / (s(s^2 + 2s + 25))
```
The inverse Laplace transform of this expression produces the time-domain step response. Inverse transformation is introduced in Lesson 48.
### SymPy workflow
The program uses SymPy to:
* create time-domain and Laplace-domain symbols
* calculate transforms with `laplace_transform`
* omit transform conditions with `noconds=True`
* construct Laplace-domain equations with `Eq`
* solve equations for `Y` with `solve`
* form transfer functions using `Y / U`
* substitute concrete system parameters with `subs`
* simplify symbolic expressions with `simplify`
* verify known transform pairs and transfer functions
### Automatic checks
The program verifies:
* the transform of a unit step
* the transform of `exp(-2t)`
* the transform of `sin(3t)`
* the first-order transfer function
* the general second-order transfer function
* the concrete DC gain
* the unit-step output relation
Successful execution prints:
```text
All Laplace intuition checks passed.
```
### Main workflow
```text
time-domain signal or equation
-> Laplace transformation
-> algebraic s-domain equation
-> solve for Y(s)
-> divide by U(s)
-> transfer function H(s)
-> multiply by a selected input U(s)
-> output Y(s)
```
### File
```text
laplace_intuition.py
```
### Run
From the repository root:
```powershell
py applications/signal_visualizer/laplace_intuition.py
```

## Poles, Zeros, and Stability
`pole_zero_explorer.py` connects transfer-function coefficients, pole and zero locations, stability classification, and time-domain behavior.
The experiment demonstrates how a small number of points in the complex s-plane can predict whether a system response decays, remains constant, or grows.
### Transfer-function form
A transfer function can be written as:
```text
H(s) = K (s - z1)(s - z2)... / ((s - p1)(s - p2)...)
```
where:
```text
zk = zeros
pk = poles
K  = overall gain
```
Zeros are the values of `s` that make the numerator equal to zero.
Poles are the values of `s` that make the denominator equal to zero.
The program calculates polynomial roots using:
```python
np.roots(coefficients)
```
For example:
```text
denominator coefficients: [1, 4]
polynomial: s + 4
pole: -4
```
A constant numerator such as `[3]` has no finite zeros.
### Stability rule
For a continuous-time linear system, pole locations determine stability:
```text
All pole real parts < 0       Stable
Pole real part = 0            Marginally stable
Any pole real part > 0        Unstable
```
Poles in the left half-plane produce responses that decay.
Poles on the imaginary axis produce oscillations whose amplitudes do not naturally decay.
Poles in the right half-plane produce responses whose amplitudes grow.
A numerical tolerance is used when comparing real parts with zero:
```text
tolerance = 1e-9
```
This prevents tiny floating-point errors from incorrectly changing the stability classification.
### Studied systems
The first-order system:
```text
H(s) = 3 / (s + 4)
```
has:
```text
pole: -4
zeros: none
classification: Stable
```
The high-pass system:
```text
H(s) = s / (s + 2)
```
has:
```text
pole: -2
zero: 0
classification: Stable
```
The stable oscillatory system:
```text
H(s) = 25 / (s^2 + 2s + 25)
```
has:
```text
poles: -1 + j4.89897949 and -1 - j4.89897949
classification: Stable
```
The marginally stable oscillator:
```text
H(s) = 1 / (s^2 + 9)
```
has:
```text
poles: 0 + j3 and 0 - j3
classification: Marginally stable
```
The unstable oscillator:
```text
H(s) = 1 / (s^2 - s + 9.25)
```
has:
```text
poles: 0.5 + j3 and 0.5 - j3
classification: Unstable
```
### Pole-zero map
The program displays poles and zeros in the complex s-plane.
The plotting convention is:
```text
red x          pole
blue circle    zero
horizontal     real axis
vertical       imaginary axis
green region   stable left half-plane
red region     unstable right half-plane
```
A zero can lie on the imaginary axis without making the system unstable.
Stability is determined by poles, while zeros shape how input components are transferred to the output.
### Connection with the time response
A complex-conjugate pole pair:
```text
p = sigma + j omega
p* = sigma - j omega
```
produces a real response with the general form:
```text
x(t) = exp(sigma t) cos(omega t)
```
The real part controls the amplitude envelope:
```text
sigma < 0      amplitude decreases
sigma = 0      amplitude remains constant
sigma > 0      amplitude increases
```
The imaginary part controls the oscillation rate.
For poles:
```text
-0.5 + j3 and -0.5 - j3
```
the amplitude envelope is:
```text
exp(-0.5t)
```
and the time constant is:
```text
tau = 1 / 0.5 = 2 s
```
The oscillation period is:
```text
T = 2 pi / 3
T approximately 2.09 s
```
For poles:
```text
0.5 + j3 and 0.5 - j3
```
the envelope is:
```text
exp(0.5t)
```
At `t = 6 s`, its value is:
```text
exp(3) approximately 20.09
```
This explains the growing unstable response shown by the program.
### Effect of a zero at the origin
The high-pass transfer function is:
```text
H_HP(s) = s / (s + 2)
```
Its value at zero frequency is:
```text
H_HP(0) = 0
```
The zero at `s = 0` therefore blocks a constant, or DC, component.
For a unit-step input, the high-pass output is:
```text
y_HP(t) = exp(-2t)
```
The output initially reacts to the sudden input change and then decreases to zero.
For comparison, the low-pass system is:
```text
H_LP(s) = 2 / (s + 2)
```
Its unit-step response is:
```text
y_LP(t) = 1 - exp(-2t)
```
The two responses are complementary:
```text
y_HP(t) + y_LP(t) = 1
```
The common pole at `-2` gives the time constant:
```text
tau = 1 / 2 = 0.5 s
```
After one time constant:
```text
y_HP(0.5) approximately 0.368
y_LP(0.5) approximately 0.632
```
### Engineering interpretation
Pole-zero analysis makes it possible to predict system behavior without first calculating every point of the time response.
It can be used to:
* determine whether a control system is stable
* predict whether a circuit response will decay or grow
* recognize oscillatory system behavior
* estimate settling speed from pole real parts
* estimate oscillation speed from pole imaginary parts
* understand why a high-pass filter removes DC offset
* connect transfer functions with time-domain behavior
The high-pass example is relevant to biomedical signal processing because a zero at the origin can help remove slowly varying baseline components from signals such as ECG measurements.
### Main conclusions
```text
Poles determine natural system behavior.
Pole real parts determine growth or decay.
Pole imaginary parts determine oscillation.
Zeros suppress selected input components.
A zero at the origin blocks DC.
Stable poles must lie in the left half-plane.
```
### File
```text
pole_zero_explorer.py
```
### Run
From the repository root:
```powershell
py applications/signal_visualizer/pole_zero_explorer.py
```


## Inverse Laplace Transform
inverse_laplace_response.py connects transfer functions in the s-domain with impulse and step responses in the time domain.
The experiment uses symbolic inverse Laplace transforms to recover system behavior directly from H(s).
### Impulse and step responses
For a transfer function:
    H(s) = Y(s) / X(s)
the impulse response is:
    h(t) = L^-1{H(s)}
because:
    L{delta(t)} = 1
For a unit-step input:
    L{u(t)} = 1 / s
so:
    Y_step(s) = H(s) / s
and:
    y_step(t) = L^-1{H(s) / s}
### First-order system
The first system is:
    H(s) = 2 / (s + 2)
Its impulse response is:
    h(t) = 2 exp(-2t)
Its step response is:
    y(t) = 1 - exp(-2t)
The impulse response decays to zero.
The step response approaches:
    H(0) = 1
which is the DC gain.
### Second-order system
The second system is:
    H(s) = 9 / (s^2 + 2s + 10)
The denominator can be written as:
    (s + 1)^2 + 9
so the poles are:
    -1 + j3
    -1 - j3
The impulse response is:
    h(t) = 3 exp(-t) sin(3t)
The pole real part produces exponential decay:
    real part -1 -> exponential decay
The pole imaginary part produces oscillation:
    imaginary part 3 -> oscillation
The step response is:
    y(t) = 9/10 - (3/10) exp(-t) sin(3t) - (9/10) exp(-t) cos(3t)
The transient oscillations decay because the poles lie in the left half-plane.
The final step-response value is:
    y(infinity) = 9/10
which matches:
    H(0) = 9/10
### Symbolic verification
SymPy calculates the inverse Laplace transforms and verifies that the results match the expected analytical expressions.
The program verifies:
    first-order impulse at t = 0 = 2
    first-order step at t = 0 = 0
    second-order impulse at t = 0 = 0
    second-order step at t = 0 = 0
For both stable systems:
    impulse response -> 0
as:
    t -> infinity
The final values of the step responses are also verified against the corresponding DC gains.
### Visualization
The program plots:
    first-order impulse response
    first-order step response
    second-order impulse response
    second-order step response
The first-order system shows exponential behavior.
The second-order system shows damped oscillations caused by its complex-conjugate poles.
The step-response plots include the DC gain as a reference line.
### Connection with previous lessons
The experiment connects:
    differential equation
            |
            v
    transfer function H(s)
            |
            v
    poles and zeros
            |
            v
    inverse Laplace transform
            |
            v
    time-domain response
Pole-zero analysis predicts the qualitative behavior.
The inverse Laplace transform produces the exact time-domain response.
### Engineering interpretation
Inverse Laplace transforms convert algebraic system models in the s-domain back into measurable time-domain behavior.
Applications include:
* circuit transient analysis
* control-system response analysis
* filter behavior
* stability interpretation
* impulse-response calculation
* step-response calculation
* connecting mathematical models with physical systems
### File
    inverse_laplace_response.py
### Run
From the repository root:
    py applications/signal_visualizer/inverse_laplace_response.py


## Transfer Functions in Software
transfer_function_software.py and transfer_function_software_validation.m demonstrate how the same continuous-time transfer function is represented and analyzed in SciPy Signal and MATLAB.
The studied system is:
    H(s) = 9 / (s^2 + 2s + 10)
The numerator and denominator coefficients are:
    numerator = [9]
    denominator = [1, 2, 10]
The coefficients are written from the highest polynomial power to the lowest.
### SciPy representation
SciPy represents the system with:
    signal.TransferFunction(numerator, denominator)
This creates a continuous-time LTI system object.
The system object can then be used to calculate:
* poles
* zeros
* step response
* impulse response
For the studied system, SciPy returns the poles:
    -1 + j3
    -1 - j3
and no finite zeros.
The complex-conjugate poles agree with the theoretical analysis from the previous lessons.
### Controlled time grid
The simulation uses the same time interval in both platforms:
    t = 0 to 8 s
    number of points = 801
    time step = 0.01 s
Using the same time grid makes the numerical comparison between SciPy and MATLAB meaningful.
### SciPy response values
Selected step-response values are approximately:
    t = 0 s    0.000000
    t = 1 s    1.212204
    t = 2 s    0.794394
    t = 8 s    0.899963
Selected impulse-response values are approximately:
    t = 0 s    0.000000
    t = 1 s    0.155745
    t = 2 s   -0.113444
    t = 8 s   -0.000911
The step response approaches the DC gain:
    H(0) = 0.9
The impulse response approaches zero.
### MATLAB representation
MATLAB represents the same system with:
    tf(numerator, denominator)
The corresponding MATLAB commands for system analysis are:
    pole
    zero
    step
    impulse
The MATLAB simulation uses the same transfer-function coefficients and the same time grid as SciPy.
The MATLAB results match the SciPy results for the tested response values and reproduce the same step and impulse-response shapes.
### Indexing difference
Python indexing starts at zero.
For the 0.01 s time grid:
    t = 0 s -> index 0
    t = 1 s -> index 100
    t = 2 s -> index 200
    t = 8 s -> index 800
MATLAB indexing starts at one:
    t = 0 s -> index 1
    t = 1 s -> index 101
    t = 2 s -> index 201
    t = 8 s -> index 801
The physical time values are identical. Only the array indexing convention differs.
### Main conclusion
SciPy and MATLAB use different software interfaces, but they represent the same mathematical system.
The workflow is:
    transfer-function coefficients
            |
            v
    software system object
            |
            +--> poles
            +--> zeros
            +--> step response
            +--> impulse response
For the same transfer function and the same simulation times, both platforms produce the same system behavior.
This demonstrates an important engineering idea:
    mathematical model stays the same
    software interface can change
### Engineering interpretation
Transfer-function objects allow system models to be analyzed without manually solving the differential equation every time.
This approach is useful for:
* control-system analysis
* circuit models
* analog filter models
* transient-response analysis
* stability analysis
* comparison between engineering software platforms
* later biomedical signal-processing and system-modeling work
### Files
    transfer_function_software.py
    transfer_function_software_validation.m
### Run Python
From the repository root:
    py applications/signal_visualizer/transfer_function_software.py
### Run MATLAB
From the repository root:
    matlab -batch "run('applications/signal_visualizer/transfer_function_software_validation.m')"


## Difference Equations and Discrete Systems
recursive_system_simulator.py demonstrates a first-order recursive discrete-time system described by the difference equation:
    y[n] = a * y[n - 1] + x[n]
Unlike a continuous-time differential equation, a difference equation describes the system sample by sample.
The current output depends on:
* the current input x[n]
* the previous output y[n - 1]
* the recursive coefficient a
Because the previous output is reused in the next calculation, the system has memory.
### Recursive simulation
The simulator processes the input sequence one sample at a time.
For every new input sample, it calculates:
    current_output = coefficient * previous_output + input_value
The newly calculated output is then stored and becomes the previous output for the next iteration.
This directly implements the mathematical recurrence:
    y[n] = a * y[n - 1] + x[n]
### Memory of the system
For the input:
    x[n] = [0, 0, 2, 2, 0, 0, 0]
and coefficient:
    a = 0.5
the output is:
    y[n] = [0, 0, 2, 3, 1.5, 0.75, 0.375]
After the input returns to zero, the output does not immediately become zero.
Instead:
    3 -> 1.5 -> 0.75 -> 0.375
This happens because the system continues to use its previous output.
The recursive term therefore acts as memory.
### Effect of the recursive coefficient
The simulator compares several values of a.
For:
    a = 0.2
the previous state disappears quickly.
For:
    a = 0.5
the response decays more slowly.
For:
    a = 0.9
the system remembers its previous state for much longer.
For:
    a = 1.0
the previous state does not decay.
For:
    a = 1.1
the previous state grows from sample to sample.
The implemented qualitative classification is:
    abs(a) < 1    Stable
    abs(a) = 1    Marginal
    abs(a) > 1    Unstable
For this first-order recursive system, coefficients with magnitude below one produce a decaying zero-input response.
### Impulse response
The discrete-time impulse input is:
    x[n] = [1, 0, 0, 0, ...]
For:
    a = 0.5
the simulator produces:
    h[n] = [1, 0.5, 0.25, 0.125, 0.0625, ...]
The theoretical impulse response is:
    h[n] = (0.5)^n
The program calculates the theoretical sequence independently and verifies:
    np.allclose(impulse_output, expected_impulse)
The numerical check passes:
    Impulse-response check: PASSED
### Connection with continuous-time systems
Continuous-time systems are commonly described by differential equations and signals such as:
    x(t)
    y(t)
Discrete-time systems use sequences:
    x[n]
    y[n]
A differential equation describes continuous evolution through derivatives.
A difference equation describes evolution from one sample to the next using previous samples.
The recursive coefficient in a discrete-time system plays a role similar to the natural decay or growth observed in continuous-time dynamic systems.
### Engineering interpretation
Difference equations are fundamental to digital signal processing.
Recursive equations appear in:
* digital filters
* feedback systems
* sampled control systems
* signal smoothing
* sensor processing
* biomedical signal processing
Later lessons will connect this recurrence to the Z-transform, poles, stability, and IIR digital filters.
### File
    recursive_system_simulator.py
### Run
From the repository root:
    py applications/signal_visualizer/recursive_system_simulator.py
## Z-Transform, ROC, and Stability
`z_plane_explorer.py` demonstrates how poles, zeros, the region of convergence, and the unit circle determine the behavior and stability of discrete-time systems.
### Recursive system
The explored first-order recursive system is:
    y[n] = a y[n - 1] + x[n]
Applying the Z-transform gives:
    Y(z) = a z^(-1) Y(z) + X(z)
Therefore, the transfer function is:
    H(z) = Y(z) / X(z)
    H(z) = 1 / (1 - a z^(-1))
    H(z) = z / (z - a)
The system has:
    pole: z = a
    zero: z = 0
### Region of convergence
For a causal impulse response:
    h[n] = a^n u[n]
the Z-transform converges when:
    |a / z| < 1
Therefore, the causal region of convergence is:
    |z| > |a|
The pole itself is never part of the ROC.
The program displays the causal ROC as the green area outside the dotted ROC boundary.
### Unit circle and stability
A discrete-time system is BIBO stable when its ROC contains the complete unit circle:
    |z| = 1
For this causal first-order system:
    |a| < 1  -> stable
    |a| = 1  -> boundary, but not BIBO stable
    |a| > 1  -> unstable
The program compares four real poles:
| System | Pole | Causal ROC | Result |
| --- | ---: | --- | --- |
| Fast decay | 0.5 | `|z| > 0.5` | Stable |
| Slow decay | 0.9 | `|z| > 0.9` | Stable |
| Boundary | 1.0 | `|z| > 1.0` | Not BIBO stable |
| Growing response | 1.1 | `|z| > 1.1` | Unstable |
### Impulse responses
For an impulse input, the system response is:
    h[n] = a^n
The four main cases produce different behavior:
    a = 0.5  -> rapid decay
    a = 0.9  -> slow decay
    a = 1.0  -> constant amplitude
    a = 1.1  -> growing amplitude
Selected values at sample 20 are approximately:
    0.5^20 = 0.000001
    0.9^20 = 0.121577
    1.0^20 = 1
    1.1^20 = 6.727500
This demonstrates that the distance of a pole from the origin determines whether the response decays, remains constant, or grows.
### Negative pole
The experiment also uses:
    a = -0.9
Its impulse response is:
    1, -0.9, 0.81, -0.729, 0.6561, ...
The pole is inside the unit circle because:
    |-0.9| = 0.9 < 1
The system is stable, but consecutive samples alternate between positive and negative values.
A negative real pole therefore produces an alternating response while its magnitude still decays.
### Complex-conjugate poles
The final experiment uses a complex-conjugate pole pair with:
    radius = 0.9
    angle = pi / 4 radians per sample
The poles are approximately:
    z1 = 0.6364 + j0.6364
    z2 = 0.6364 - j0.6364
The corresponding real impulse response is:
    h[n] = 0.9^n cos((pi / 4)n)
The pole radius controls the amplitude envelope:
    0.9^n
The pole angle controls the oscillation rate:
    omega = pi / 4 radians per sample
The oscillation period is:
    N = 2pi / omega
    N = 2pi / (pi / 4)
    N = 8 samples
Complex poles occur in conjugate pairs for systems with real coefficients. Together, the two poles produce a real oscillatory response.
### Main interpretation
The Z-plane provides two important pieces of information:
    pole radius -> growth or decay
    pole angle  -> oscillation rate
For causal systems:
    pole inside the unit circle  -> stable decay
    pole on the unit circle      -> persistent response
    pole outside the unit circle -> growing response
A stable system can still oscillate. Stability means that the oscillation amplitude eventually decreases, not that oscillation is absent.
### Visualizations
The program creates four groups of visualizations:
1. real poles, zeros, and the unit circle
2. causal ROC regions for stable, boundary, and unstable cases
3. impulse responses for four real poles
4. negative and complex-pole oscillatory responses
The green area represents the ROC. The blue dashed circle represents the unit circle, red crosses represent poles, and blue open circles represent zeros.
### Run
From the repository root:
    py applications/signal_visualizer/z_plane_explorer.py
The program prints the pole, zero, causal ROC, and stability classification for each system and displays the corresponding Z-plane and time-domain figures.

## Continuous and Discrete System Solver
`continuous_discrete_bridge.py` connects a continuous-time first-order system with its equivalent discrete-time recursive model.
The experiment focuses on the mathematical bridge between the s-plane and the Z-plane without duplicating the project in multiple software tools.
### Continuous-time system
The continuous first-order model is:
    tau dy(t) / dt + y(t) = x(t)
For a unit-step input and zero initial output, its response is:
    y(t) = 1 - exp(-t / tau)
The experiment uses:
    tau = 1.0 s
    sample interval = 0.2 s
    duration = 5.0 s
The continuous-system pole is:
    s = -1 / tau
    s = -1
Because the pole is in the left half of the s-plane, the continuous system is stable.
### Continuous-to-discrete mapping
The continuous pole is mapped into the Z-plane using:
    z = exp(s T_s)
For:
    s = -1
    T_s = 0.2 s
the discrete pole is:
    z = exp(-0.2)
    z = 0.8187307530779818
The discrete pole is inside the unit circle:
    |z| < 1
Therefore, the discrete system is also stable.
### Discrete-time system
The equivalent recursive model is:
    y[n] = a y[n - 1] + (1 - a) x[n]
where:
    a = exp(-T_s / tau)
For this experiment:
    a = 0.8187307530779818
    1 - a = 0.18126924692201818
The recursive calculation therefore becomes:
    y[n] = 0.8187307531 y[n - 1]
         + 0.1812692469 x[n]
At each new sample, the system keeps approximately 81.87 percent of its previous output and adds approximately 18.13 percent of the current input.
### Numerical comparison
The experiment calculates:
* a dense continuous-time step response
* the discrete response at 26 sampling instants
* the exact continuous response at the same sampling instants
* the absolute difference between both representations
The measured result is:
    Maximum error: 1.1102230246251565e-16
This value is effectively zero at floating-point precision.
The result confirms that the discrete recursive model matches the continuous first-order response at every sampling instant when the coefficient is calculated using the exact pole mapping.
### Visualization
The graph displays:
* the continuous response as a smooth blue curve
* the discrete response as orange sample markers
* the sampling instants using a stem plot
The discrete markers lie on the continuous curve.
The vertical stem lines are only a visual representation of discrete samples. They do not describe the system behavior between sampling instants.
### Main connection
The experiment connects the two system descriptions:
    continuous pole: s = -1 / tau
    discrete pole: z = exp(s T_s)
    continuous model:
    tau dy(t) / dt + y(t) = x(t)
    discrete model:
    y[n] = a y[n - 1] + (1 - a) x[n]
The continuous and discrete models use different mathematical languages, but they describe the same first-order memory and decay.
### Main conclusions
    left-half-plane continuous pole
    -> pole inside the Z-plane unit circle
    continuous exponential decay
    -> discrete geometric decay
    continuous time constant tau
    -> discrete coefficient a = exp(-T_s / tau)
The sampling interval controls how frequently the discrete system updates, while the exact pole mapping preserves the continuous response at the sampling instants.
### File
    continuous_discrete_bridge.py
### Run
From the repository root:
    py applications/signal_visualizer/continuous_discrete_bridge.py

## Why We Need the DFT
`dft_intuition.py` introduces the Discrete Fourier Transform as a practical tool for discovering the frequency content hidden inside a sampled signal.
The main intuition is to treat the DFT as a prism for signals:
    sampled signal
    -> DFT
    -> frequency spectrum
A waveform that appears complicated in the time domain can be separated into its individual frequency components in the frequency domain.
### Test signal
The experiment uses a sampling frequency of:
    Fs = 500 Hz
and a duration of:
    T = 4 s
The sampled signal contains three sinusoidal components:
    x(t) =
        sin(2*pi*12*t)
        + 0.75*sin(2*pi*35*t)
        + 0.25*sin(2*pi*60*t)
The three components therefore have frequencies and relative amplitudes:
    12 Hz -> amplitude 1.00
    35 Hz -> amplitude 0.75
    60 Hz -> amplitude 0.25
In the time domain these components combine into one complicated waveform.
The DFT separates them again.
### Frequency bins
For a signal with sampling frequency `Fs` and `N` samples, the spacing between DFT frequency bins is:
    delta_f = Fs / N
For this experiment:
    N = 2000
    delta_f = 0.25 Hz
The frequency represented by DFT bin `k` is:
    f_k = k * Fs / N
Therefore the expected positive-frequency bins are:
    12 Hz -> k = 48
    35 Hz -> k = 140
    60 Hz -> k = 240
### NumPy DFT workflow
The DFT is calculated using:
    spectrum = np.fft.fft(signal)
The result is complex because the DFT contains both magnitude and phase information.
The magnitude spectrum is obtained using:
    magnitude = np.abs(spectrum)
The corresponding frequency axis is generated with:
    frequencies = np.fft.fftfreq(len(signal), d=1 / sampling_frequency)
For a real-valued signal, the full DFT contains corresponding positive- and negative-frequency components.
This experiment keeps the nonnegative-frequency part for visualization and dominant-frequency detection.
### Automatic frequency detection
The program does not receive the frequencies 12 Hz, 35 Hz, and 60 Hz as search targets.
Instead, it examines the calculated magnitude spectrum and uses `np.argsort` to locate the three largest spectral peaks.
The measured result is:
    12.00 Hz, magnitude = 1000.00
    35.00 Hz, magnitude = 750.00
    60.00 Hz, magnitude = 250.00
The detected frequencies exactly match the components used to construct the signal.
The raw DFT magnitudes are not yet normalized to physical signal amplitudes. However, their ratios are preserved:
    1000 : 750 : 250
    =
    1.00 : 0.75 : 0.25
Amplitude normalization is treated separately later in the spectral-analysis block.
### Why the DFT is useful
A time-domain waveform shows how a signal changes with time, but it can hide the individual oscillations that produced it.
The DFT provides another representation:
    x[n]
    -> X[k]
where `x[n]` contains samples in time and `X[k]` describes their frequency content.
This is especially useful when analyzing measured signals such as ECG data.
A real measurement may contain:
    physiological signal
    + interference
    + sensor noise
    + power-line contamination
The DFT can reveal narrow spectral components that are difficult to recognize directly in the time-domain waveform.
The DFT itself does not decide whether a frequency is useful or unwanted. It reveals what frequency content exists. Engineering knowledge is then used to decide which components should be preserved, investigated, or filtered.
### DFT and FFT
The DFT is the mathematical transform.
The FFT is an efficient algorithm for calculating the same DFT.
Therefore:
    FFT result = DFT result
but the FFT computes it much more efficiently.
### Main conclusion
The central intuition of this lesson is:
    time-domain samples
    -> DFT / FFT
    -> frequency-domain spectrum
    -> identify dominant frequency components
The DFT acts as a prism for a sampled signal: components that are mixed together in the time waveform become individually visible in the frequency spectrum.
### File
    dft_intuition.py
### Run
From the repository root:
    py applications/signal_visualizer/dft_intuition.py
## DFT Matrix and Complex Spectrum
`dft_matrix.py` builds the Discrete Fourier Transform directly from its matrix definition instead of using the FFT as the primary calculation method.
For a signal with `N` samples, each DFT matrix element is:
    W[k, n] = exp(-j * 2*pi*k*n / N)
Each row of the DFT matrix corresponds to one DFT frequency bin. The row acts as a frequency detector that measures how strongly the input signal matches that complex exponential.
For `N = 4`, the theoretical matrix is:
    [ 1   1    1   1  ]
    [ 1  -j   -1   j  ]
    [ 1  -1    1  -1  ]
    [ 1   j   -1  -j  ]
Small numerical values around `1e-16` appear in the NumPy result because floating-point arithmetic cannot represent some trigonometric values as exact zeros.
The DFT is calculated through matrix multiplication:
    X = W @ x
For the test signal:
    x = [1, 0, -1, 0]
the matrix calculation produces approximately:
    X = [0, 2, 0, 2]
The result is compared with:
    np.fft.fft(signal)
and the two results agree within floating-point precision:
    Matrix DFT matches NumPy FFT: True
This demonstrates that the FFT does not compute a different transform. It is an efficient algorithm for computing the same DFT.
### Complex spectrum
A second signal is used to demonstrate phase information:
    x = [0, 1, 0, -1]
Its DFT is approximately:
    X = [0, -2j, 0, 2j]
The significant spectral components have magnitudes:
    2, 2
and phases:
    -90 deg, +90 deg
This shows why the full complex DFT contains more information than the magnitude spectrum alone.
For a complex spectral value:
    X[k] = a + j*b
the magnitude is:
    |X[k]| = sqrt(a^2 + b^2)
and the complex angle represents phase.
For real-valued input signals, the DFT has conjugate symmetry:
    X[N-k] = conjugate(X[k])
Therefore corresponding positive- and negative-frequency components contain related information.
Phase values at bins whose magnitude is approximately zero are not meaningful, because an almost-zero complex vector has no physically useful direction.
### Main conclusion
The DFT can be viewed as a linear transformation:
    time-domain samples
    -> DFT matrix
    -> complex frequency spectrum
or simply:
    X = W x
Each row of `W` tests one discrete frequency. Each value in `X` contains magnitude and phase information for that frequency.
The FFT produces the same DFT result but computes it much more efficiently.
### File
    dft_matrix.py
### Run
From the repository root:
    py applications/signal_visualizer/dft_matrix.py
## C Introduction Through DFT Implementation
`dft.c` implements the Discrete Fourier Transform directly in C.
The implementation uses the DFT definition:
    X[k] = sum x[n] * exp(-j * 2*pi*k*n / N)
Using Euler's formula:
    exp(-j*theta) = cos(theta) - j*sin(theta)
the real and imaginary parts are calculated separately:
    Re{X[k]} = sum x[n] * cos(2*pi*k*n/N)
    Im{X[k]} = -sum x[n] * sin(2*pi*k*n/N)
The implementation uses two nested loops:
    k -> selects the DFT frequency bin
    n -> iterates through all input samples
For each bin, the program accumulates the real and imaginary contributions from every signal sample.
### DFT function
The transform is implemented as a reusable function:
    void dft(const double signal[], int N, double real_part[], double imag_part[])
The input signal is marked `const` because the DFT function reads the samples but does not modify them.
The complex spectrum is stored using two arrays:
    real_part[k]
    imag_part[k]
so that:
    X[k] = real_part[k] + j*imag_part[k]
### Test signal
The test signal is:
    x = [0, 1, 0, -1]
Its expected DFT is approximately:
    X = [0, -2j, 0, 2j]
The C implementation produces the expected result.
### Floating-point verification
Direct equality is not used for floating-point values because numerical calculations can produce very small residual errors near zero.
Instead, the program checks:
    abs(calculated - expected) < tolerance
with:
    tolerance = 1e-9
The final verification result is:
    DFT test: PASSED
### Compile and run
From the `applications/signal_visualizer` directory:
    gcc dft.c -o dft.exe && ./dft.exe
The source file must be recompiled after changes before the executable reflects the updated code.
### Main conclusion
This lesson connects the mathematical definition of the DFT with a low-level implementation.
The same transform previously calculated with NumPy is now calculated explicitly in C using loops, trigonometric functions, arrays, and floating-point arithmetic.
This provides a foundation for later DSP implementations on embedded systems and for comparing high-level numerical tools with lower-level implementations.
### File
    dft.c
