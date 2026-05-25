#include <iostream>
using namespace std;

int main() {
    int start, end, cnt, answer = 0;
    cin >> start >> end;
    for (int i=start; i<=end; i++){
        cnt = 0;
        for (int j=1; j<=i; j++){
            if (i%j == 0){
                cnt += 1;
            }
        }
        if (cnt == 3){
            answer += 1;
        }
    }
    cout << answer;
    return 0;
}