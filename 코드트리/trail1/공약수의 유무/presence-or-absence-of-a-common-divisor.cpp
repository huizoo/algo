#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    bool exist = false;
    for (int i=a; i<=b; i++) {
        if (1920%i==0 && 2880%i==0) {
            exist = true;
            break;
        }
    }
    cout << (exist ? 1 : 0);
    return 0;
}