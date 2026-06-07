#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    bool found = false;
    for (int i=a; i<=b; i++) {
        if (i%c==0) {
            found = true;
            break;
        }
    }
    if (found) cout << "YES";
    else cout << "NO";
    return 0;
}