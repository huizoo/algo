#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    string arr[n];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    char a;
    cin >> a;
    int total = 0, cnt = 0;
    for (int i=0; i<n; i++) {
        if (arr[i].front() == a) {
            cnt++;
            total += arr[i].size();
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << cnt << ' ' << double(total) / cnt;
    return 0;
}