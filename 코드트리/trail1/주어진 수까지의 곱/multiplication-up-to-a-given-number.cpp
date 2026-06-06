#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int m = 1;
    for (int i=a; i<=b; i++) {
        m *= i;
    }
    cout << m;
    return 0;
}