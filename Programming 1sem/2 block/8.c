#include <stdio.h>

main() {
    
    int lenstr;
    scanf("%d\n", &lenstr);
    lenstr++;
    char string[lenstr];
    fgets(string, lenstr, stdin);
    int lenstr1;
    scanf("%d\n", &lenstr1);
    lenstr1++;
    char string1[lenstr1];
    fgets(string1, lenstr1, stdin);
    int n;
    scanf("%d", &n);
    char newstring[lenstr + n];
    for (int i = 0; i < lenstr; i++) {
        newstring[i] = string[i];
    }
    for (int i = 0; i < n; i++) {
        newstring[i + lenstr] = string1[i];
    }
    for (int i = 0; i < lenstr + n; i++) {
        printf("%c", newstring[i]);
    }
    printf("\n");

    int lenstr2, lenstr3;
    scanf("%d\n", &lenstr2);
    lenstr2++;
    char string2[lenstr2];
    fgets(string2, lenstr2, stdin);
    scanf("%d\n", &lenstr3);
    lenstr3++;
    char string3[lenstr3];
    fgets(string3, lenstr3, stdin);
    int flag = 0;
    for (int i = 0; i < lenstr2; i++) {
        if (string2[i] != string3[i]) {
            flag = 1;
        }
    }
    if (flag == 1) {
        printf("Строки не равны\n");
    } else {
        printf("Строки равны\n");
    }
    
    int lenstr4, lenstr5;
    scanf("%d\n", &lenstr4);
    lenstr4++;
    char string4[lenstr4];
    fgets(string4, lenstr4, stdin);
    scanf("%d\n", &lenstr5);
    lenstr5++;
    char string5[lenstr5];
    fgets(string5, lenstr5, stdin);
    int n1;
    scanf("%d", &n1);
    for (int i = 0; i < n1; i++) {
        string5[i] = string4[i];
    }
    for (int i = 0; i < lenstr5; i++) {
        printf("%c", string5[i]);
    }
    
    char b;
    b = getchar();
    int lenstr6;
    scanf("%d\n", &lenstr6);
    lenstr6++;
    char string6[lenstr6];
    fgets(string6, lenstr6, stdin);
    int k = -1;
    for (int i = 0; i < lenstr6; i++) {
        if (string6[i] == b) {
            k = i;
        }
    }
    if (k == -1) {
        printf("Такого символа нету в данной строке");
    } else {
        printf("Последнее вхождение данного символа =%d", k + 1);
    }
    
    int k1 = -1;
    int flag1 = 1;
    int lenstr7, lenstr8;
    scanf("%d\n", &lenstr7);
    lenstr7++;
    char string7[lenstr7];
    fgets(string7, lenstr7, stdin);
    scanf("%d\n", &lenstr8);
    lenstr8++;
    char string8[lenstr8];
    fgets(string8, lenstr8, stdin);
    for (int i = 0; i < lenstr7; i++) {
        for (int j = 0; j < lenstr8; j++) {
            if (string7[i] == string8[j]) {
                flag1 = 0;
            }
        }
        if (flag1 == 0) {
            k1 = i;
            break;
        }
    }
    if (k1 == -1) {
        printf("%d", lenstr7);
    } else {
        printf("%d", k1);
    }
    
    return 0;
}
