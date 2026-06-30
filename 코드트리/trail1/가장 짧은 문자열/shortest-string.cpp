#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[3];
    for (int i=0; i<3; i++) {
        cin >> arr[i];
    }
    int max, min;
    max = min = arr[0].length();
    for (int i=1; i<3; i++) {
        if (max < arr[i].length()) {
            max = arr[i].length();
        }
        if (min > arr[i].length()) {
            min = arr[i].length();
        }
    }
    cout << max - min;
    
    return 0;
}