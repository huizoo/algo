#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int m, total=0;
    for (int i=0; i<n; i++) {
        cin >> m;
        if (m%2==1 && m%3==0) {
            total += m;
        }
    }
    cout << total;
    return 0;
}