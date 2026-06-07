#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    bool flag = false;
    for (int i=a; i<=b; i++) {
        if (i%c==0) {
            flag = true;
            break;
        }
    }
    cout << (flag ? "NO" : "YES");
    return 0;
}