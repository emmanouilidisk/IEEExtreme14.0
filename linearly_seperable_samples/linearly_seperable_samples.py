t = int(input())
for _ in range(t):
    n = int(input())
    dataset = [[0,0,0] for i in range(n)]
    for i in range(n):
        dataset.append(list(map(float,input().split())))
    flag1 = 0
    flag2 = 0
    x1 = dataset[0][0]
    x2 = dataset[0][1]
    for i in range(1,n):
        if(dataset[i][0] > x1 and dataset[i][1] > x2):
            flag1 = 1
        if(dataset[i][0] < x1 and dataset[i][1] < x2):
            flag2 = 1
    if(flag1 and flag2):
        print("NO")
    else:
        print("YES")
