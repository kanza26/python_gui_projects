//Question details!!!!
//A student signed up for  workshops and wants to attend the maximum number of workshops where no two workshops overlap. 
//You must do the following:
//struct Workshop having the following members:
/*The workshop's start time.
The workshop's duration.
The workshop's end time.
struct Available_Workshops having the following members:

An integer,  (the number of workshops the student signed up for).
An array of type Workshop array having size .
Implement  functions:

Available_Workshops* initialize (int start_time[], int duration[], int n)
Creates an Available_Workshops object and initializes its elements using the elements in the  and  parameters (both are of size ). Here,  and  are the respective start time and duration for the  workshop. This function must return a pointer to an Available_Workshops object.

int CalculateMaxWorkshops(Available_Workshops* ptr)
Returns the maximum number of workshops the student can attend—without overlap. The next workshop cannot be attended until the previous workshop 
ends.*/



//Solution!!!!!!!!

#include <iostream>
#include <algorithm>                       //included this headerfile to use sort function
using namespace std;
int count=0;
struct workshop{
    int stime;
    int duration;
    int etime;
};
struct AvailableWorkshop{
    int NoOfworkshop;
    workshop* arr;                           // pointer to an array of datatype workshop
};
bool compareWorkshops(workshop w1,workshop w2) {          // the object of datatype AvailableWorkshop has an array which contain objects of datatype workshop
    return w1.etime < w2.etime;
}

int CalculateMaxWorkshops(AvailableWorkshop  *obj){
    int end_time=0;
    int count=0;
    for(int i=0;i<obj->NoOfworkshop;i++){
        if(obj->arr[i].stime>end_time){
            end_time=obj->arr[i].etime;
            count=count+1;
        count=count+0;
        }
    }
    return count;
}
AvailableWorkshop  available_Workshops(int start_time[],int duration[],int n){
    AvailableWorkshop aws;
    aws.NoOfworkshop=n;
    aws.arr=new workshop[n];
    for(int i=0;i<=n;i++){
        aws.arr[i].stime=start_time[i];
        aws.arr[i].duration=duration[i];       
    }
    for(int i=0;i<=n;i++){
        aws.arr[i].etime=start_time[i]+duration[i];
        aws.arr[i].etime=start_time[i]+duration[i];       
    }
    sort(aws.arr,aws.arr + n,compareWorkshops); // the object of datatype AvailableWorkshop has an array which contain objects of datatype workshop
    return aws;
}

int main() {
    int x;
    
    cout<<"Enter no of workshops"<<endl;
    cin>>x;
    int *start_time=new int[x];
    int *duration=new int[x];
    for(int y=0;y<x;y++){
        cout<<"Enter start time of "<<y+1<<" conference"<<endl;
        cin>>start_time[y];
    }
    for(int y=0;y<x;y++){
        cout<<"Enter duration of "<<y+1<<" conference"<<endl;
        cin>>duration[y];
    }
    
    AvailableWorkshop myobj=available_Workshops(start_time,duration,x);
    int a= CalculateMaxWorkshops(&myobj);
    cout<<a;
    delete[] myobj.arr;  // Clean up memory allocated using new
    return 0;
}
