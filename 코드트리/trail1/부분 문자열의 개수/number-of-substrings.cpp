#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    int l = b.length();
    int cnt = 0;
    for (int i=0; i<a.length()-l+1; i++) {
        if (a.substr(i, l) == b) {
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}