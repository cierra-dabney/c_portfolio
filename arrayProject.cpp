/*

Author: Cierra Dabney
Date: 09/02/2024
Description: This program generates an array of random integers, calculates their sum and average,
			 and displays the results. The user first inputs the array size, then the program fills the 
			 array with random numbers between -200 and 199. It calculates the total sum and average of 
			 the array elements and prints them, along with the array itself. Shows understanding of functions 
			 handling array loading, sum calculation, and printing, demonstrates basic array manipulation 
			 and pointer use.
*/

#include<iostream>//input/output
#include<stdlib.h>//allows for random numbers
#include<time.h>//allows for time
using namespace std;

//loadArray function loads array with random numbers by using srand, a loop, and pointer
void loadArray(int *arr, int size) {
    srand(time(0));  // seed for the random number 
    for (int i = 0; i < size; i++) {
        *(arr + i) = (rand() % 400) - 200; // random numbers between -200 and 199
    }
}

//calculateSum funtion calculates the sum of elements in the array by looping through arr
//void function because there was no need to return a value to main
void calculateSum(int *arr, int size, int &sum) {
    sum = 0;
    for (int i = 0; i < size; i++) {
        sum += *(arr + i);
    }
}

//calculateAvergae function calculates the average of the elements by having
//calculateSum called on the inside to return the average found through the function
double calculateAverage(int *arr, int size) {
    int sum;
    calculateSum(arr, size, sum); // calls the calculateSum function
    //static_cast used for the conversion between types int --> double for the variable sum
    return static_cast<double>(sum) / size; // returns the average
}

//printArray function prints the array elements through a loop with spaces seperating
void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << "   "; // prints each element separated by 3 spaces
    }
    cout << endl;
}

int main(){
	
	int arySize, sum;
	int *bigArray;
	
	//input elements into the array
	cout << "Enter the size of the array: " << endl;
	cin >> arySize;
	cout <<"Array list with requested size: " << endl;
	bigArray = new int[arySize];
	loadArray(bigArray, arySize);
	printArray(bigArray, arySize);
	
	//calculate sum and avergae
	calculateSum(bigArray, arySize, sum);
	double average = calculateAverage(bigArray, arySize);
	
	//output sum and average
	cout << "Sum of the array elements: " << sum << endl;
	cout << "Average of the array elements: " << average << endl;

	return 0;
}


