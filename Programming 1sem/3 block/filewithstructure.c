#include "filewithstructure.h"
#include <stdio.h>
#include <math.h>

void scancoordinate() {
    scanf("%f %f\n", &tr.x1, &tr.y1);
    scanf("%f %f\n", &tr.x2, &tr.y2);
    scanf("%f %f", &tr.x3, &tr.y3);
}

float counts(float x1, float x2, float x3, float y1, float y2, float y3) {
    float pp, s, a, b, c;
    a = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    b = sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2));
    c = sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2));
    pp = (a + b + c) / 2;
    if (pp * (pp - a) * (pp - b) * (pp - c) > 0) {
        s = sqrt(pp * (pp - a) * (pp - b) * (pp - c));
    } else {
        s = -1;
    }
    return s;
}

float countp(float x1, float x2, float x3, float y1, float y2, float y3) {
    float p, a, b, c;
    a = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    b = sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2));
    c = sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2));
    p = a + b + c;
    return p;
}
