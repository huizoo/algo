#include <iostream>
#include <string>
using namespace std;

int main() {
    string st, st2;
    cin >> st;
    for (int i=1; i<st.length(); i+=2) {
        st2 += st[i];
    }
    for (int i=st2.length()-1; i>=0; i--) {
        cout << st2[i];
    }
    return 0;
}