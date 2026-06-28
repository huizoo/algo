#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    cout << fixed;
    cout.precision(1);
    vector<vector<int>> arr(2, vector<int>(4));
    for (int i=0; i<2; i++) {
        for (int j=0; j<4; j++) {
            cin >> arr[i][j];
        }
        double sum;
        sum = accumulate(arr[i].begin(), arr[i].end(), 0);
        cout << sum/arr[i].size() << ' ';
    }
    cout << '\n';

    double total = 0;
    for (int j=0; j<4; j++) {
        double sum = 0;
        for (int i=0; i<2; i++) {
            sum += arr[i][j];
        }
        cout << sum/2 << ' ';
        total += sum;
    }
    cout << '\n';
    cout << total/8;
    return 0;
}