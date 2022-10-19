#include <bits/stdc++.h>
#include <iostream>


using namespace std;

// bool canVisit(int i, int j, int &m[][]){
//     if(m[i][j] == 1){
//         return true;
//     }
//     return false;
// }


void dfsRatInAMaze(int i, int j, vector<vector<int>> &m, int n, vector<vector<int>> &visit, vector<string> &ans){

    if(i == n-1 && j== n-1){
        for(auto d: ans){
            cout<<d<<" ";
        }
        cout<<endl;
        return;
    }

    // down
    if(i+1 < n && !visit[i+1][j] && m[i+1][j] == 1){
        ans.push_back("D");
        visit[i+1][j] = 1;
        dfsRatInAMaze(i+1,j,m,n,visit, ans);     
        visit[i+1][j] = 0;
        ans.pop_back(); 
    }
     
    // left          
    if(j-1 >= 0 && !visit[i][j-1] &&  m[i][j-1] == 1){
        ans.push_back("L");
        visit[i][j-1] = 1;
        dfsRatInAMaze(i,j-1,m,n,visit, ans);     
        visit[i][j-1] = 0;
        ans.pop_back(); 
    }
         
        // right
        if(j+1 < n && !visit[i][j+1] && m[i][j+1] == 1){
            ans.push_back("R");
            visit[i][j+1] = 1;
            dfsRatInAMaze(i,j+1,m,n,visit, ans);     
            visit[i][j+1] = 0;
            ans.pop_back(); 
        }

        // up
        if(i-1 >= 0 && !visit[i-1][j] && m[i-1][j] == 1){
            ans.push_back("U");
            visit[i-1][j] = 1;
            dfsRatInAMaze(i-1,j,m,n,visit, ans);  
            visit[i-1][j] = 0;
            ans.pop_back();      
        } 
    
}


int main(){


    string ab = "aabb";

    // cout<<ab[0]<<endl;
    // cout<<ab[1]<<endl;

    // cout<<ab.substr(0,0)<<endl;
    // cout<<ab.substr(1,2)<<endl;
    // cout<<ab.substr(1)<<endl;

    int n = 4;
    vector<vector<int>> m  = {{1,0,0,0},{1,1,0,1},{1,1,0,0},{0,1,1,1}};
    vector<vector<int>> visit = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};


    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<m[i][j]<<" ";
        }
        cout<<endl;
    }

    vector<string> ans;
    dfsRatInAMaze(0,0,m,n,visit,ans);




    cout<<endl;
    return 0;
}


// Palindromic partitioning of a string
// bool isPalindrome(string s,int start, int end){ 
//     while(start <= end){
//         if(s[start++] != s[end--]){
//             return false;
//         }
//     }
//     return true;
// }

// void palindromePartition(int ind, string ab, vector<string> &ds){

//    if(ind == ab.size()){
//        for(auto d: ds){
//            cout<<d<<" ";
//        }
//        cout<<endl;
//        return;
//    }

//    for(int i=ind; i<ab.size(); ++i){
//        if(isPalindrome(ab,ind,i)){
//            ds.push_back(ab.substr(ind,i - ind + 1));
//            palindromePartition(i+1,ab,ds);
//            ds.pop_back();
//        }
//    } 
// }