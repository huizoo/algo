#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a/b << '.';
    a = (a%b)*10;
    for (int i=1; i<21; i++) {
        cout << a/b;
        a = (a%b)*10;
    }
    return 0;
}