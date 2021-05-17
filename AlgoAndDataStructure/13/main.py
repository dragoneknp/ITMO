file = open("search1.in", "r")
fin = file.read().split()
str_1 = fin[0]
str_2 = fin[1]
count = []

for i in range(len(str_2)):

    if str_2[i:i + len(str_1)] == str_1:
        count.append(i + 1)
fout = open("search1.out", "w")
print(len(count), file=fout)
print(*count, file=fout)
