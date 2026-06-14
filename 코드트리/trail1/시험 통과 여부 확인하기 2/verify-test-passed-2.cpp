#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, total, cnt=0;
    cin >> n;
    vector<int> arr(n);
    for (int i=0; i<n; i++) {
        total = 0;
        for (int i=0; i<4; i++) {
            cin >> arr[i];
            total += arr[i];
        }
        if (total/4 >= 60) {
            cout << "pass\n";
            cnt += 1;
        } else cout << "fail\n";
    }
    cout << cnt;
    return 0;
}