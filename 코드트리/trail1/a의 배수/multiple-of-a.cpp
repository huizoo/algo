#include <iostream>
using namespace std;

int main() {
    int N, a;
    cin >> N >> a;
    int b = 1;
    while (b<=N) {
        if (b%a==0) {
            cout << 1;
        } else cout << 0;
        cout << '\n';
        b += 1;
    }
    return 0;
}