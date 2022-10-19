#include <iostream>
#include <vector>
#include <string>

using namespace std;

// bool isPalindrome(int first, int last, string s){

//     if (first >= last){
//         return true;
//     }
    
//     if (s[first] != s[last]){
//         return false;
//     }

//     bool ans = isPalindrome(first+1,last-1,s);
//     return ans;
// }


int main(){


    // checkis if string is Palindrome
    // string s = "ABCDCBA";

    // using loop
    // bool isPalindrome = true;
    // for(int i=0; i<s.size(); i++){
    //    int p1 = i;
    //    int p2 = s.size()- 1 - i;
    //    if(s[p1] != s[p2]){
    //        isPalindrome = false;
    //         break;
    //    } 
    // }
    // cout<<isPalindrome<<endl;

    // using recursion
    // bool ans = isPalindrome(0,s.size()-1,s);
    // cout<<ans<<endl;


    // Palindrom leetcode
    // string s = "A man, a plan, a canal: Panama";
    //     bool isPalin = true;
        
    //     int p1 = 0;
    //     int p2 = s.size()-1;
    //     for(int i = 0; i<s.size(); i++){
         
            
    //       if(!isalnum(s[p1])){
    //           p1 +=1;
    //           continue;
    //       }
    //       else if(!isalnum(s[p2])){
    //           p2 -=1;
    //           continue;
    //       }
    //       else if(tolower(s[p1]) != tolower(s[p2])){
    //         isPalin = false;
    //         break;
    //       }
    //       p1 +=1;
    //       p2 -=1;
    //     }
         
    // cout<<isPalin<<endl;

    cout<<endl;
    return 0;
}


void a_square_plus_b_equation(){

        int n,m;
    cin>>n>>m;
    
    int count = 0;
    for(int a = 0; a * a <=n && a <= m; ++a){
        int b = n - a*a;
        if(a + b*b == m){
            count+=1;
        }
    }

    cout<<count;   
}


// cp codeforce 100A, 100B, 50C problems practice

// void same_num_of_ones(){
//     int n;
//     set<int> s;
//     for(int i=0; i<4; i++){
//         cin>>n;
//         s.insert(n);
//     }

//     cout<<4 - s.size()<<endl;
// }

// void same_num_of_ones(){
//     int n;
//     cin>>n;

//     int n1,n2,n3;
//     int count = 0;
//     for(int i=0; i<n; i++){
//         cin>>n1>>n2>>n3;
//         if(n1==1 && (n2 == 1 || n3==1) ){
//             count +=1;
//         }
//         else if(n2 == 1 && (n1==1 || n3==1)){
//             count +=1;
//         }
//         else if(n3==1 && (n1==1 || n2==1)){
//             count +=1;
//         }
//     }

//     cout<<count<<endl;
// }

// void perfect_permuatation(){
//         int n;
//     cin>>n;
    
//     if(n%2 == 1){
//         cout<<-1<<endl;
//     }
//     else{
//         cout<<"2 1";
//         for(int i=3; i<n; i+=2){
//             cout<<" "<<i+1<<" "<<i;
//         }
//     }
// }

// void chatWithServer(){
//      string n;
//     set<int> s;

//     cin>>n;
    
//     for(int i=0; i<n.size(); i++){
//         s.insert(n[i]);
//     }

//     if(s.size()%2 != 0){
//         cout<<"IGNORE HIM!";
//     }else{
//         cout<<"CHAT WITH HER!";
//     }
// }

