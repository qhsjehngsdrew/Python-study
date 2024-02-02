#include <iostream>
using namespace std;

int facto(int n)
{
	int ft;
	return n ==1 ? 1 : n * facto(n - 1);
}

int main()
{ 
	cout << facto(4);
}