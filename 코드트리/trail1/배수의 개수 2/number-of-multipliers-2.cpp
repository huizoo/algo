#include <iostream>
using namespace std;

int main() {
    int n, cnt=0;
    for (int i=0;i<10;i++){
        cin >> n;
        if (n%2==1) {
            cnt += 1;
        }
    }
    cout << cnt;
    
    return 0;
}