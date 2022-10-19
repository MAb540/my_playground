#include <iostream>
#include <vector>
#include <string>

using namespace std;

void swap(int a, int b, int *arr){
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}

void recursive(int first, int last, int *arr){
    if (first >= last){
        return;
    };
    swap(first,last,arr);
    recursive(first+1,last-1,arr);
}



int main(){


    std::cout<<"working some lenabdsfa"<<endl;

    int arr[5] = {5,4,3,2,1};
    int n= 5;
    // for(int i=0; i < 5; i++){
    //     cout<<"some output\t"<<arr[i]<<"\t\n";
    // }

    recursive(0,n-1,arr);

    // for(int i=0; i<= n/2; i++){
    //     int first = i;
    //     int last = n - 1 - i;
    //     int temp = arr[first];
    //     arr[first] = arr[last];
    //     arr[last] = temp;
    // }

    for(int i=0;  i< 5; i++){
        cout<<"some output\t"<<arr[i]<<"\t\n";
    }

    cout<<endl;
    return 0;
}