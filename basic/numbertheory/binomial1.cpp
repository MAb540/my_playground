#include <iostream>
#include <string.h>

using namespace std;

int factorial(int x){
    int fact = 1;
    for(int i=x; i>=1; i--){
        fact *=i;
    }
    return fact;
}

int factorialUsingRecursion(int x,int sum){

    if(x==1){
        return sum;
    }
    sum *= x;
    return factorialUsingRecursion(x-1,sum);
}

void valueOfBinomialCoefficient(int n, int k){
    int factOfN = factorialUsingRecursion(n,1);
    int factOfK = factorialUsingRecursion(k,1); 
    int factOfNminusK = factorialUsingRecursion(n-k,1);

    // int factOfN = factorial(n);
    // int factOfK = factorial(k); 
    // int factOfNminusK = factorial(n-k);

    int ans = factOfN/(factOfK * factOfNminusK);
    cout<<ans<<endl;
}

int binomialCoefficient(int n, int r){
    if (r > n){
        return 0;
    }
    if((r == 0) || (n == r)){
        return 1;
    }
    return binomialCoefficient(n-1,r-1) + binomialCoefficient(n-1,r);
}

int binomialCoeffUsingDP(int n, int k){

    int dpArray[n+1][k+1];
    for(int i=0; i<=n; i++){
        for(int j=0; j<=k; j++){
            dpArray[i][j]=0;
        }
    }

    for(int i=0; i<=n; i++){
        for(int j=0; j<=i; j++){
            if(j==0 || j==i){
                dpArray[i][j] = 1;
            }
            else{
                dpArray[i][j] = dpArray[i-1][j-1] + dpArray[i-1][j];
            }
        }
    }
    cout<<endl;
    return dpArray[n][k];
}

int bionomialCoffiUsingMemset(int n, int k){

    int C[k+1];
    // // both doing same thing,(filling array 'C' with 0's)
    memset(C,0,sizeof(C));
    C[0] = 1;

    for(int i=1; i<=n; i++){
        for(int j=min(i,k); j>0; j--){
            C[j] = C[j] + C[j-1];
        }
    }
    for(const auto& c: C){
        cout<<c<<endl;
    }

    return C[k];
}

int binomialCoefficientUsingSingleArray(int n, int r){

    int arr[r+1];
    for(int i=0; i<=r; i++){
        arr[i] = 0;
    }
    arr[0] = 1;
    for(int i=1; i<=n; i++){
        // int ans = binomialCoefficient(n,i);
        // arr[i] = ans;
        for(int j=i; j>0; j--){
            arr[j] = arr[j] + arr[j-1];
        }
    }
    // for(const auto& a: arr){
    //     cout<<a<<" "<<endl;
    // }
    return arr[r];
}

int binomialCoefficientUsingDpoubleArray(int n, int k, int** arr){

    if(arr[n][k] != -1){
        return arr[n][k];
    }

    if(k == 0){
        arr[n][k] = 1;
        return arr[n][k];
    }
    if(k==n){
        arr[n][k] = 1;
        return arr[n][k];
    }

    arr[n][k] = binomialCoefficientUsingDpoubleArray(n-1,k-1,arr) + binomialCoefficientUsingDpoubleArray(n-1,k,arr);
    return arr[n][k];
}

void binomialCoefficientUsingDoubleArray(int n, int r){
    

    int** dp; // make a temporary lookup table
    dp = new int*[n + 1];
 
   // loop to create table dynamically
    for (int i = 0; i < (n + 1); i++) {
        dp[i] = new int[r + 1];
    }
 
   // nested loop to initialise the table with -1
    for (int i = 0; i < (n + 1); i++) {
        for (int j = 0; j < (r + 1); j++) {
            dp[i][j] = -1;
        }
    }


    cout<<binomialCoefficientUsingDpoubleArray(n,r,dp)<<endl;
}

int gcd(int a, int b){

    int min_num = min(a,b);

    while(min_num > 0){
        if(a%min_num == 0 && b%min_num == 0){
            break;
        }
        min_num--;
    }
    return min_num;

}


int main(){

    // valueOfBinomialCoefficient(4,2);
    // valueOfBinomialCoefficient(5,2);
    // cout<<binomialCoefficient(4,2)<<endl;
    // cout<<binomialCoefficient(5,2)<<endl;
    // cout<<binomialCoeffUsingDP(5,2)<<endl;
    // bionomialCoffiUsingMemset(3,3);
    // cout<<binomialCoefficientUsingSingleArray(5,2);
    // binomialCoefficientUsingDoubleArray(5,2);


    cout<<endl;
    return 0;
}