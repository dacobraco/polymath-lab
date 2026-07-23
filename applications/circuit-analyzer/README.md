# AC Impedance Calculator

A Python calculator for the complex impedance of a series RLC circuit.

## Features

- Calculates resistor impedance
- Calculates inductor impedance
- Calculates capacitor impedance
- Calculates total series RLC impedance
- Calculates impedance magnitude
- Calculates phase angle in degrees
- Includes automatic tests

## Formulas

- Resistor: Z_R = R
- Inductor: Z_L = jωL
- Capacitor: Z_C = 1 / (jωC)
- Angular frequency: ω = 2πf
- Total impedance: Z = Z_R + Z_L + Z_C

## Example

Input values:

- R = 100 Ω
- L = 0.05 H
- C = 100 μF
- f = 50 Hz

Output:

```
Resistor impedance is 100.00+0.00j ohm
Inductor impedance is 0.00+15.71j ohm
Capacitor impedance is 0.00-31.83j ohm
Total impedance is 100.00-16.12j ohm
Magnitude is 101.29 ohm
Phase is -9.16 degrees
```