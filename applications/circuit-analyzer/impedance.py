import math as m

def resistor_impedance(resistance):
    ZR = complex(resistance, 0)
    return ZR

def inductor_impedance(inductance, frequency):
    omega = 2 * m.pi * frequency
    ZL = complex(0, omega * inductance)
    return ZL

def capacitor_impedance(capacitance, frequency):
    omega = 2 * m.pi * frequency
    ZC = complex(0, -1 / (omega * capacitance))
    return ZC

def series_rlc_impedance(resistance, inductance, capacitance, frequency):
    ZR = resistor_impedance(resistance)
    ZL = inductor_impedance(inductance, frequency)
    ZC = capacitor_impedance(capacitance, frequency)
    Z = ZR + ZL + ZC
    return Z

def impedance_magnitude(impedance):
    module = abs(impedance)
    return module

def impedance_phase(impedance):
    phase_rad = m.atan2(impedance.imag, impedance.real)
    phase_deg = m.degrees(phase_rad)
    return phase_deg

def print_all(resistance, inductance, capacitance, frequency):
    ZR = resistor_impedance(resistance)
    ZL = inductor_impedance(inductance, frequency)
    ZC = capacitor_impedance(capacitance, frequency)
    Z = series_rlc_impedance(resistance, inductance, capacitance, frequency)

    print(f"Resistor impedance is {ZR:.2f} ohm")
    print(f"Inductor impedance is {ZL:.2f} ohm")
    print(f"Capacitor impedance is {ZC:.2f} ohm")
    print(f"Total impedance is {Z:.2f} ohm")
    print(f"Magnitude is {impedance_magnitude(Z):.2f} ohm")
    print(f"Phase is {impedance_phase(Z):.2f} degrees")

resistance = 100
inductance = 0.05
capacitance = 100e-6
frequency = 50

print_all(resistance, inductance, capacitance, frequency)