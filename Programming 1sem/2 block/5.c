#include <stdio.h>

main() {
    int m[6] = {34, 45, 56, 67, 78, 89};
    for (int i = 0; i < 6; i++)
        printf("%d ", m[i]);
    printf("\n");
    int a[2][2] = {{2, 1},
                   {1, 3}};
    int b[2][2] = {{1, 2},
                   {3, 1}};
    int f[2][2];
    {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                f[i][j] = 0;
                for (int k = 0; k < 2; ++k)
                    f[i][j] += (a[i][k] * b[k][j]); 
            }
        }
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) 
            printf("%d ", f[i][j]);
        printf("\n");
    }
    return 0;
}
