#include <iostream>
using namespace std;

void pp(int n, int m) {
    if (n == 0) return;
    for (int i=0; i<n-1; i++) {
        cout << "  ";
    }
    for (int i=0; i<m-n+1; i++) {
        cout << "@ ";
    }
    cout << '\n';
    pp(n-1, m);
    for (int i=0; i<m-n; i++) {
        cout << "@ ";
    }
    cout << '\n';
}

int main() {
    int n;
    cin >> n;
    pp(n, n);
    return 0;
}