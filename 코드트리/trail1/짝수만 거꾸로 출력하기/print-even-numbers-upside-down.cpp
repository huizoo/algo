#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    vector<int> arr;
    for (int i=0; i<n; i++) {
        cin >> m;
        if (m%2==0) {
            arr.push_back(m);
        }
    }
    for (int i=arr.size()-1; i>=0; i--) {
        cout << arr[i] << ' ';
    }

    return 0;
}