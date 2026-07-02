#include <iostream>
#include <string>
using namespace std;

int main() {
    string st1;
    char ch1;
    getline(cin, st1);
    cin >> ch1;
    int cnt = 0;
    for (int i=0; i<st1.length(); i++) {
        if (st1[i] == ch1) {
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}