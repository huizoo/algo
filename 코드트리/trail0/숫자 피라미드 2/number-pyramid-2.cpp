#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    m = 1;
    for (int i=0; i<n; i++) {
        for (int j=0; j<=i; j++) {
            cout << m++ << ' ';
        }
        cout << '\n';
    }
    return 0;
}