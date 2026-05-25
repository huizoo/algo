#include <iostream>
using namespace std;

int main() {
    int cnt, n;
    for (int i=0; i<4; i++) {
        cnt = 0;
        for (int j=0; j<4; j++) {
            cin >> n;
            cnt += n;
        }
        cout << cnt << '\n';
    }
    return 0;
}