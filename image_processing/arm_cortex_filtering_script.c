#include "arm_math.h"
#include <stdint.h>
#include <stdio.h>

#define IMG_SIZE 5  // Define a small test image (5x5 pixels)
#define KERNEL_SIZE 3

// Example 5x5 Grayscale Image (Simulated Space Image: 0 = Black, 255 = White)
int8_t image[IMG_SIZE * IMG_SIZE] = {
    0,   0,   0,   0,   0,
    0,  127, 127, 127,  0,
    0,  127,   0, 127,  0,
    0,  127, 127, 127,  0,
    0,   0,   0,   0,   0
};

// Sobel Kernels (Q7 format: -128 to 127 range)
const int8_t sobel_x[KERNEL_SIZE * KERNEL_SIZE] = {
    -1,  0,  1,
    -2,  0,  2,
    -1,  0,  1
};

const int8_t sobel_y[KERNEL_SIZE * KERNEL_SIZE] = {
    -1, -2, -1,
     0,  0,  0,
     1,  2,  1
};

// Output buffers
int8_t Gx[IMG_SIZE * IMG_SIZE];
int8_t Gy[IMG_SIZE * IMG_SIZE];
int8_t edge_magnitude[IMG_SIZE * IMG_SIZE];

// Function to compute edge magnitude
void compute_edge_magnitude(int8_t *Gx, int8_t *Gy, int8_t *edge_mag, uint32_t size) {
    for (uint32_t i = 0; i < size; i++) {
        int32_t gx = Gx[i];
        int32_t gy = Gy[i];

        // Approximate sqrt(Gx^2 + Gy^2) using abs(Gx) + abs(Gy)
        edge_mag[i] = (int8_t)(__USAT(abs(gx) + abs(gy), 8));
    }
}

int main() {
    // Apply Sobel-X Filter
    arm_convolve_3x3_q7(image, IMG_SIZE, IMG_SIZE, sobel_x, Gx, 1);
    
    // Apply Sobel-Y Filter
    arm_convolve_3x3_q7(image, IMG_SIZE, IMG_SIZE, sobel_y, Gy, 1);

    // Compute Gradient Magnitude (L1 Approximation for Speed)
    compute_edge_magnitude(Gx, Gy, edge_magnitude, IMG_SIZE * IMG_SIZE);

    // Print Edge Detection Result
    printf("Edge Magnitude Output:\n");
    for (int i = 0; i < IMG_SIZE; i++) {
        for (int j = 0; j < IMG_SIZE; j++) {
            printf("%3d ", edge_magnitude[i * IMG_SIZE + j]);
        }
        printf("\n");
    }

    return 0;
}
