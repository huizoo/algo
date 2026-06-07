#include <iostream>
using namespace std;

int main() {
    int n;
    bool flag = false;
    for (int i=0; i<5; i++) {
        cin >> n;
        if (n%3!=0) {
            flag = true;
            break;
        }
    }
    cout << (flag ? 0 : 1);
    return 0;
}