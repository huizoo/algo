#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 10;
    vector<int> arr(n);
    for (int i=0; i<n; i++) {
        cin >> arr[i];
        if (arr[i] == 0) {n = i; break;}
    }
    int total = accumulate(arr.begin(), arr.begin()+n, 0);
    cout << fixed;
    cout.precision(1);
    cout << total << ' ' << double(total)/n;
    return 0;
}