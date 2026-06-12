#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<double> arr(10);
    int total, cnt;
    total = cnt = 0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (arr[i] >= 250) break;
        total += arr[i];
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << total << ' ' << double(total)/cnt;

    return 0;
}