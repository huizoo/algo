#include <iostream>
using namespace std;

int main() {
    int a, b, c, total;
    cin >> a >> b >> c;
    total = a + b + c;
    cout << total << '\n';
    cout << total / 3 << '\n';
    cout << total - total / 3;
    return 0;
}