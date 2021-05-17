#include <iostream>


using namespace std;


int main() {

    int n, m, request;
    int l, r, l1, r1, mediana, fl = 0, mediana1;
    freopen("binsearch.in", "r", stdin);
    freopen("binsearch.out", "w", stdout);
    cin >> n;
    int array[n];
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    cin >> m;
    for (int i = 0; i < m; i++) {
        l = l1 = -1;
        r = r1 = n;
        fl=0;
        cin >> request;
        while (r > l + 1) {
            mediana = (l + r) / 2;
            if (array[mediana] >= request) {
                r = mediana;
            } else {
                l = mediana;
            }


        }
        while (r1 > l1 + 1) {
            mediana1 = (l1 + r1) / 2;
            if (array[mediana1] > request) {
                r1 = mediana1;
            } else {
                l1 = mediana1;
            }
        }
        if (l==l1 && r==r1){
            cout << -1 << " " << -1 << endl;

        }
        else{
            cout << r + 1 << " " << r1 << endl;
        }
        

    }


}