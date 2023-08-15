//ways to climb nth stairs
#include<iostream>
#include <cmath>
using namespace std;
int findWays(int n){
    if(n<=0){           // base case
        return 0;         
    }
    if(n==1){      //base
        return 1;
    }
    if(n==2){       //base
        return 2;
    }
    return findWays(n-1)+findWays(n-2);           //recursive step
}
int n;
int main(){
    cout<<"Enter no of steps ";cin>>n;
    cout<<"No of ways to climb "<<n<<" steps= "<<findWays(n);  
    return 0;
}