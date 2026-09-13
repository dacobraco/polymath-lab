#include <stdio.h>
#include <math.h>

void dft(const double signal[], int N, double real_part[], double imag_part[]){
    const double pi = 3.141592653589793;
    for (int k = 0; k < N; k++) {
        real_part[k] = 0;
        imag_part[k] = 0;
        for (int n = 0; n < N; n++){
            double angle = 2*pi*k*n/N;
            real_part[k] += signal[n] * cos(angle);
            imag_part[k] -= signal[n] * sin(angle);
        }
    }
}

int main(void) {
    int N = 4;
    const double signal[4] = {0.0, 1.0, 0.0, -1.0};
    double real_part[4] = {0.0, 0.0, 0.0, 0.0};
    double imag_part[4] = {0.0, 0.0, 0.0, 0.0};

    dft(signal, N, real_part, imag_part);

    for (int k = 0; k < N; k++){
        printf("X[%d] = %.6f %+.6fj\n", k, real_part[k], imag_part[k]);
    }

    const double expected_real[4] = {0.0, 0.0, 0.0, 0.0};
    const double expected_imag[4] = {0.0, -2.0, 0.0, 2.0};

    const double tolerance = 1e-9;
    int test_passed = 1;

    for (int k = 0; k < N; k++){
        if (fabs(real_part[k] - expected_real[k]) > tolerance) test_passed = 0;
        if (fabs(imag_part[k] - expected_imag[k]) > tolerance) test_passed = 0;
    }

    if (test_passed == 0) {
        printf("DFT test: FAILED\n");
    }
    else {
        printf("DFT test: PASSED\n");
    }

    return 0;
}
