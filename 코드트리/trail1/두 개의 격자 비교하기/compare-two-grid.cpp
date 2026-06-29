#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int arr[n][m];
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> arr[i][j];
        }
    }
    int l;
    int arr2[n][m];
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> l;
            arr2[i][j] = (arr[i][j] == l) ? 0 : 1;
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cout << arr2[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}