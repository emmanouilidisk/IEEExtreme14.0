N,T = list(map(int,input().split()))

#create list with ones on indexes equal to input numbers
#and zeros elsewhere
init_list = [0 for i in range(T)]
for i in input().split():
    init_list[int(i)] = 1
    
#compare init_list with rotations of init_list
#and count the number of rotated lists that are equal to the initial list    
counter = 0
for i in range(1,T):
    num = 0
    for j in range(0,N):
        if(init_list[j-i] != init_list[j]):
            break
        else:
            num += 1
    if(num == N):
        break
    else:
        counter += 1
print(counter)   
