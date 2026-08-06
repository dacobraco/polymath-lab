# System Response Explorer

A simple Python application that demonstrates how basic systems transform numerical inputs and signals.

## Systems

- Amplify: `y = 2x`
- Attenuate: `y = 0.5x`
- Shift: `y = x + 3`

## Features

- Accepts a single number
- Accepts a comma-separated list
- Applies the selected system
- Displays the input and output
- Delays and advances discrete signals by one sample
- Checks systems for time invariance
- Creates and visualizes unit impulses and impulse responses

## Project Structure

- `basic_systems.py` - contains the system functions
- `linearity.py` - checks systems for linearity
- `main.py` - runs the interactive application
- `tests.py` - verifies the system functions
- `signal_shifts.py` - delays and advances discrete signals
- `time_invariance.py` - checks systems for time invariance
- `impulse_response.py` - creates and visualizes unit impulses and impulse responses

## Run

```bash
python main.py
```

## Tests

```bash
python tests.py
```

Expected output:

```text
All tests passed!
```

## Linearity Checker

The application can test whether a selected system satisfies:

T(a*x1 + b*x2) = a*T(x1) + b*T(x2)

Current results:

- Amplify is linear
- Attenuate is linear
- Shift is not linear

Run the checker:

```bash
python linearity.py
```

## Signal Shifts

The application supports one-sample signal shifts with zero padding:

- Delay: `y[n] = x[n - 1]`
- Advance: `y[n] = x[n + 1]`

Example:

```text
Input:    [1, 2, 3, 4]
Delayed: [0, 1, 2, 3]
Advanced:[2, 3, 4, 0]
```

## Time-Invariance Checker

A system is time invariant when delaying the input before applying the
system gives the same result as applying the system before delaying the
output.

Current results:

- Amplify - time invariant
- Attenuate - time invariant
- Shift - time invariant
- Multiply by index - time varying

Run the checker:

```bash
python time_invariance.py
```

## Previous Sample Addition

The system is defined by:

`y[n] = x[n] + x[n - 1]`

This system has memory because its output depends on both the current and the previous input sample.

Example:

```text
Input:  [1, 2, 3, 4]
Output: [1, 3, 5, 7]
```

## Impulse Response

The impulse response describes how a system responds to a unit impulse `δ[n]`.

The explorer visualizes the following systems:

- `h1[n] = 2δ[n]` - amplification
- `h2[n] = δ[n - 1]` - one-sample delay
- `h3[n] = δ[n] + 0.5δ[n - 1]` - current and delayed response

The signals are displayed using discrete stem plots.

Run the explorer:

```bash
python impulse_response.py
```
