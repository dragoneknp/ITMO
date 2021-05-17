#include <iostream>
#include <fstream>
int main() {

    int n;
    bool flag=true;
    std::ifstream fin("input.txt");
    std::ofstream fout("output.txt");
    fin >> n ;
    int array[n][n];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            fin >> array[i][j];
        }
    }
    fin.close();
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            if ((array[i][j]!=array[j][i]) || (array[i][i]==1)){
                flag=false;
            }
        }
    }
    if (flag==true){
        fout << "YES";
    }
    else{
        fout << "NO";
    }
    fout.close();
}

