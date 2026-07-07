#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10];
    int total = 0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        total += arr[i].length();
    }
    cout << total;
    
    return 0;
}