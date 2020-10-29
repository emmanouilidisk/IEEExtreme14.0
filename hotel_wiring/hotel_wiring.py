import numpy as np
t = int(input())

for _ in range(t):

    M, N, K = map(int,input().split())
    Hotel = np.ones((M,2))

    for i in range(M):
        Hotel[i][0] = i
        Hotel[i][1] = int(input())
    Hotel.sort(axis=0)
    ans = 0
    i = 0
    while i < K:
        ans += N - Hotel[i][1]
        i += 1
    while i < M:
        ans += Hotel[i][1]
        i += 1
    print(int(ans))
