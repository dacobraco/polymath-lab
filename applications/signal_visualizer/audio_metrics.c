#include <stdio.h>
#include <math.h>

int main(void) {
    double sample;
    int read_status = scanf("%lf", &sample);
    int sample_count = 0;
    double sum_of_squares = 0.0;
    double max_amplitude = 0.0;

    while (read_status == 1) {
        if (!isfinite(sample)) {printf("The sample is not finite."); return 1;}
        sample_count += 1;
        sum_of_squares += sample * sample;
        if (fabs(sample) > max_amplitude) { max_amplitude = fabs(sample);}

        read_status = scanf("%lf", &sample);
    }

    if (read_status == 0) {printf("There was an error in input."); return 1;}
    if (ferror(stdin) != 0) {printf("There was an error while reading inputs."); return 1;}
    if (sample_count == 0) {printf("No sample was read."); return 1;}

    double rms = sqrt(sum_of_squares / sample_count);

    printf("Samples: %d\n", sample_count);
    printf("RMS: %.12f\n", rms);
    printf("Peak: %.12f\n", max_amplitude);

    return 0;
}
