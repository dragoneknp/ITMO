#include <stdio.h>

main() {
    char b;
    b = getchar();
    printf("%d\n", b);
    int lenstr;
    scanf("%d\n", &lenstr);
    lenstr++;
    char string[lenstr];
    fgets(string, lenstr, stdin);
    int countdigit, countsymbol, countbigsymbol;
    for (int i = 0; i < lenstr; i++) {
        if (string[i] >= 65 && string[i] <= 90) {
            countbigsymbol += 1;
        } else if (string[i] >= 48 && string[i] <= 57) {
            countdigit += 1;
        } else if (string[i] >= 97 && string[i] <= 122) {
            countsymbol += 1;
        }
    }
    printf("Количество цифр:%d\n", countdigit);
    printf("Количество букв:%d\n", countsymbol);
    printf("Количество заглавных букв:%d\n", countbigsymbol);
    return 0;
}
