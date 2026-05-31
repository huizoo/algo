#include <iostream>
using namespace std;

int main() {
    char a, b, c;
    int aa, bb, cc, sick;
    cin >> a >> aa >> b >> bb >> c >> cc;
    sick = 0;
    if (a == 'Y' && aa >= 37) sick += 1;
    if (b == 'Y' && bb >= 37) sick += 1;
    if (c == 'Y' && cc >= 37) sick += 1;

    if (sick >= 2) {
        cout << 'E';
    } else {
        cout << 'N';
    }
    return 0;
}