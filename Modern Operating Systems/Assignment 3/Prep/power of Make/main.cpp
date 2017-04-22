/*
Demonstrating makefile working 
here only exceutes files in which changes have been made not other files
Here main calls factorial() and print_hello()
Functions.h has declaration of the two functions.
function1.cpp has factorial defination
fucntion2.cpp has print_hello  definiton
*/

#include<iostream>
#include "functions.h"
int main()
{
	print_hello();
	std::cout << std::endl;
	std::cout << "The factorial of 5 is " << factorial(5) << std::endl;
	return 0;
}
