#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<char>> arr(5, vector<char>(3));

    for (int i=0; i<5; i++) {
        for (int j=0; j<3; j++) {
            cin >> arr[i][j];
            arr[i][j] = arr[i][j] - 'a' + 'A';
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}