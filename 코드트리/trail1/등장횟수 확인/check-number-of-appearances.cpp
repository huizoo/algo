#include <iostream>
using namespace std;

int main() {
    int cnt=0;
    int n;
    for (int i=0; i<5; i++) {
        cin >> n;
        if (n%2==0) cnt += 1;
    }
    cout << cnt;
    return 0;
}