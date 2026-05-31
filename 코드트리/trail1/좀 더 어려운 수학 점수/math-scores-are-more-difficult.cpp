#include <iostream>
using namespace std;

int main() {
    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    if (a1 > b1) {
        cout << 'A';
    } else if (b1 > a1) {
        cout << 'B';
    } else if (b2 > a2) {
        cout << 'B';
    } else {
        cout << 'A';
    }
    return 0;
}