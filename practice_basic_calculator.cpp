//creating a basic calculator using user input, variables, math functions, and data types

#include <iostream> //input output stream
#include <cmath> //allows for math
using namespace std; //allows for the cout and printing



int main()//function
{
	
//initial variables
	float num1, num2;
	
//user input
	cout<<"User welcome to the addition calculator!\n";
	
	cout<<"Enter your first value: ";
	cin>>num1;//first input value stored
	
	cout<<endl<<"Enter your second value: "<<endl;
	cin>>num2;//second input value stored
//result	
	cout<<"Result: "<<num1 + num2;
		
return 0;
}
