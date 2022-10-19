
#include<bits/stdc++.h>
#include <iostream>

using namespace std;

bool canColor(int node, int color[], bool graph[101][101], int n, int col){

    for(int j=0; j<n; j++){
        if(j != node && graph[j][node] && color[j] == col){
            return false;
        }
    }
    return true;

}


bool solve(int node,int color[], int m, int n, bool graph[101][101]){
    if(node == n){
        return true;
    }

   for(int i=1; i<=m; i++){

       if(canColor(node,color,graph, n, i)){
        color[node] = i;
        if(solve(node + 1,color,m,n,graph)){
            return true;
        }
        color[node] = 0;
       }

   } 
   return false;

}

// Function to determine if graph can be coloured with at most M colours such
// that no two adjacent vertices of graph are coloured with same colour.
bool graphColoring(bool graph[101][101], int m, int n){

    int color[n] = {0};
    if(solve(0,color,m,n,graph)){
        return true;
    }
    return false;
}

int main(){







    // int n = 4;
    // vector<vector<string>> ansBoard;
    // vector<string> chessBoard(n);
    // string s(n,'.');
    // for(int i=0; i<n; i++){
    //     chessBoard[i] = s;
    // }

    // vector<int> upperDiagonal(2*n,0);
    // vector<int> lowerDiagonal(2*n,0);
    // vector<int> leftArray(n,0);


    // int startCol=0;
    // nQueens(startCol,chessBoard,n,ansBoard, upperDiagonal,lowerDiagonal,leftArray);


    // for(int i=0; i<ansBoard.size(); i++){
    //     for(int j=0; j<n; j++){
    //         cout<<ansBoard[i][j]<<"\t\t\t"<<endl;
    //     }
    //     cout<<endl;
    // }





    cout <<endl;
    return 0;
}


// with out using extra loops
// void nQueens(int startCol, vector<string> &chessBoard,int n, vector<vector<string>> &ansBoard, vector<int> &upperDiagonal,vector<int> &lowerDiagonal,vector<int> &leftArray){
//     if(startCol == n){
//         ansBoard.push_back(chessBoard);
//         return;
//     }
//     for(int row = 0; row<n; row++){
//         int calc = startCol - row;
//         if(leftArray[row] == 0 && lowerDiagonal[row + startCol] == 0 && upperDiagonal[n-1 + calc] == 0){

//             chessBoard[row][startCol] = 'Q';
//             leftArray[row] = 1;
//             lowerDiagonal[row + startCol]  = 1;
//             upperDiagonal[n-1 + calc] = 1;

//             nQueens(startCol+1,chessBoard,n,ansBoard, upperDiagonal,lowerDiagonal,leftArray);

//             chessBoard[row][startCol] = '.';            
//             leftArray[row] = 0;
//             lowerDiagonal[row + startCol]= 0;    
//             upperDiagonal[n-1 + calc] = 0;
//         }
//     }
// }

// using extra loops
// bool isSafe(int row, int col,int n, vector<string> &chessBoard){

//     int tempRow = row;
//     int tempCol = col;

//     // upper diagonal
//     while (tempRow >= 0 && tempCol >= 0){
//         if(chessBoard[tempRow][tempCol] == 'Q'){
//             return false;
//         }
//         tempRow--;
//         tempCol--;
//     }

//     tempRow = row;
//     tempCol = col;

//     while(tempCol >= 0){
//         if(chessBoard[row][tempCol] == 'Q'){
//             return false;
//         }
//         tempCol--;
//     }

//     tempRow = row;
//     tempCol = col;

//     while(tempRow < n && tempCol >= 0){
//         if(chessBoard[tempRow][tempCol] == 'Q'){
//             return false;
//         }
//         tempRow++;
//         tempCol--;
//     }
//     return true;
// }

// void nQueens(int startCol, vector<string> &chessBoard,int n, vector<vector<string>> &ansBoard){
//     if(startCol == n){
//         ansBoard.push_back(chessBoard);
//         return;
//     }
//     for(int row = 0; row<n; row++){
//         if(isSafe(row,startCol,n,chessBoard)){
//             chessBoard[row][startCol] = 'Q';
//             nQueens(startCol+1,chessBoard,n,ansBoard);
//             chessBoard[row][startCol] = '.';    
//         }
//     }
// }

// void printAllPermutationsWithOutUsingExtraSpace(int ind,int arr[], int n){
//     if(ind == n){
//         for(int i=0; i<n; i++){
//             cout<<arr[i]<<" ";
//         }
//         cout<<endl;
//         return;
//     }

//     for(int i=ind; i<n; i++){
//         int temp = arr[ind];
//         arr[ind] = arr[i];
//         arr[i] = temp;
//         printAllPermutationsWithOutUsingExtraSpace(ind + 1,arr, n);
//         int t = arr[i];
//         arr[i] = arr[ind];    
//         arr[ind] = t;
//     }
// }


// void printAllPermutationsUsingExtraSpace(int arr[], int n, vector<int> &ds, vector<bool> &freq_array){
//     if(ds.size() == n){
//         for(auto d: ds){
//             cout<<d<<" ";
//         }
//         cout<<endl;
//         return;
//     }

//     for(int i=0; i<n; i++){
//         if(freq_array[i] == false){
//             ds.push_back(arr[i]);
//             freq_array[i] = true;
//             printAllPermutations(0,arr, n, ds, freq_array);
//             ds.pop_back();
//             freq_array[i] = false;
//         }
//     }
// }



// The Subset Sum, (print the sum of all the subsets of any array) 
// void printSubsetSum(int ind, int arr[], int n, int sum, vector<int> &ds){
//     if(ind == n){
//         ds.push_back(sum);
//         for(auto d: ds){
//             cout<<d<<" ";
//         }
//         cout<<endl;
//         return;
//     }
//     printSubsetSum(ind + 1, arr, n, sum + arr[ind], ds);
//     printSubsetSum(ind + 1, arr, n, sum, ds);
// }


// The Power Sum
// int powerSum(int total, int num, int power){
//     int ans = total - pow(num,power);
//     if (ans < 0){
//         return 0;
//     }
//     if (ans == 0){
//         return 1;
//     }
//     return powerSum(ans,num,power+1) + powerSum(total,num,power+1);
// }

// int total = 10;
// int num = 2;
// cout<<powerSum(total,num,1);

// The combination sum
// void combinationSum(int ind,vector<int> &array, vector<int> &ds, int target){
//     if(target == 0){
//         for(auto d: ds){
//             cout<<d<<" ";
//         }
//         cout<<endl;
//         return;
//     }
    
//   for(int i=ind; i<array.size(); i++){
//       if(i > ind && array[i] == array[i-1]){
//           continue;
//       }
//       if(array[i] <= target){
//           ds.push_back(array[i]);
//           combinationSum(i+1, array,ds,target - array[i]);  
//           ds.pop_back();
//       }
//   }  
// }

// int superDigit(int digit){
//     if(digit >= 0 && digit < 10){
//         return digit;
//     }
//     int sum = 0;
//     string tempps = to_string(digit);
//     for(int i=0; i<tempps.length(); i++){
//         string s = tempps.substr(i,1);   
//         int a = std::stoi(s);
//         sum += a;
//     }
//     int ans = superDigit(sum);; 
//     return ans;
// }