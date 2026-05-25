#include <iostream>
using namespace std;

int main() {
    int n, a, b, total;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> a >> b;
        total = 0;
        for (int j=a; j<=b; j++){
            if (j%2 == 0){
                total += j;
            }
        }
        cout << total << '\n';
    }
    
    return 0;
}