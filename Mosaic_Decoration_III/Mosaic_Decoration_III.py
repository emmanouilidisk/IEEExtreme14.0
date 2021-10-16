import math
inp = list(map(int,input().split()))
N_rows = inp[0]
M_col = inp[1]
R_rows = inp[2]
C_col = inp[3]
costs = []
for i in range(R_rows):
    costs.append(input().split())
# print(costs)'
a = math.ceil(N_rows/R_rows)
b = math.ceil(M_col/C_col)
if (a*R_rows)%N_rows != 0:
    pass
if (b*C_col)%M_col !=0:
    pass
R_C_cost = 0
tiles = a*b
for i in costs:
    for j in i:
        R_C_cost+=int(j)
print(a*b*R_C_cost)