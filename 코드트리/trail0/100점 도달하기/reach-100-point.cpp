#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i=n; i<=100; i++) {
        if (i >= 90) {
            cout << "A\t";
        } else if (i >= 80) {
            cout << "B\t";
        } else if (i >= 70) {
            cout << "C\t";
        } else if (i >= 60) {
            cout << "D\t";
        } else {
            cout << "F\t";
        }
    }
    return 0;
}