#include <iostream>

using namespace std;

int main() {
    //get input
    int N,counter,differences;
    cin >> N;
    string codes[N];
    counter = 0;
    for(int i=0;i<N;i++){
        cin >> codes[i];
    }
    //compare the characters of each two different coupons
    //and increase counter if differences=1 
    for(int j=0;j<N-1;j++){
        for(int k=j+1;k<N;k++)   {
            differences = 0;
            for(int l=0;l<codes[j].size();l++) {
                if(codes[j][l] != codes[k][l]) differences += 1;
            }
            if(differences==1) counter +=1;
        } 
    }
    cout << counter;
    return 0;
}