#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    char c;
    cin >> s >> c;
    if (s.find(c) != string::npos) {
        cout << s.find(c);
    } else cout << "No";
    return 0;
}