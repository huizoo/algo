#include <iostream>
using namespace std;

int main() {
    int n, cnt3=0, cnt5=0;
    for (int i=0;i<10;i++) {
        cin >> n;
        if (n%3==0) cnt3 += 1;
        if (n%5==0) cnt5 += 1;
    }
    cout << cnt3 << ' ' << cnt5;
    return 0;
}