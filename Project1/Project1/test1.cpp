#include <iostream>
using namespace std;

int main()
{
    int N;
    cout << "N = ";
    cin >> N;

    for (int i = 1; i < 10; i++)
        cout << N << " X " << i << " = " << N * i << endl;
    cout << endl;
}
