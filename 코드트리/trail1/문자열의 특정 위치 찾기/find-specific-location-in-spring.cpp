#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    char c;
    cin >> s >> c;
    int idx = -1;
    for (int i=0; i<s.length(); i++) {
        if (s[i] == c) {
            idx = i;
            break;
        }
    }
    if (idx != -1) {
        cout << idx;
    } else cout << "No";
    return 0;
}