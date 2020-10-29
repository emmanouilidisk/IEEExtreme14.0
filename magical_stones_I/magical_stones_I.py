N = int(input())
Stones = list(map(int,input().split()))
Q = int(input())
# initialize the states
states = [i for i in range(1,N+1)]

ans = []

size = len(states)
oldsize = 100000
while True:
    for i in range(size):
        # cast the spell
        states[i] = Stones[states[i]-1]
    #sort and remove duplicates
    states = sorted(list(set(states)))
    oldsize = size
    size = len(states)
    # if nothing changed break
    if size == oldsize:
        break
    ans.append(size)


for _ in range(Q):
    K = int(input())
    try:
        c = ans.index(K) + 1
    except:
        c = -1
    print(c)
