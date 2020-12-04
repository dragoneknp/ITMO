#include <stdio.h>
#include <stdlib.h>

main() {
    float a[4]; 
    int i;
    float *p = a; 
    for (i = 0; i < 4; i++)
        scanf("%f", &a[i]); 
    for (i = 0; i < 4; i++)
        printf("%f ", *(p + i)); 
    printf("\n");
    float *b;
    b = (int *) malloc(4 * sizeof(int)); 
    for (i = 0; i < 4; i++)
        scanf("%f", &b[i]);
    for (i = 0; i < 4; i++)
        printf("%f ", b[i]);
    free(b); 
    return 0;
}
