from impedance import (
    resistor_impedance,
    inductor_impedance,
    capacitor_impedance,
    series_rlc_impedance,
    impedance_magnitude,
    impedance_phase
)

resistance = 100
inductance = 0.05
capacitance = 100e-6
frequency = 50

ZR = resistor_impedance(resistance)
ZL = inductor_impedance(inductance, frequency)
ZC = capacitor_impedance(capacitance, frequency)
Z = series_rlc_impedance(
    resistance,
    inductance,
    capacitance,
    frequency
)

assert ZR == complex(100, 0)
assert round(ZL.imag, 2) == 15.71
assert round(ZC.imag, 2) == -31.83
assert round(Z.real, 2) == 100.00
assert round(Z.imag, 2) == -16.12
assert round(impedance_magnitude(Z), 2) == 101.29
assert round(impedance_phase(Z), 2) == -9.16

print("All tests passed.")