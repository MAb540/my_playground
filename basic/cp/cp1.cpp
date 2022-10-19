#include <iostream>
#include <set>
#include <string>
#include <math.h>
using namespace std;

#define MAX  500

bool isPrime(int n){
    bool prime = true;
    for(int i=2; i<=sqrt(n); i++){
        if(n%i == 0){
            prime=false;
            break;
        }
    }
    return prime;
}

int main(){

    int n=12;

    for(int i=2; i<=sqrt(n); i++){
        if(n%i == 0){

            int quotient = n/i;
            if(isPrime(i)){
                cout<<i<<endl;
            }
            if(isPrime(quotient)){
                cout<<quotient<<endl;
            }
        }
    }


    // int n = 316;
    // while(n%2 == 0){
    //     cout<<2<<" ";
    //     n=n/2;
    // }

    // for(int i=3; i<=sqrt(n); i++){
    //     while(n%i == 0){
    //         cout<<i<<" ";
    //         n=n/i;
    //     }
    // }

    // int num;
    // cin>>num;

    // int arr[MAX];

    // // filling array in reverse
    // int i=0;
    // while (num > 0){
    //     arr[i] = num%10;
    //     num = num/10;
    //     i++;
    // }
    // cout<<endl;


    // int s;
    // cin>>s;
    
    // string abc = "abc";

    // int len = abc.size();

    // for(int i=1; i<= len; i++){
    //     for(int j=0; j <= len-i; j++){
    //         for(int k=j; k<=j+i-1; k++){
    //             cout<<abc[k];
    //         }
    //         cout<<endl;
    //     }
    // }
    cout<<endl;
    return 0;
}


    // factors of a number
    // int n = 12;
    // for(int i=1; i<=sqrt(n); i++){
    //     if(n%i == 0){
    //         cout<<i<<endl;
    //         /** secondFactor is the quotient(the number by which we multiply) of i*/
    //         int secondFactor =(n/i);
    //         cout<<secondFactor<<endl;
    //     }
    // }