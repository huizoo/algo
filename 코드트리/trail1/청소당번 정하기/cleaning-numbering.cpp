#include <iostream>
using namespace std;

int main() {
    int n, a, b, c;
    a = b = c = 0;
    cin >> n;
    for (int i=1; i<=n; i++) {
        if (i%12==0) c+=1;
        else if (i%3==0) b+=1;
        else if (i%2==0) a+=1;
    }
    cout << a << ' ' << b << ' ' << c;
    return 0;
}