#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int total = 0;
    if (b>a) {
        for (int i=a; i<=b; i++) {
            if (i%5==0) {
                total += i;
            }
        }
    } else {
        for (int i=b; i<=a; i++) {
            if (i%5==0) {
                total += i;
            }
        }
    }
    cout << total;
    return 0;
}