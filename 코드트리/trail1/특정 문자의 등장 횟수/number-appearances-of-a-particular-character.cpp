#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int cnt1, cnt2;
    cnt1 = cnt2 = 0;
    if (s.length() < 2) {
        cout << 0 << ' ' << 0;
    } else {
        for (int i=0; i+1<s.length(); i++) {
            string s2 = s.substr(i, 2);
            if (s2 == "ee") {
                cnt1++;
            }
            if (s2 == "eb") {
                cnt2++;
            }
        }
    }
    cout << cnt1 << ' ' << cnt2;
    return 0;
}