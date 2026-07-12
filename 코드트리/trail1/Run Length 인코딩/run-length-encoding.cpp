#include <iostream>
#include <string>
using namespace std;

int main() {
    string st;
    cin >> st;
    
    string ans;

    int i = 0;

    while (i < st.length()) {
        char ch = st[i];
        int cnt = 0;

        while (i < st.length() && st[i] == ch) {
            cnt++;
            i++;
        }

        ans += ch;
        ans += to_string(cnt);
    }

    cout << ans.length() << '\n' << ans;
    
    return 0;
}