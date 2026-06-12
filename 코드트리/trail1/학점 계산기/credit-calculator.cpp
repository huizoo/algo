#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<double> arr(n);
    double total = 0;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
        total += arr[i];
    }
    double avg = total/n;
    cout << fixed;
    cout.precision(1);
    cout << avg << '\n';
    if (avg >= 4.0) cout << "Perfect";
    else if (avg >= 3.0) cout << "Good";
    else cout << "Poor";
    return 0;
}