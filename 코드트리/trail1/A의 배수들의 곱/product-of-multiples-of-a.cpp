#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int ans = 1;
    for (int i=1; i<=b; i++) {
        if (i%a==0) {
            ans *= i;
        }
    }
    cout << ans;
    return 0;
}