#include <iostream>
using namespace std;

int main(){
    int N, K;
    int result = 0;
    cin >> N >> K;
    while (N != 1){
        if(N%K == 0){
            result ++;
            N = N/K;
        }
        else{
            result ++;
            N --;
        }
    }
    cout << result << endl;
}
