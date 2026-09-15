#include <stdio.h>
#include <math.h>
#include <time.h>

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

int main(void){
    const double pi = 3.141592653589793;
    const int number_of_samples[5] = {64, 128, 256, 512, 1024};
    const int size_count = sizeof(number_of_samples) / sizeof(number_of_samples[0]);
    const int repetitions = 20;
    volatile double checksum = 0.0;

    double signal[1024];
    double real_part[1024];
    double imag_part[1024];

    printf("Direct DFT benchmark\n");
    printf("Repetitions per size: %d\n\n", repetitions);
    printf("%10s %15s\n", "Samples", "Average [ms]");

    for (int size_index = 0; size_index < size_count; size_index++) {
        int N = number_of_samples[size_index];

        for (int n = 0; n < N; n++) {
            signal[n] = sin(2.0*pi*n/N);
        }

        dft(signal, N, real_part, imag_part);

        clock_t start_time = clock();

        for (int i = 0; i < repetitions; i++) {
            dft(signal, N, real_part, imag_part);
            int index = i % N;
            checksum += real_part[index] + imag_part[index];
        }

        clock_t end_time = clock();
        double duration = (double)(end_time - start_time);

        double time = duration / CLOCKS_PER_SEC;
        double average_time_ms = 1000.0 * time / repetitions;
        printf("%10d %15.6f\n", N, average_time_ms);
    }
    printf("Checksum: %.6f\n", checksum);
    return 0;
}