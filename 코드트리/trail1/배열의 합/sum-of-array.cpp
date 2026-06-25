#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> arr(4, vector<int>(4));
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> arr[i][j];
        }
    }
    int sum;
    for (int i=0; i<4; i++) {
        sum = 0;
        for (int j=0; j<4; j++) {
            sum += arr[i][j];
        }
        cout << sum << '\n';
    }
    return 0;
}