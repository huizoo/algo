#include <iostream>
using namespace std;

int main() {
    int b, a;
    cin >> b >> a;
    while (a <= b) {
        if (a%2==0) {
            cout << b << ' ';
            b -= 2;
        } else {
            b -= 1;
        }
    }
    return 0;
}