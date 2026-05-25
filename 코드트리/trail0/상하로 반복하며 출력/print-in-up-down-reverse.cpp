#include <iostream>
using namespace std;

int main() {
    int n, num;
    cin >> n;
    int arr[n][n];
    for (int j=0; j<n; j++){
        num = 0;
        if (j%2 == 0) {
            for (int i=0; i<n; i++) {
                num += 1;
                arr[i][j] = num;
            }
        } else {
            for (int i=n-1; i>=0; i--) {
                num += 1;
                arr[i][j] = num;
            }
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++){
            cout << arr[i][j];
        }
        cout << '\n';
    }
    return 0;
}