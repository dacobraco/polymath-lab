#include <stdio.h>

void fir_filter(double input[], int input_length, double coefficients[], int number_of_taps, double output[]) {

    int output_length = input_length + number_of_taps - 1;
    for (int n = 0; n < output_length; n++) {
        double accumulator = 0.0;

        for (int k = 0; k < number_of_taps; k++) {
            int input_index = n - k;
            if (input_index >= 0 && input_index < input_length) {
                accumulator += coefficients[k] * input[input_index];
            }
        }
        output[n] = accumulator;
    }
}

int main(void)
{
    double input[] = {1.0};
    double coefficients[] = {
    7.18992617e-04, 1.05300949e-03, 2.04128689e-04, -1.31224541e-03, -1.84565738e-03, 2.28610061e-18,
    3.04986296e-03, 3.52446569e-03, -8.58242837e-04, -6.49999277e-03, -5.95943296e-03, 3.18282432e-03,
    1.23391660e-02, 8.85422051e-03, -8.21208444e-03, -2.16754411e-02, -1.17947299e-02, 1.83614093e-02,
    3.73566941e-02, 1.43248532e-02, -4.09892217e-02, -7.12515020e-02, -1.60339348e-02, 1.26676190e-01,
    2.82092917e-01, 3.49387503e-01, 2.82092917e-01, 1.26676190e-01, -1.60339348e-02, -7.12515020e-02,
    -4.09892217e-02, 1.43248532e-02, 3.73566941e-02, 1.83614093e-02, -1.17947299e-02, -2.16754411e-02,
    -8.21208444e-03, 8.85422051e-03, 1.23391660e-02, 3.18282432e-03, -5.95943296e-03, -6.49999277e-03,
    -8.58242837e-04, 3.52446569e-03, 3.04986296e-03, 2.28610061e-18, -1.84565738e-03, -1.31224541e-03,
    2.04128689e-04, 1.05300949e-03, 7.18992617e-04
    };
    int input_length = sizeof(input) / sizeof(input[0]);
    int number_of_taps = sizeof(coefficients) / sizeof(coefficients[0]);
    int output_length = input_length + number_of_taps - 1;
    double output[output_length];

    fir_filter(input, input_length, coefficients, number_of_taps, output);

    for (int n = 0; n < output_length; n++) {
        printf("y[%d] = %f\n", n, output[n]);
    }

    return 0;
}
