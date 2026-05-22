#include <iostream>
using namespace std;

int main() {
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char st;
    int cnt = 0;
    cin >> st;
    for (int i=0; i<5; i++) {
        if (arr[i][2] == st || arr[i][3] == st) {
            cnt += 1;
            cout << arr[i] << endl;
        }
    }
    cout << cnt;
    return 0;
}