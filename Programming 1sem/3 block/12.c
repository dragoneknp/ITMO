#include <stdio.h>

struct daymonthyear {
    int day;
    int month;
    int year;
} dmy;

int main(int argc, char *argv[]) {
    dmy.day = 17;
    dmy.month = 10;
    dmy.year = 2020;
    FILE *file;
    file = fopen(*argv, "w");
    for (int i = 0; i < 10; i++) {
        fprintf(file, "%d %d %d\n", dmy.day, dmy.month, dmy.year);
        dmy.day += 1;
    }
}
