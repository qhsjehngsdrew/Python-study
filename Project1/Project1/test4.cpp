#include <iostream>
using namespace std;

int main() 
{
    int X, Y;
    cout << "X = ";
    cin >> X;

    cout << "Y = ";
    cin >> Y;

    for (int i = 0; i < Y; i++) 
    {
        for (int j = 0; j < X; j++) 
        {
            if (i == 0 || i == Y - 1 || j == 0 || j == X - 1) 
            {
                cout << '*';
            }
            else 
            {
                cout << ' ';
            }
        }
        cout << std::endl;
    }

    return 0;
}