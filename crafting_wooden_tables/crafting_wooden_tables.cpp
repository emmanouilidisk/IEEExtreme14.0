#include <iostream>

using namespace std;
typedef long long ll;

int main() {
    ll wood_for_table,slot_capacity,slots,woods;
    cin >>  wood_for_table >> slots >> slot_capacity >> woods;
    if(wood_for_table > woods) cout << 0;
    else cout << woods / wood_for_table;
    return 0;
}