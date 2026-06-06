#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int answer = 1;
    for (int i=0; i<b; i++) {
        answer *= a;
    }
    cout << answer;
    return 0;
}