#include <iostream>
using namespace std;

int main() {
    int total, cnt;
    total = cnt = 0;
    int n;
    for (int i=0; i<10; i++) {
        cin >> n;
        if (n>=0 && n<=200) {
            total += n;
            cnt++;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << total << ' ' << double(total)/cnt;
    return 0;
}