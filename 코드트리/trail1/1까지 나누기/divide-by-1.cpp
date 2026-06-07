#include <iostream>
using namespace std;

int main() {
    int n, cnt;
    cin >> n;
    cnt = 0;
    for (int i=1; i<=5001; i++) {
        n /= i;
        cnt++;
        if (n<=1) break;
    }
    cout << cnt;
    return 0;
}