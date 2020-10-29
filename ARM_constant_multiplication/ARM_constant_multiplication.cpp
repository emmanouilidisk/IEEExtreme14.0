#include <iostream>
#include <math.h>
#include<bits/stdc++.h>
using namespace std;
// a table that holds 2^n - 1
int table[] = {3,7,15,31,63,127,255,511,1023,2023,4096,8191,16383,32767,65535,131071,262143,524287};
int tablesize = 18;
// find the highest power of 2
int highestPowerof2(int n)
{
   int p = (int)log2(n);
   return (int)pow(2, p);
}

int binarySearch(int arr[], int l, int r, int x)
{
    while (l <= r) {
        int m = l + (r - l) / 2;

        // Check if x is present at mid
        if (arr[m] == x)
            return m;

        // If x greater, ignore left half
        if (arr[m] < x)
            l = m + 1;

        // If x is smaller, ignore right half
        else
            r = m - 1;
    }

    // if we reach here, then element was
    // not present
    return -1;
}


void Next(unsigned int x){
        unsigned int HighPower, LowPower;
        bool found = false;
        HighPower = x;
        LowPower = highestPowerof2(x);
        HighPower--;
        HighPower |= HighPower >> 1;
        HighPower |= HighPower >> 2;
        HighPower |= HighPower >> 4;
        HighPower |= HighPower >> 8;
        HighPower |= HighPower >> 16;
        HighPower++;

        if (x == HighPower){
            cout << "MOV R0, R0, LSL #" << log2(x) << "\n";
            return;
        } 
        else if (HighPower == x+1){
            cout << "RSB R0, R0, R0, LSL #" << log2(HighPower) << "\n";
            return;
        }
        else if (LowPower == x-1){
            cout << "ADD R0, R0, R0, LSL #" << log2(LowPower) << "\n";
            return;
        }
        else{
            unsigned int i;
            unsigned int other;
            for (i = 0; i < tablesize; i++ ){
                if (x%table[i] == 0) {
                    other = binarySearch(table, 0, tablesize-1, x/table[i]);
                    if (other != -1){
                        cout << "RSB R0, R0, R0, LSL #" << other+2 << "\n";
                        cout << "RSB R0, R0, R0, LSL #" << i+2 << "\n";
                        return;
                    }
                }
            }

        }
            int j = 0;
            while (x > 1) {
                if (x % 2)
                    cout << "ADD R1, R1, R0, LSL #" << j << "\n";

                j++;
                x /= 2;
            }
            cout << "ADD R0, R1, R0, LSL #" << j << "\n";
    return;
}


int main() {
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; i++) {
        unsigned int x;

        cin >> x;
        Next(x);


        cout << "END" << "\n";
    }

    return 0;
}
