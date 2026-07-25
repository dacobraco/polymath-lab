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

## Project Structure

- `basic_systems.py` — contains the system functions
- `main.py` — runs the interactive application
- `tests.py` — verifies the system functions

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