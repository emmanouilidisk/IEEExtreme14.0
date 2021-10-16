import math 
inp = list(map(int,input().split()))
b_width = inp[0]
b_height = inp[1]
t_width = inp[2]
t_height = inp[3]
M = inp[4]
C = inp[5]

a = math.ceil(b_width/t_width)
b = math.ceil(b_height/t_height)
c = math.ceil(a*b/10)
cuth = 0 
cutv = 0
# cuth = ((a*t_width)%b_width)*b_height
# cutv = ((b*t_height)%b_height)*b_width
if (a*t_width)%b_width!=0:
    cuth = b_height
if (b*t_height)%b_height!=0:
    cutv = b_width

cut = cuth+cutv
print(c*M+C*cut)
