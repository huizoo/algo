#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s, tot;
    for (int i=0; i<n; i++) {
        cin >> s;
        tot += s;
    }
    cout << tot;

    return 0;
}