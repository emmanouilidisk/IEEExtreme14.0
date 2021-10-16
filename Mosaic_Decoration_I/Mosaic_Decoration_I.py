import math
inp = list(map(int,input().split()))
ts = inp[0]
cb = inp[1]
cp = inp[2]
# print(ts)
# print(cb)
res = 0
bt = 0
pt = 0
for i in range(ts):
    tiles = list(map(int,input().split()))
    bt  = bt + tiles[0]
    pt  = pt + tiles[1]
tbt = math.ceil(bt/10)
tpt = math.ceil(pt/10)
print(tbt*cb+tpt*cp)
    
