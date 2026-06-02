#include <iostream>
using namespace std;

int main() {
    int n;
    int i=1;
    cin >> n;
    while (i<=n) {
        if (i%3==0) {
            cout << i << ' ';
            i += 3;
        } else {
            i++;
        }
    }
    return 0;
}