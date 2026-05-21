#include <iostream>
using namespace std;

int main() {
    string st;
    cin >> st;
    st[1] = 'a';
    st[st.length() - 2] = 'a';
    cout << st;
    return 0;
}