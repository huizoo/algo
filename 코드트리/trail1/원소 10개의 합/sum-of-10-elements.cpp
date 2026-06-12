#include <iostream>
using namespace std;

int main() {
    int total, n;
    total = 0;
    for (int i=0; i<10; i++) {
        cin >> n;
        total += n;
    }
    cout << total;
    return 0;
}