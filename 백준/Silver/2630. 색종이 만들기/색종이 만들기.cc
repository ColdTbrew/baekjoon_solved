#include <iostream>
using namespace std;
#include <vector>
vector<vector<int>> arr;
int n;
int blu=0, whi =0;
void white(int len, int x, int y){
    
    //베이직 케이스
    if(len == 1){
        if(arr[y][x] == 1) blu++;
        if(arr[y][x] == 0) whi++;
        return;
    }
    //디바이드
    int div = len/2;
    int yval = y, xval  = x;
    int initC = arr[y][x];
    for(int j = yval;j<yval + len; j++){
        for(int i = xval;i<xval+len ;i++){
            if(arr[j][i] != initC){
                goto devide;
            }
            if(j==yval + len -1 && i == xval + len -1){
                if(initC) blu++;
                else whi++;
                return;
            }
        }
    }
    devide:
    for(int j =0;j<2 ;j++){
                    for(int i = 0; i<2;i++){
                        white(div, x + div*i, y+div*j);
                    }
                }
    
}

int main(){
    cin >> n;
    int i=0, j =0;
    arr.assign(n, vector<int>(n, 0));
    for(i =0;i<n;i++){
        for(j =0;j<n;j++){
            cin >> arr[i][j];
        }
    }
    white(n, 0, 0);
    cout << whi << '\n' << blu;
   
}