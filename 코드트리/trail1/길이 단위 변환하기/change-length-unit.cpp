#include <iostream>
using namespace std;

int main() {
    double a = 30.48;
    int b = 160934;
    cout << fixed;
    cout.precision(1);
    cout << 9.2 << "ft = " << 9.2*a << "cm\n";
    cout << 1.3 << "mi = " << 1.3*b << "cm";
    return 0;
}