#include <iostream>
using namespace std;

void abc(int now, int n) {
    for (int i=0; i<n-now; i++) {
        cout << ' ';
    }
    for (int i=0; i<now; i++) {
        cout << "* ";
    }
    cout << '\n';

    if (now >= n) return;
    
    abc(now + 1, n);
    
    for (int i=0; i<n-now; i++) {
        cout << ' ';
    }
    for (int i=0; i<now; i++) {
        cout << "* ";
    }
    cout << '\n';
}

int main() {
    int n;
    cin >> n;
    abc(1, n);
    return 0;
}