#include <iostream>
using namespace std;

int main() {
    int n, m, cnt=0;
    int l;
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        cin >> l;
        if (l==m) cnt++;
    }
    
    cout << cnt;
    return 0;
}