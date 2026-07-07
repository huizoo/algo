#include <iostream>
#include <string>
using namespace std;

int main() {
    string st1, st2;
    getline(cin, st1);
    getline(cin, st2);
    for (int i=0; i<st1.length(); i++) {
        if (st1[i] != ' ') {
            cout << st1[i];
        }
    }
    for (int i=0; i<st2.length(); i++) {
        if (st2[i] != ' ') {
            cout << st2[i];
        }
    }
    return 0;
}