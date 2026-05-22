#include <iostream>
using namespace std;

int main() {
    int a = 0;
    while (true) {
        cin >> a;
        if (a > 25) {
            cout << "Lower\n";
        } else if (a < 25) {
            cout << "Higher\n";
        } else {
            cout << "Good";
            break;
        }
    }
    
    return 0;
}