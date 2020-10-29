import copy
# update the table according to its neighbors
def update(table):
    for i in range(N):
        for j in range(N):
            if l[i][j] == 0:
                if (l[i-1][j] + l[i][j-1] + l[(i+1)%N][j] + l[i][(j+1)%N]) in liveEmpty:
                    table[i][j] = 1
                else:
                    table[i][j] = 0
            else:
                if (l[i-1][j] + l[i][j-1] + l[(i+1)%N][j] + l[i][(j+1)%N]) in liveRule:
                    table[i][j] = 1
                else:
                    table[i][j] = 0
    return table


rule_empty,rule_live = input().split(";")
liveRule = [-1]*5
liveEmpty = [-1]*5
for i in range(5):
    liveRule[i] = i if rule_live[i] == '1' else -1
    liveEmpty[i] = i if rule_empty[i] == '1' else -1

N,M = list(map(int,input().split()))
sample = N-1
l = [[0] for i in range(N)]
for i in range(N):
    l[i] = list(map(int,list(input())))

for _ in range(M):
    # create a deepcopy
    l = update(copy.deepcopy(l))
for i in range(N):
    print (''.join(map(str, l[i])))
