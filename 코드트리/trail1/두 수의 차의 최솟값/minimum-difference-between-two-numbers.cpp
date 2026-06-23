#include <iostream>
using namespace std;

int main() {
    int n, prev, now, gap;
    cin >> n;
    prev = -100;
    gap = 99;
    for (int i=0; i<n; i++) {
        cin >> now;
        if ((now-prev) < gap){
            gap = now-prev;
        }
        prev = now;
    }
    cout << gap;
    return 0;
}