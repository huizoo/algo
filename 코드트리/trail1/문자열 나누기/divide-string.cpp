#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    string st, tot;
    for (int i=0; i<n; i++) {
        cin >> st;
        tot += st;
    }
    for (int i=0; i<tot.length(); i++) {
        cout << tot[i];
        if (((i+1)%5)==0) cout << '\n';
    }
    return 0;
}