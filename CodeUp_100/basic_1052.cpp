/*
 두 정수(a, b)를 입력받아
 a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
 */

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int a, b;
    bool result;
    cin >> a >> b;
    
    result = a != b;
    cout << result;
}
