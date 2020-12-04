#include <stdlib.h>
#include <stdio.h>
#include <string.h>
unsigned int reverseBytes(unsigned int n) // реверс
{
return ((n >> 24) & 0x000000ff) | ((n >> 8) & 0x0000ff00) | ((n << 8) & 0x00ff0000) | ((n <<
24) & 0xff000000);
}
typedef union TAGHEADER
{
char bufforstruct[12]; // строка, по смещению которой мы сможем читать то или иное
поле структуры
struct {
unsigned short empty; // 2 bytes
unsigned char version[3]; // 3 bytes
unsigned char version1; // 1 byte
unsigned char version2; // 1 byte
unsigned char flags; // 1 byte
unsigned int size; // 4 bytes
} tagdata;
} TAGHEADER;
typedef union FRAMEHEADER
{
char bufforstruct[10]; // строка, по смещению которой мы сможем читать то или иное
поле структуры
struct {
char name[4]; // 4 bytes
unsigned int size; // 4 bytes
unsigned short flags; // 2 bytes
} framedata;
} FRAMEHEADER;
void copyFile(FILE* inp, FILE* outp) { // функция копирования ,принимает что копировать
и куда копировать
int Char;
while ((Char = getc(inp)) != EOF) // читаем по одному символу пока файл читается(пока
не конец файла)
putc(Char, outp); // записываем прочитанный символ в выходной файл
}
void show(char* fileName)
{
FILE* file;
file = fopen(fileName, "rb"); // открытие нетекстового файла на чтение
if (file == NULL) // проверка на то ,что файл открылся {
printf("Smth wrong with file!\n");
}
fseek(file, 0, SEEK_SET); // ставим указатель на начало файла
TAGHEADER tagHeader;
fread(tagHeader.bufforstruct + 2, sizeof(char), 10, file); // считываем из файла 10
чар обьектов и запихиваем в буфер тега,начиная со второго байта
unsigned int tagSize = reverseBytes(tagHeader.tagdata.size); // делаем реверс с помощью
маски
printf("%sv%d.%d\n", tagHeader.tagdata.version,
tagHeader.tagdata.version1,
tagHeader.tagdata.version2);
while (ftell(file) < tagSize + 10) // смотрим на текущее положение указателя в файле
и спрашиваем больше ли оно чем реверснутый размер тега
{
FRAMEHEADER frameHeader;
fread(frameHeader.bufforstruct, sizeof(char), 10, file); // считываем из File 10 объектов
длины char и запихиываем в буфер фрейма
if (frameHeader.framedata.name[0] == 0) // если в имени файла ничего нет - дальше не
читаем
break;
printf("%s: ", frameHeader.framedata.name); // вывод имени файла
unsigned int frameSize = reverseBytes(frameHeader.framedata.size); // опять ревирсим с
помощью маски
unsigned char* frameContent;
frameContent = malloc(sizeof(char) * frameSize); // выделяем память под
строку(массив из чаров)
fread(frameContent, sizeof(char), frameSize, file); // считываем FrameSize
элеметов длины char в FrameContent
unsigned int i;
for ( i = 0; i < frameSize; ++i)
{
printf("%c", frameContent[i]); // печатаем посимвольно каждый символ фрейма
}
printf("\n");
free(frameContent); // освобождаем память под FrameContent
}
fclose(file); // закрываем файл
}
void get(char* fileName, char frameName[4])
{
FILE* file;
file = fopen(fileName, "rb");
TAGHEADER tagHeader;
fread(tagHeader.bufforstruct + 2, sizeof(char), 10, file);// считываем из файла 10
чар обьектов и запихиваем в буфер тега,начиная со второго байта
unsigned int tagSize = reverseBytes(tagHeader.tagdata.size);//получаем размер тегов
реверсом с помощью маски
while (ftell(file) < tagSize + 10) // смотрим на текущее положение указателя в файле
и спрашиваем больше ли оно чем реверснутый размер тега
{
FRAMEHEADER frameHeader;
fread(frameHeader.bufforstruct, sizeof(char), 10, file); // считываем из File 10 объектов
длины char и запихиываем в буфер фрейма
unsigned int frameSize = reverseBytes(frameHeader.framedata.size); // снова
ревирсим достаем размер фрейма
if (strcmp(frameHeader.framedata.name, frameName) == 0) // сравниваем название
считанного и запрошенного фрейма, если не совпадают, то идем, пока не найдем, либо не
обнаружим, что такого фрейма нет
{
printf("%s: ", frameHeader.framedata.name); //выводим название фрейма
unsigned char* frameContent;
frameContent = malloc(sizeof(char) * frameSize); // выделяем памяти под
строку(массив из чаров)
fread(frameContent, sizeof(char), frameSize, file); // считываем FrameSize элеметов
длины char в FrameContent из File
unsigned int i;
for (i = 0; i < frameSize; ++i)
{
printf("%c", frameContent[i]); // посимвольно выводим фрейм
}
printf("\n");
free(frameContent); // освобождаем память
fclose(file); // закрываем файл
return;
}
fseek(file, frameSize, SEEK_CUR); // меняем указатель в файле(смещаем на frameSize)
}
fclose(file);
printf("No value for %s!", frameName); // если не нашли пишем что нету такого
}
void set(char* fileName, char frameName[4], char* frameValue)
{
FILE* file;
file = fopen(fileName, "rb");
TAGHEADER tagHeader;
fread(tagHeader.bufforstruct + 2, sizeof(char), 10, file); // считываем из файла 10
чар обьектов и запихиваем в буфер тега,начиная со второго байта
unsigned int tagSize = reverseBytes(tagHeader.tagdata.size); //получаем размер тегов
реверсом с помощью маски
unsigned int oldFramePos = 0;
unsigned int oldFrameSize = 0;
while (ftell(file) < tagSize + 10) // смотрим на текущее положение указателя в файле
и спрашиваем больше ли оно чем реверснутый размер тега
{
FRAMEHEADER frameHeader;
fread(frameHeader.bufforstruct, sizeof(char), 10, file); // считываем из File 10 объектов
длины char и запихиываем в буфер фрейма
unsigned int frameSize = reverseBytes(frameHeader.framedata.size); // реверсим и
получаем размер фрейма с помощью маски
if (strcmp(frameHeader.framedata.name, frameName) == 0) // сравниваем название
считанного и запрошенного фрейма, если не совпадают, то идем, пока не найдем, либо не
обнаружим, что такого фрейма нет
{
oldFramePos = ftell(file) - 10;//показвыаем, что текущее указание на фрейм —
текущий указатель - 10
oldFrameSize = frameSize; // копируем размер
фрейма break;
}
fseek(file, frameSize, SEEK_CUR); // меняем указатель в файле (смещаем на frameSize)
}
unsigned int valueSize = strlen(frameValue);
unsigned int newTagSize = tagSize - oldFrameSize + valueSize + 10 * (oldFramePos != 0);
if (oldFramePos == 0) // если позиция старого фрейма равна 0,то такого фрейма не
существует - просто смещаемся
{
oldFramePos = ftell(file);
}
if (valueSize == 0) // если новое значение равно нулю,то фрейм следует уничтожить
{
newTagSize -= 10;
}
FILE* fileCopy;
fileCopy = fopen("temp.mp3", "wb"); // создаем "temp.mp3",который открываем на запись
нетекстового файла
fseek(file, 0, SEEK_SET); // ставим указатель в изначальном файле на начало
fseek(fileCopy, 0, SEEK_SET); // ставим указатель в временном файле на начало
copyFile(file, fileCopy); // копируем один файл в другой
fclose(file); // закрываем оба файла
fclose(fileCopy);
fileCopy = fopen("temp.mp3", "rb"); // открываем временный файл на чтение
file = fopen(fileName, "wb"); // открываем исходный файл на запись
tagHeader.tagdata.size = reverseBytes(newTagSize);
fwrite(tagHeader.bufforstruct + 2, sizeof(char), 10, file); // записываем поэлементно 10
символов в буфер, начиная со 2
fseek(fileCopy, 10, SEEK_SET); // ставим указатель на 10 символ в временном
файле unsigned int i;
for (i = 0; i < oldFramePos - 10; ++i)
{
int c;
c = getc(fileCopy); //посимвольно считываем
putc(c, file); // записываем в исходный файл
}
if (valueSize > 0)
{
FRAMEHEADER frameHeader;
unsigned int i;
for (i = 0; i < 4; ++i)
{
frameHeader.framedata.name[i] = frameName[i]; // записываем имя
}
frameHeader.framedata.size = reverseBytes(valueSize);
frameHeader.framedata.flags = 0;
fwrite(frameHeader.bufforstruct, sizeof(char), 10, file); // записываем 10 байт в фрейм
буффер
}
fwrite(frameValue, sizeof(char), valueSize, file); //записываем новое значение фрейма
fseek(fileCopy, oldFramePos + 10 + oldFrameSize, SEEK_SET); // ищем старый фрейм
for (i = ftell(file); i < newTagSize; ++i) // проходимся по значениям тега
{
unsigned short int c;
c = getc(fileCopy);
putc(c, file); // копируем
}
printf("New value %s:%s\n", frameName, frameValue);
copyFile(fileCopy, file);// копируем все назад
fclose(file); //закрываем оба файла
fclose(fileCopy);
remove("temp.mp3"); // удаляем временный файл
}
int main(int argc, char* argv[]) {
char* fileName;
char* frameName;
char* value;
char showFlag = 0;
char setFlag = 0;
char getFlag = 0;
int i;
for (i = 1; i < argc; i++) { // идем по введенным в консоли данным
if (argv[i][2]=='s' && argv[i][3]=='h'){// если show ставим флаг show и
продолжаем
 showFlag = 1;
continue;
}
if (argv[i][2] == 'f') // если встречаем на третье позиции "f",то это "--filepath"
{
fileName = strpbrk(argv[i], "=") + 1; // записываем имя файла
}
if (argv[i][2] == 'g') { // функция get ставим флаг на get
getFlag = 1;
frameName = strpbrk(argv[i], "=") + 1; //записываем имя фрейма который нужно
получить
continue;
}
if (argv[i][2] == 's') { // функция set ставим флаг на set
setFlag = 1;
frameName = strpbrk(argv[i], "=") + 1; // записываем имя фрема который изменить
continue;
}
if (argv[i][2] == 'v') {
value = strpbrk(argv[i], "=") + 1; // записываем имя фрейма на которое изменить
continue;
}
}
if (showFlag)
{
show(fileName);
}
if (getFlag)
{
get(fileName, frameName);
}
if (setFlag)
{
set(fileName, frameName, value);
}
return 0;
}
