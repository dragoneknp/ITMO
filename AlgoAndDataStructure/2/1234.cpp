#include <fstream>



using namespace std;

int ksort(int array[], int leftside, int rightside, int k) {

    int j = rightside, i = leftside;
    int s = (leftside+rightside)/2;
    int x = array[s];
    if (leftside==rightside) {
        return array[k];
    }
    while (i<=j) {
        while (array[i]<x){
            i++;
        }
        while (array[j]>x){
            j--;
        }
        if (i<=j) {
            swap(array[i],array[j]);
            i++;
            j--;
        }
    }
    if ((k<=j) && (leftside<=k)){
        return ksort(array,leftside,j,k);
    }
    if ((i<=k) && (k<=rightside)) {
        return ksort(array,i,rightside,k);

    }
}

int main() {
    ifstream fin("kth.in");
    ofstream fout("kth.out");

    int n, k;
    fin >> n >> k;
    int a, b, c, a1, a2;
    fin >> a >> b >> c >> a1 >> a2;

    int array[n] = {a1, a2};


    for (int i = 2; i < n; i++) {
        array[i] = a* array[i-2]+b*array[i-1]+c;



    }
    ksort(array,0,n-1,k-1);
    int answer = array[k-1];


    fout << answer ;





    fin.close();
    fout.close();
    return 0;
}