/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

// This is my introduction to C++, not to be taken literally or in reference
// to the rest of this class. Simply in experiment on an existing repo for myself.

#include <iostream>

using namespace std;

int main()
{
    string el = "Hello world!";
    string lo = "enterprise";
    
    // a small integer value
    int test = 11;
    // a large integer value
    long ficl = 1012314214152151;
    // float can have the decimal wherever
    float te = 10.101111111112;
    // double limits to six places after the decimal
    double oee = 222210.0010201333333333;
    
    // an array example
    int ckint[3] = { 4, 4, 4};
    
    while (lo != "e")  {
     
        // print to console example with casting
        cout << el << to_string(oee);

        // for loop example
        for (int i = 0; i < sizeof(ckint) / sizeof(int); i++) { cout << ckint[i]; }

        // input from console example
        cin >> lo;

    
   
    }

    return 0;
    
}
