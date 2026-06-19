#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<char> arr = {'L', 'E', 'B', 'R', 'O', 'S'};
    char a;
    cin >> a;
    int n = -1;
    for (int i=0; i<6; i++) {
        if (a == arr[i]) {
            n = i;
        }
    }
    if (n==-1) {
        cout << "None";
    } else cout << n;
    return 0;
}