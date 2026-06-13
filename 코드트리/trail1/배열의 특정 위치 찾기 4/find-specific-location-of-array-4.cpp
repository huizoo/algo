#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr(10);
    int total = 0, cnt = 0;
    for (int i=0; i<=10; i++) {
        cin >> arr[i];
        if (arr[i] == 0) {
            break;
        }
        if (arr[i]%2 == 0) {
            total += arr[i];
            cnt += 1;
        }
    }
    cout << cnt << ' ' << total;
    return 0;
}