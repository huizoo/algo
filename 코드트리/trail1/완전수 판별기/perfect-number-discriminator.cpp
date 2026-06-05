#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[1001] = {0};
    for (int i=1; i<=1000; i++) {
        for (int j=2*i; j<=1000; j+=i) {
            arr[j] += i;
        }
    }
    if (arr[n] == n) cout << 'P';
    else cout << 'N';
    return 0;
}