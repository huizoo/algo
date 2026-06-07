#include <iostream>
using namespace std;

int main() {
    cout << fixed;
    cout.precision(2);
    int age, cnt = 0;
    double total = 0;
    while (true) {
        cin >> age;
        if (age >= 20 && age < 30) {
            total += age;
            cnt += 1;
        } else break;
    }
    cout << total / cnt;
    return 0;
}