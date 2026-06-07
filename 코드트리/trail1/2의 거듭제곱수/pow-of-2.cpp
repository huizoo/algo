#include <iostream>
using namespace std;

int main() {
    int x=0, n;
    cin >> n;
    while (n!=1) {
        n /= 2;
        x++;
    }
    cout << x;
    return 0;
}