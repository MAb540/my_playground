#include<bits/stdc++.h>
#include <iostream>

using namespace std;


void printSubSequenceEqualToSum(int start, vector<int> &ds, int n, int arr[], int total,bool &counter){

    int ans = accumulate(ds.begin(), ds.end(), 0);
    if(ans == total){
        counter = true;   
        // for(auto d:ds){
        //     cout<<d<<" ";
        // }
        return;
    }

    cout<<endl;
    for(int i=start; i<n; i++){
        ds.push_back(arr[i]);
        printSubSequenceEqualToSum(i+1,ds,n,arr,total,counter);
        ds.pop_back();
    }


}



int main(){

    int arr[] = {1,2,3,4,5};
    int n = 5;
    vector<int> ds;
    int start=0, total = 5; 
    bool counter = false;
    printSubSequenceEqualToSum(start,ds,n,arr,total,counter);
    cout<<counter;

    cout<<endl;
    return 0;
}

// void printSubSequence(int start,int arr[],int n, vector<int> &ds){
    // for(auto it: ds){
    //     cout<<it<<" ";
    // }
    // cout<<endl;
//     for(int i=start; i<n; i++){

//         ds.push_back(arr[i]);
//         printSubSequence(i+1,arr,n,ds);
//         ds.pop_back();
//     }
// }

// void printSubSequence(int start,int arr[],int n, vector<int> &ds){
//     if(start >= n){
//         for(auto it: ds){
//             cout<<it<<" ";
//         }
//         cout<<endl;
//         return;
//     }

//     ds.push_back(arr[start]);
//     printSubSequence(start+1,arr,n,ds);

//     ds.pop_back();
//     printSubSequence(start+1,arr,n,ds);
// }

// int fibonacci(int n){

    // if(n<=1){
    //     return n;
    // }

    // return fibonacci(n-1) + fibonacci(n-2);

    // using loop
    // int n1 = 0;
    // int n2 = 1;

    // int nextNum = n1 + n2;
    // int nthFibonacci = 0;

    // for(int i=2; i<=n; i++){
    //     nthFibonacci = nextNum;

    //     n1 = n2;
    //     n2 = nextNum;
    //     nextNum = n1 + n2;
    // }
    // cout<<nthFibonacci<<endl;
    
    // another way
    // int arr[] = {0,1};
    // for(int i=2; i<=n; i++){
    //     arr[i] = arr[i-1] + arr[i-2];
    // }
    
    // for(int i=0; i<n; i++){
    //     cout<<arr[i]<<endl;
    // }
// }

// bool isStrPalindrome(string s,int start){

//     if(start >= s.length()/2){
//         return true;
//     }

//     int end = s.length() - 1 - start;
//     if(s[start] == s[end]){
//         return isStrPalindrome(s,start+1);
//     }
//     return false;
// }

// void reverseAArray(int arr[], int n,int start){
//     if(start >= n/2){
//         for(int i=0; i<n; i++){
//             cout<<arr[i]<<endl;
//         }
//         return;
//     }
//     int temp = arr[start];
//     arr[start] = arr[n-1-start];
//     arr[n-1-start] = temp;
//     reverseAArray(arr,n,start+1);
// }

// int factorialOfN(int n){
//     if(n ==1){
//         return 1;
//     }
//     return n * factorialOfN(n-1);
// }

// int sumOfFirstNNumers(int n){
//     if(n<1){
//         return 0;
//     }
//     return n + sumOfFirstNNumers(n-1);
// }

// void printFromNTillOne(int n){
//     if(n < 1){
//         return;
//     }
//     cout<<n<<endl;
//     printNameNTimes(n-1);
// }

// void printNameNTimes(int i, int n){
//     if(i>n){
//         return;
//     }
//     cout<<n<<endl;
//     printNameNTimes(i+1,n);
// }



