#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int SUM = 0, cnt = 0;
    for (int i=a; i<=b; i++) {
        if (i%5==0 || i%7==0) {
            SUM += i;
            cnt += 1;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << SUM << ' ' << double(SUM)/cnt;
    return 0;
}