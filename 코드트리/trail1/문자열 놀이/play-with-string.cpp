#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int q;
    cin >> s >> q;
    int t;
    for (int i=0; i<q; i++) {
        cin >> t;
        if (t==1) {
            int a, b;
            cin >> a >> b;
            char temp = s[a-1];
            s[a-1] = s[b-1];
            s[b-1] = temp;
            cout << s << '\n';
        } else {
            char a, b;
            cin >> a >> b;
            for (int i=0; i<s.size(); i++) {
                if (s[i] == a) {
                    s[i] = b;
                }
            }
            cout << s << '\n';
        }
    }
    return 0;
}