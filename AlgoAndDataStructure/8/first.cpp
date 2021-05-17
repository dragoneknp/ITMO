#include <iostream>

int main() {

    int n, m, k, j;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    std::cin >> n >> m;
    int array[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            array[i][j] = 0;
        }
    }
    for (int i = 0; i < m; i++) {
        std::cin >> k >> j;
        array[k - 1][j - 1] = 1;

    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << array[i][j] << " ";

        }
        std::cout << std::endl;
    }
}
