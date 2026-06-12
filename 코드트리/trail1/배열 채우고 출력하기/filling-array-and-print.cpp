#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<char> arr(10);
    for (int i=0; i<10; i++) {
        cin >> arr[i];
    }
    for (int i=arr.size()-1; i>=0; i--) {
        cout << arr[i];
    }
    return 0;
}