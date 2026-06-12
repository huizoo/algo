#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    vector<double> arr(8);
    for (int i=0; i<8; i++) {
        cin >> arr[i];
    }
    cout << fixed;
    cout.precision(1);
    cout << accumulate(arr.begin(), arr.end(), 0.0)/8;
    return 0;
}