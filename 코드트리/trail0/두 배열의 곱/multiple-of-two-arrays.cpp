#include <iostream>
using namespace std;

int main() {
    int arr[3][3] = {0}, arr2[3][3] = {0};
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            cin >> arr[i][j];
        }
    }
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            cin >> arr2[i][j];
        }
    }
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            cout << arr[i][j] * arr2[i][j] << ' ';
        }
        cout << '\n';
    }   
    return 0;
}