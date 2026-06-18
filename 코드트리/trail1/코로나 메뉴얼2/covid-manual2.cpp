#include <iostream>
#include <vector>
using namespace std;

int main() {
    char is_sick;
    int temp;
    int A, B, C, D;
    A = B = C = D = 0;
    for (int i=0; i<3; i++) {
        cin >> is_sick >> temp;
        if (is_sick == 'Y' & temp >= 37) A++;
        else if (is_sick == 'N' & temp >= 37) B++;
        else if (is_sick == 'Y' & temp < 37) C++;
        else D++;
        
    }
    cout << A << ' ' << B << ' ' << C << ' ' << D;
    if (A>=2) cout << ' ' << 'E';
    return 0;
}