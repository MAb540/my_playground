#include <string>
#include <iostream>
#include <vector>

using namespace std;


// ****
// *  *
// *  *
// *  *
// ****

// using loops
void fifteenStarPattern(int n){    
    int s = 2 * n - 1;
    cout<<s<<endl<<endl;
    int to = s/2;
   
    for(int i=0; i<to; i++){
        int m=n;
        for(int j=0; j < i; j++){
            cout<<m<<" ";
            m -=1;
        }
         for (int k = 0; k < s - 2 * i; k++) {
            cout << n - i << " ";
        }

        m = n-i+1;
        for(int l=0; l < i; l++){
            cout<<m<<" ";
            m +=1;
        }
        cout<<endl;
    }
}

// using recursion
// void fifteenStarPattern(int start, int n){

//     if(start > n){
//         return;
//     }
//     int ascii_of_a = 65 + n-start;
//     for(int i=1; i<=start; i++){
//         cout<<(char)ascii_of_a<<"";   
//         ascii_of_a +=1;
//     }
//     cout<<endl;
//     fifteenStarPattern(start+1,n);
// }

// void thirteenStarPattern(int n){
//     if(n==0){
//         return;
//     }

//     int ascii_of_a = 65;
//     for(int i=1; i<=n; i++){
//         cout<<(char)ascii_of_a<<"";
//         ascii_of_a +=1;   
//     }
//     cout<<endl;
//     thirteenStarPattern(n-1);
// }


int main(){

    fifteenStarPattern(3);
    cout<<endl;
    return 0;
}

// ****
// *  *
// *  *
// *  *
// ****

// using loops
// void fifteenStarPattern(int n){    
//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=n-1; j++){   
//             if(j==1|| j==n-1 || i==1 || i==n){
//                 cout<<"*";
//             }else{
//                 cout<<" ";
//             }
//         }
//         cout<<endl;
//     }
// }

// *        *
// **      **
// ***    ***
// ****  ****
// **********
// ****  ****
// ***    ***
// **      **
// *        *
// using loops
// void fifteenStarPattern(int n){   
        
//     for(int i=1; i<=n; i++){

//         for(int j=1; j<=i; j++){
//             cout<<"*";
//         }
//         for(int k=1; k <= (n*2) - (i*2); k++){
//             cout<<" ";
//         }
//         for(int l=1; l<=i; l++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }

//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=n-i; j++){
//             cout<<"*";
//         } 
//         for(int k=1; k <=i*2; k++){
//             cout<<" ";
//         }
//         for(int m=1; m<=n-i;m++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
// }

// **********
// ****  ****
// ***    ***
// **      **
// *        *
// *        *
// **      **
// ***    ***
// ****  ****
// **********

// using loops
// void fifteenStarPattern(int n){   
    
//     for(int i=1; i<=n; i++){
//         for(int j=i; j<=n; j++){
//             cout<<"*";
//         } 
//         for(int k=1; k <=i*2; k++){
//             if(k>2){
//             cout<<" ";
//             }

//         }
//         for(int m=i; m<=n;m++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
    
//     for(int i=1; i<=n; i++){

//         for(int j=1; j<=i; j++){
//             cout<<"*";
//         }
//         for(int k=1; k <= (n*2) - (i*2); k++){
//             cout<<" ";
//         }
//         for(int l=1; l<=i; l++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }

// }

// E  
// D E
// C D E 
// B C D E
// A B C D E
// using loops
// void fifteenStarPattern(int n){   
//     int ascii_of_a = 65 + n;
//     for(int i=1; i<=n; i++){
//         ascii_of_a -= i;
//         for(int j=1; j<=i; j++){
//             cout<<(char)ascii_of_a<<"";
//             ascii_of_a +=1;
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void fifteenStarPattern(int start, int n){

//     if(start > n){
//         return;
//     }
//     int ascii_of_a = 65 + n-start;
//     for(int i=1; i<=start; i++){
//         cout<<(char)ascii_of_a<<"";   
//         ascii_of_a +=1;
//     }
//     cout<<endl;
//     fifteenStarPattern(start+1,n);
// }


//     A    
//    ABA
//   ABCBA
//  ABCDCBA

// using loops
// void fourteenStarPattern(int n){   
//     for(int i=1; i<=n; i++){
//         for(int s=1; s<=n-i; s++){
//             cout<<" ";
//         }

//         int ascii_of_a = 65;
//         for(int j=1; j<=i; j++){
//             cout<<(char)ascii_of_a<<"";
//             ascii_of_a +=1;
//         }

//         ascii_of_a = ascii_of_a - 2; 
//         for(int k=1; k < i; k++){
//             cout<<(char)ascii_of_a<<"";
//             ascii_of_a = ascii_of_a -1;
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void fourteenStarPattern(int start, int n){

//     if(n == 0){
//         return;
//     }
//     fourteenStarPattern(1,n-1);
//     int ascii_of_a = 65;
//     for(int i=1; i<=n; i++){
//         cout<<(char)ascii_of_a<<"";
//         ascii_of_a +=1;
//     }
//     ascii_of_a -= 2;
//     for(int j=1; j<=n-1; j++){
//         cout<<(char)ascii_of_a<<"";
//         ascii_of_a -=1;
//     }
//     cout<<endl;
// }

//  A    
//  BB
//  CCC
//  DDDD
//  EEEE

// using loops
// void fourteenStarPattern(int n){  
//     int ascii_of_a = 65;
//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=i; j++){
//             cout<<(char)ascii_of_a<<"";
//         }
//         ascii_of_a +=1;
//         cout<<endl;
//     }
// }

// using recursion
// void fourteenStarPattern(int start,int ascii_of_a, int n){
//     if(start > n){
//         return;
//     }
//     for(int i=1; i<=start; i++){
//        cout<<(char)ascii_of_a << "";
//     }
//     cout<<endl;
//     ascii_of_a +=1;
//     fourteenStarPattern(start+1,ascii_of_a,n);
// }

//  A    
//  AB     
//  ABC
//  ABCD
//  ABCDE

//  ABCDE
//  ABCD
//  ABC
//  AB
//  A
// using loops
// void thirteenStarPattern(int n){  
    
//     for(int i=1; i<=n; i++){
//         int ascii_of_a = 65;
//         for(int j=1; j<=i; j++){
//             cout<<(char)ascii_of_a << "";
//             ascii_of_a +=1;
//         }
//         cout<<endl;
//     }

//     cout<<endl;
//     for(int i=0; i < n; i++){
//         int ascii_of_a = 65;
//         for(int j=0; j <  n-i; j++){
//             cout<<(char)ascii_of_a << "";
//             ascii_of_a +=1;
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void thirteenStarPattern(int start, int n){

//     if(start > n){
//         return;
//     }

//     int ascii_of_a = 65; 
//     for(int i=1; i<=start; i++){
//        cout<<(char)ascii_of_a << "";
//        ascii_of_a +=1;
//     }
//     cout<<endl;
//     thirteenStarPattern(start+1,n);
// }

// void thirteenStarPattern(int n){
//     if(n==0){
//         return;
//     }

//     int ascii_of_a = 65;
//     for(int i=1; i<=n; i++){
//         cout<<(char)ascii_of_a<<"";
//         ascii_of_a +=1;   
//     }
//     cout<<endl;
//     thirteenStarPattern(n-1);
// }


//  1    
//  2 3    
//  4 5 6
//  7 8 9 10
//  11 12 13 14 15

// using loops
// void twelthStarPattern(int n){
//     int record = 1;
//     for(int i=1; i<=n; i++){
//         for(int j=record; j<record + i; j++){
//             cout<<j<<" ";
//         }
//         record = record +i;
//         cout<<endl;
//     }
// }

// using recursion
// void twelthStarPattern(int start,int n,int record){
//     if(start > n){
//         return;
//     }
//     for(int i=record; i < record+start; i++){
//         cout<<i<<" ";
//     }
//     cout<<endl;
//     record = record+start;
//     twelthStarPattern(start+1,n,record);
// }


//  1      1
//  12    21
//  123  321
//  12344321

// using loops
// void eleventhStarPattern(int n){
//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=i; j++){
//             cout<<j;
//         }
//         for(int k=i+1; k<=(n+n)-i; k++){
//             cout<<" ";
//         }
//         for(int l=i; l>=1; l--){
//             cout<<l;
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void eleventhStarPattern(int start,int n){

//     if(start > n){
//         return;
//     }
//     for(int i=1; i<=start; i++){
//         cout<<i;
//     }
//     for(int j=start+1; j<=(n+n)-start; j++){
//         cout<<" ";
//     }
//     for(int k=start; k>=1; k--){
//         cout<<k;
//     }
//     cout<<endl;
//     eleventhStarPattern(start+1,n);
// }

//  1
//  0 1
//  1 0 1
//  0 1 0 1
//  1 0 1 0 1

// using loops
// void eleventhStarPattern(int n){
//     for(int i=1; i<=n; i++){
//         for(int j=i; j >= 1; j--){
            // if(j%2 != 0){
            //     cout<<"1 ";                
            // }else{
            //     cout<<"0 ";
            // }
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void eleventhStarPattern(int n){
    
//     if(n==0){
//         return;
//     }
//     eleventhStarPattern(n-1);
//     for(int i=n; i>=1; i--){
//         if(i%2 != 0){
//                 cout<<"1 ";                
//         }else{
//                 cout<<"0 ";
//             }
//     }
//     cout<<endl;
//}


//  *
//  **
//  ***
//  ****
//  *****
//  ******
//  *****
//  ****
//  ***
//  **
//  *

// using loops
// void tenthStarPattern(int n){
//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=i; j++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
//     for(int i=n-1; i>=1; i--){
//         for(int j=i; j>=1; j--){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
// }

// using recursion
// void tenthStarPatternUpperPartOfDiamond(int n){
//     if(n == 0){
//         return;
//     }
//     tenthStarPatternUpperPartOfDiamond(n-1);

//      for(int i=1; i <=  n; i++){
//         cout<<"*";
//     }
//     cout<<endl;
// }

// void tenthStarPatternLowerPartOfDiamond(int n){

//     if(n == 0){
//         return;
//     }
//     for(int i=n-1; i>=1; i-- ){
//         cout<<"*";
//     }
//     cout<<endl;
//     tenthStarPatternLowerPartOfDiamond(n-1);

// }


//     *
//    ***
//   *****
//  *******
// *********
// *********
//  *******
//   *****
//    ***
//     *

// using loops
// void nineStarPattern(int n){
//     for(int i=1;  i <= n; i++){
//       for(int j=1; j <= n-i; j++){
//           cout<<" ";
//       }  
//       for(int k=1; k <= (i*2)-1; k++){
//           cout<<"*";
//       }
//       cout<<endl;
//     }
    
//     for(int i=n; i>0; i--){
//         for(int j=0; j < n-i ; j++){
//             cout<<" ";
//         }
//         for(int k=1; k <= (i*2)-1; k++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
// }

// using recursion

// void nineStarPatternUpperPartOfDiamond(int lower_bound, int n){

//     if(lower_bound > n){
//         return;
//     }

//     for(int i=1; i <= n-lower_bound; i++){
//         cout<<" ";
//     }
//     for(int j=0; j<(2*lower_bound)-1; j++){
//         cout<<"*";
//     }
//     cout<<endl;
//     nineStarPatternUpperPartOfDiamond(lower_bound+1,n);
// }

// void nineStarPatternLowerPartOfDiamond(int upper_bound,int n){
//     if(upper_bound == 0){
//         return;
//     }
//     for(int i=n; i >  upper_bound; i--){        
//         cout<<' ';
//     }
//     for(int j=0; j < (2 * upper_bound) - 1; j++){
//         cout<<'*';
//     }
//     cout<<endl;
//     nineStarPatternLowerPartOfDiamond(upper_bound-1, n);
// }

// *********
//  *******
//   *****
//    ***
//     *

// using loops
// void eigthStarPattern(int n){
//     for(int i=n;  i > 0; i--){

//       for(int j=n; j > i; j--){
//           cout<<" ";
//       }  

//       for(int k=1; k <= (i*2)-1; k++){
//           cout<<"*";
//       }
//       cout<<endl;
//     }
//     cout<<endl;   
// }

// using recursion
// void eigthStarPattern(int upper_bound,int n){

//     if(upper_bound == 0){
//         return;
//     }

//     for(int i=n; i >  upper_bound; i--){        
//         cout<<' ';
//     }
//     for(int j=0; j < (2 * upper_bound) - 1; j++){
//         cout<<'*';
//     }
//     cout<<endl;
//     eigthStarPattern(upper_bound-1, n);
// }



//     *
//    ***
//   *****
//  *******
// *********
// using loops
// void seventhStarPattern(int n){
//     for(int i=0; i < n; i++){      

//         for(int j=0; j<n-1-i; j++){
//             cout<<" ";            
//         }

//         for(int k=0; k < (i+1) + i; k++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
//     cout<<endl;   
// }

// using recursion
// void seventhStarPattern(int lower_bound,int n){
//     if(lower_bound >= n){
//         return;
//     }
//     for(int i=1; i < n - lower_bound; i++){        
//         cout<<' ';
//     }
//     for(int j=0; j < (lower_bound+1) + lower_bound; j++){
//         cout<<'*';
//     }
//     cout<<endl;
//     seventhStarPattern(lower_bound+1,n);
// }

// 12345
// 1234
// 123
// 12
// 1
// using loops
// void sixthStarPattern(int n){
//     for(int i=0; i < n; i++){        
//         for(int j=1; j <= n-i; j++){
//             cout<<j;
//         }
//         cout<<endl;
//     }
//     cout<<endl;   
// }

// using recursion
// void sixthStarPattern(int n){
//     if(n==0){
//         return;
//     }
//      for(int i=1; i<=n; i++){        
//         cout<<i;
//      }
//     cout<<endl;
//     sixthStarPattern(n-1);
// }



// ***
// **
// *

// using loops
// void fifthStarPattern(int n){
//     for(int i=1; i<=n; i++){        
//         for(int j=i; j<=n; j++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
//     cout<<endl;   
// }

// using recursion
// void fifthStarPattern(int n){

//      if(n==0){
//          return;
//      }
//      for(int i=1; i<=n; i++){        
//         cout<<"*";
//     }
//     cout<<endl;   
//     fifthStarPattern(n-1);
// }


// 1
// 22
// 333
// using loop
// void fourStarPattern(int n){

//     cout<<endl;
//     for(int i=1; i<=n; i++){        
//         for(int j=1; j<=i; j++){
//             cout<<i;
//         }
//         cout<<endl;
//     }   
// }

// using recursion
// void fourStarPattern(int n){

//     if(n==0){
//         return;
//     }
//     fourStarPattern(n-1);
//     for(int i=1; i<=n; i++){        
//         cout<<n;
//     }
//     cout<<endl;   
// }





// 1
// 12
// 123
// using loops
// void thirdStarPattern(int n){
//     for(int i=1; i<=n; i++){
//         for(int j=1; j<=i; j++){
//             cout<<j;
//         }
//         cout<<endl;
//     }
// }
// using recursion
// void thirdStarPattern(int n){

//     if(n == 0){
//         return;
//     }
//     thirdStarPattern(n-1);
//     for(int i=1; i<=n; i++){
//         cout<<i;
//     }   
//     cout<<endl;
// }


// *
// **
// ***
// using loops
// void secondStarPattern(int n){
//     cout<<endl;
//     for(int i=0; i<n; i++){

//         for(int j=0; j<=i; j++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }

// }

// using recursion
// void secondStarPattern(int n){

//     if(n==0){
//         return;
//     }
//     secondStarPattern(n-1);
//     for(int i=0; i<n; i++){
//        cout<<"*";
//     }
//     cout<<endl;
// }


// *****
// *****
// *****
// using loops
// void firstStarPattern(int n){
//     cout<<endl;
//     for(int i=0; i<n; i++){

//         for(int i=0; i<n; i++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }

// }

// using recursion
// void firstStarPattern(int start, int n){

//     if(start >= n){
//         return;
//     }
//     for(int i=1; i<=n; i++){
//         cout<<"*";
//     }
//     cout<<endl;
//     firstStarPattern(start+1,n);
// }

