#include<iostream>
#include <cmath>
using namespace std;

bool checkPalindrome(string a, int start,int end){
    if(start>=end){
        return true;
    }
    if(a[start]!=a[end]){
        return false;
    }

    checkPalindrome(a,start+1,end-1);
}
int main(){
    string mystring;
    cout<<"Enter string"<<endl;
    cin>>mystring;
    int a=mystring.size();
    if(checkPalindrome(mystring,0,a-1)){
        cout<<"Palindrome"<<endl;
    }
    else{
        cout<<"Not palindrome";
    };
    return 0;
}