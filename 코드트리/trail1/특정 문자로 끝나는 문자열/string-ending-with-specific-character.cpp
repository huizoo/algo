#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10];
    char ch;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
    }
    cin >> ch;
    int cnt = 0;
    for (int i=0; i<10; i++) {
        if (arr[i].back() == ch) {
            cout << arr[i] << '\n';
            cnt++;
        }
    }
    if (cnt == 0) {
        cout << "None";
    }
    return 0;
}