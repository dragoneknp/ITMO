#include <iostream>
#include <fstream>

int main() {

    int n, m, k, l;
    std::ifstream fin("input.txt");
    std::ofstream fout("output.txt");
    fin >> n >> m;
    int array[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            array[i][j] = 0;
        }
    }
    for (int i = 0; i < m; i++) {
        fin >> k >> l;
        if ((array[k - 1][l - 1] == 1) || (array[l - 1][k - 1] == 1)) {
            fout << "YES";
            return 0;
        }
        array[k - 1][l - 1] = 1;
    }
    fin.close();
    fout << "NO";
    fout.close();
}

