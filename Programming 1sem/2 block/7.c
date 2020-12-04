#include <stdio.h>
#include <math.h>

#define PI 3.14159265

main() {
    struct app { 
        unsigned int NumLock: 1;
        unsigned int CapsLock: 1;
        unsigned int ScrollLock: 1;
    };
    union App { 
        unsigned char value;
        struct app bitfield;
    };
    enum printed_editions {
        книга, журнал, газета
    };
    enum printed_editions edit;
    edit = газета;
    switch (edit) {
        case книга:
            printf("Значение Книги в каталоге = %d \n", книга);
            break;
        case журнал:
            printf("Значение Журнала в каталоге = %d \n", журнал);
            break;
        case газета:
            printf("Значение Газеты в каталоге = %d \n", газета);
            break;
    }
    struct circle {
        int x1, y1, radius;
        float length;
    };
    struct circle l;
    l.x1 = 0;
    l.y1 = 0;
    l.radius = 4;
    l.length = 2 * PI * l.radius;
    printf("Длина окружности равна = %f", l.length);
    int state;
    scanf("%X", &state);
    union App x;
    x.value = state;
    printf("%d\n", x.bitfield.NumLock);
    printf("%d\n", x.bitfield.CapsLock);
    printf("%d\n", x.bitfield.ScrollLock);
    return 0;
}
