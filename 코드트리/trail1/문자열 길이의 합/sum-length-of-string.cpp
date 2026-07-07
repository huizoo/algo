#include <iostream>
#include <string>
using namespace std;

int main() {
    int N, total=0, cnt=0;
    cin >> N;
    string arr[N];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
        total += arr[i].length();
        if (arr[i][0] == 'a') {
            cnt++;
        }
    }
    cout << total << ' ' << cnt;
    return 0;
}