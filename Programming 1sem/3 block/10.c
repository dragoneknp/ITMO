#include <stdio.h>
#include <stdlib.h>

int *array;
nod(a, b
){
while (a!=0 && b!=0){
if (a>b){
a = a % b;
}
else{
b = b % a;
}
}
return (a+b);
};
nok(a, b
){
return (
a *b
)/
nod(a, b
);
}

int makearray(n, k) {
    int i = 0;
    while (n != 0) {
        array[k - i - 1] = n % 10;
        n = n / 10;
        i++;
    }
    return 0;
}

main() {
    int a, b, c, d, n, k = 0;
    scanf("%d %d", &a, &b);
    c = nod(a, b);
    printf("НОД равен = %d\n", c);
    d = nok(a, b);
    printf("НОК равен = %d\n", d);
    scanf("%d", &n);
    int r = n;
    while (r > 0) {
        k += 1;
        r = r / 10;
    }
    array = (int *) malloc(sizeof(int) * k);
    makearray(n, k);
    for (int i = 0; i < k; i++) {
        printf("%d ", array[i]);
    }
    return 0;
}
