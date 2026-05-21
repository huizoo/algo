#include <iostream>
using namespace std;

int main() {
    string st1, st2;
    cin >> st1 >> st2;
    int a = st1.length(), b = st2.length();
    if (a > b) {
        cout << st1 << '\t' << a;
    } else if (b > a) {
        cout << st2 << '\t' << b;
    } else {
        cout << "same";
    }
    return 0;
}