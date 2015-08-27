/* Gaurav Mohanty */
/* 201225090 */

#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	
	string str;
	int flag_set;
	string rax,rdi,rsi,rdx,syscall;
	

	/* Replacers */
	rax="rax";	
	rdi="rdi";	
	rsi="rsi";	
	rdx="rdx"; 
	syscall="syscall";

	ifstream file("32_bit.asm"); // Take input as file stream.
	

	while (getline(file, str))
	{
		flag_set=str.find("eax, 4");
		if(flag_set!=string::npos)
			str.replace(flag_set,6,"rax, 1");

		flag_set=str.find("eax, 1");
		if(flag_set!=string::npos)
			str.replace(flag_set,6,"rax, 60");

		flag_set=str.find("int 80h");
		if(flag_set!=string::npos)
			str.replace(flag_set,syscall.length(),syscall);

		flag_set=str.find("ebx");
		if(flag_set!=string::npos)
			str.replace(flag_set,rdi.length(),rdi);

		flag_set=str.find("ecx");
		if(flag_set!=string::npos)
			str.replace(flag_set,rsi.length(),rsi);
		
		flag_set=str.find("edx");
		if(flag_set!=string::npos)
			str.replace(flag_set,rdx.length(),rdx);

		
		cout<<str<<endl;
	}
	return 0;
}