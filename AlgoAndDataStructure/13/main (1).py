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


def kmp(p, t):
    answer = []
    pref = find_prefix(p + '#' + t)
    for i in range(len(pref)):
        if pref[i] == len(p):
            answer.append(i - 2 * len(p) + 1)
    return answer


def main():
    file = open("search2.in", "r")
    fin = file.readline().split()
    p = fin[0]
    fin = file.readline().split()
    t = fin[0]
    ans = kmp(p, t)
    fout = open("search2.out", "w")
    print(len(ans), file=fout)
    print(*ans, file=fout)


if __name__ == "__main__":
    main()
