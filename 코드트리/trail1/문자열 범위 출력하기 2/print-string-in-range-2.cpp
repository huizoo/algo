#include <iostream>
#include <string>
using namespace std;

int main() {
    string st1;
    cin >> st1;
    int a;
    cin >> a;
    if (st1.length() < a) {
        for (int i=0; i<st1.length(); i++) {
            cout << st1[st1.length()-i-1];
        }
    } else {
        for (int i=0; i<a; i++) {
            cout << st1[st1.length()-i-1];
        }
    }
    return 0;
}