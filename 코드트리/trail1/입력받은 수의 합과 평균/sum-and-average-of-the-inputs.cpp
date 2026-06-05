#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int m, total = 0, cnt = 0;
    for (int i=0; i<n; i++) {
        cin >> m;
        total += m;
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << total << ' ' << double(total)/cnt;
    return 0;
}
