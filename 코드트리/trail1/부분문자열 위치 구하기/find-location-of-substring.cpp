#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;
    if (s1.find(s2) != string::npos) {
        cout << s1.find(s2);
    } else cout << -1;
    return 0;
}