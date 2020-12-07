//./lab14 input_file "c.bmp" output_file "dir" max_iter 100 dump_freq 5
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* inttostr(int a)
{
    int b = a;
    int k = 0;
    while (b > 0)
    {
        b = b / 10;
        k++;
    }
    char* c = (char*)malloc(sizeof(char) * (k + 1));
    int i;
    for (i = k - 1; i >= 0; i--)
    {
        if (a % 10 == 0){
            c[i] = '0';
        }
        else if (a % 10 == 1){
            c[i] = '1';
        }
        else if (a % 10 == 2){
            c[i] = '2';
        }
        else if (a % 10 == 3){
            c[i] = '3';
        }
        else if (a % 10 == 4){
            c[i] = '4';
        }
        else if (a % 10 == 5){
            c[i] = '5';
        }
        else if (a % 10 == 6){
            c[i] = '6';
        }
        else if (a % 10 == 7){
            c[i] = '7';
        }
        else if (a % 10 == 8){
            c[i] = '8';
        }
        else if (a % 10 == 9){
            c[i] = '9';
        }
        a = a / 10;
    }
    c[k] = '\0';
    return c;
}

int strtoint(char* c){
    int i = 0;
    int ans = 0;
    while (c[i] != '\0'){
        if (c[i] == '0'){
            ans = ans * 10;
        }
        else if (c[i] == '1'){
            ans = ans * 10 + 1;
        }
        else if (c[i] == '2'){
            ans = ans * 10 + 2;
        }
        else if (c[i] == '3'){
            ans = ans * 10 + 3;
        }
        else if (c[i] == '4'){
            ans = ans * 10 + 4;
        }
        else if (c[i] == '5'){
            ans = ans * 10 + 5;
        }
        else if (c[i] == '6'){
            ans = ans * 10 + 6;
        }
        else if (c[i] == '7'){
            ans = ans * 10 + 7;
        }
        else if (c[i] == '8'){
            ans = ans * 10 + 8;
        }
        else if (c[i] == '9'){
            ans = ans * 10 + 9;
        }
        i++;
    }
    return ans;
}

int main(int argc, char* argv[]) {
    char input_name[50];
    char output_name[50];
    int max_iter;
    int dump_freq = -1;
    for (int i=0;i<argc;i++){
        if (strcmp("input_file",argv[i])==0){
            strcpy(input_name,argv[i+1]);
            continue;
        }
        if (strcmp("output_file",argv[i])==0){
            strcpy(output_name,argv[i+1]);
            continue;
        }
        if (strcmp("max_iter",argv[i])==0){
            max_iter=strtoint(argv[i+1]);
            continue;
        }
        if (strcmp("dump_freq",argv[i])==0){
            dump_freq=strtoint(argv[i+1]);
            continue;
        }

    }
    if (dump_freq==-1){
        dump_freq=1;
    }


    FILE *file = fopen(input_name, "rb");

    int size, offset, width, height;
    char skip;
    int skip_int;
    char* name_out = "generation";
    char count[50];
    for (int i = 0; i < 2; ++i) {
        fread(&skip, 1, 1, file);
    }

    fread(&size, 4, 1, file);
    for (int i = 0; i < 4; ++i) {
        fread(&skip, 1, 1, file);
    }

    fread(&offset, 4, 1, file);
    fread(&skip_int, 4, 1, file);
    fread(&width, 4, 1, file);
    fread(&height, 4, 1, file);
    int **a = (int **) malloc(height * sizeof(int *));
    for (int i = 0; i < height; i++) {
        a[i] = (int *) malloc(width * sizeof(int));
    }

    int **b = (int **) malloc(height * sizeof(int *));
    for (int i = 0; i < height; i++) {
        b[i] = (int *) malloc(width * sizeof(int));
    }
    unsigned short int d;
    for (int i = height - 1; i >= 0; --i) {
        for (int j = 0; j < width; ++j) {
            fread(&d, 1, 1, file);
            fread(&d, 1, 1, file);
            fread(&d, 1, 1, file);
            if (d == 255) {
                a[i][j] = 255;
            } else
                a[i][j] = 0;
        }
    }

    char c;
    for (int k = 1; k < max_iter+1; ++k) {
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                b[i][j] = a[i][j];
                unsigned short int neighbour = 0;
                if (a[(i - 1 + height) % height][(j - 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i - 1 + height) % height][(j + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i - 1 + height) % height][(j + 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i + height) % height][(j - 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i + height) % height][(j + 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i + 1 + height) % height][(j - 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i + 1 + height) % height][(j + width) % width] == 0) {
                    neighbour++;
                }
                if (a[(i + 1 + height) % height][(j + 1 + width) % width] == 0) {
                    neighbour++;
                }
                if (a[i][j] == 0) {
                    if ((neighbour > 3) || (neighbour < 2)) {
                        b[i][j] = 255;
                    }
                } else {
                    if (neighbour == 3) {
                        b[i][j] = 0;
                    }
                }
            }
        }

        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                a[i][j] = b[i][j];
            }
        }

        if (k % dump_freq == 0) {
            strcpy(count, output_name);
            strcat(count, "/");
            strcat(count, name_out);
            strcat(count, inttostr(k));
            strcat(count, ".bmp");
            FILE *file_out = fopen(count, "wb");
            fseek(file, 0, SEEK_SET);
            fseek(file_out, 0, SEEK_SET);
            for (int i = 0; i < offset; i++) {
                fread(&c, 1, 1, file);
                fwrite(&c, 1, 1, file_out);
            }
            fseek(file, offset, SEEK_SET);
            fseek(file_out, offset, SEEK_SET);
            for (int i = height - 1; i >= 0; i--) {

                for (int j = 0; j < width; j++) {
                    fwrite(&b[i][j], 1, 1, file_out);
                    fwrite(&b[i][j], 1, 1, file_out);
                    fwrite(&b[i][j], 1, 1, file_out);
                }
            }
        }
    }
    return 0;
}
