def find_prefix(string_):
    prefix = [0] * len(string_)
    for i in range(1, len(string_)):
        k = prefix[i - 1]
        while k > 0 and string_[i] != string_[k]:
            k = prefix[k - 1]
        if string_[i] == string_[k]:
            k += 1
        prefix[i] = k
    return prefix


def main():
    file = open("prefix.in", "r")
    fin = file.readline().split()
    answer = find_prefix(fin[0])
    fout = open("prefix.out", "w")
    print(*answer, file=fout)


if __name__ == '__main__':
    main()
