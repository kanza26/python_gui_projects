//ways to climb nth stairs
#include<iostream>
#include <cmath>
using namespace std;
int findWays(int n){
    if(n<=0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    if(n==2){
        return 2;
    }
    return findWays(n-1)+findWays(n-2);
}
int n;
int main(){
    cout<<"Enter no of steps ";cin>>n;
    cout<<"No of ways to climb "<<n<<" steps= "<<findWays(n);  
    return 0;
}