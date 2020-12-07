//./lab15 --filename "15.arc" --list
//./lab15 --filename "15.arc" --extract
//./lab15 --filename "15.arc" --create "a.txt" "b.txt" "c.txt"
#include <stdio.h>
#include <string.h>
void archive(char *filename, int how_many_files, char **files_from_command_line) {
    FILE *file;
    file = fopen(filename, "w");
    unsigned int filename_size;
    unsigned int size;
    for (int i = 0; i < how_many_files; i++) {
        filename_size = strlen(files_from_command_line[i]);
        fputc(filename_size, file);
        for (int j = 0; j < filename_size; j++) {
            fputc(files_from_command_line[i][j], file);
        }
        FILE *archivating_file;
        archivating_file = fopen(files_from_command_line[i], "r");
        fseek(archivating_file, 0, SEEK_END);
        size = ftell(archivating_file);
        fseek(archivating_file, 0, SEEK_SET);
        fwrite(&size, sizeof(unsigned int), 1, file);
        for (int j = 0; j < size; j++) {
            fputc(getc(archivating_file), file);
        }

    }
}

void extract(char *filename) {
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    unsigned int how_many_bytes = ftell(file);
    fseek(file, 0, SEEK_SET);
    while (ftell(file) < how_many_bytes) {
        unsigned int size = getc(file);
        char name_of_file[size];
        for (int i = 0; i < size; i++) {
            name_of_file[i] = getc(file);
        }
        fread(&size, sizeof(unsigned int), 1, file);
        FILE *new_file;
        new_file = fopen(name_of_file, "w");
        for (int i = 0; i < size; i++) {
            fputc(getc(file), new_file);
        }
        fclose(new_file);

    }

}

void list(char *filename) {
    FILE *file;
    file = fopen(filename, "r");
    fseek(file, 0, SEEK_END);
    unsigned int how_many_bytes = ftell(file);

    fseek(file, 0, SEEK_SET);
    while (ftell(file) < how_many_bytes) {
        unsigned int size = getc(file);
        char name_of_file[size];
        for (int i = 0; i < size; i++) {
            name_of_file[i] = getc(file);
            printf("%c", name_of_file[i]);
        }
        printf("\n");

        fread(&size, sizeof(unsigned int), 1, file);
        fseek(file, size, SEEK_CUR);
    }
}

int main(int argc, char *argv[]) {
    char filename[50];
    int how_many_files;

    for (int i = 0; i < argc; i++) {

        if (strcmp("--filename", argv[i]) == 0) {
            strcpy(filename, argv[i + 1]);

            continue;
        }
        if (strcmp("--create", argv[i]) == 0) {
            how_many_files = argc - i - 1;
            archive(filename, how_many_files, &argv[i + 1]);
            continue;
        }
        if (strcmp("--extract", argv[i]) == 0) {
            extract(filename);
            continue;
        }
        if (strcmp("--list", argv[i]) == 0) {

            list(filename);
            continue;
        }

    }
    return 0;

}


