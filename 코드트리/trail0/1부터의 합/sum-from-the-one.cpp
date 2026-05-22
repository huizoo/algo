#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;
    for (int i=1; i<=100; i++) {
        cnt += i;
        if (cnt >= n) {
            cout << i;
            break;
        }
    }
    return 0;
}