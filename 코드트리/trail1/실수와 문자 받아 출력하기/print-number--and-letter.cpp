#include <iostream>
using namespace std;

int main() {
    char c;
    double a, b;
    cin >> c >> a >> b;
    cout << fixed;
    cout.precision(2);
    cout << c << '\n' << a << '\n' << b;
    return 0;
}