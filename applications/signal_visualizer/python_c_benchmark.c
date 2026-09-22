#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main(void){
    int number_of_samples = 1000000;
    double *signal_ptr = malloc(number_of_samples * sizeof(double));
    double energy = 0.0;
    LARGE_INTEGER timer_frequency;
    LARGE_INTEGER start_time;
    LARGE_INTEGER end_time;
    QueryPerformanceFrequency(&timer_frequency);
    if (signal_ptr == NULL) {
        printf("\nProgram couldn't reserve memory.");
        return 1;
    }

    for (int i = 0; i < number_of_samples; i++) {
        signal_ptr[i] = i * 1.0 / (number_of_samples - 1);
    }
    QueryPerformanceCounter(&start_time);
    for (int i = 0; i < number_of_samples; i++) {
        energy += signal_ptr[i] * signal_ptr[i];
    }
    QueryPerformanceCounter(&end_time);

    double duration = (double)(end_time.QuadPart - start_time.QuadPart) / timer_frequency.QuadPart;

    printf("\nEnergy is %f", energy);
    printf("\nThe process ran for %.9f seconds", duration);
    printf("\nNumber of bytes: %d", number_of_samples * (int)sizeof(double));
    free(signal_ptr);

    return 0;
}
