N, M =  list(map(int,input().split()))
coin_comb = [["Zulian","Razzashi","Hakkari"],
             ["Sandfury","Skullsplitter","Bloodscalp"],
             ["Gurubashi","Vilebranch","Witherbark"]]

inp = [input().split() for x in range(M)]

g0 = [0, 0, 0]
g1 = [0, 0, 0]
g2 = [0, 0, 0]

for i in range(M):
    if inp[i][0] == coin_comb[0][0]:
        g0[0] += int(inp[i][1])
    elif inp[i][0] == coin_comb[0][1]:
        g0[1] += int(inp[i][1])
    elif inp[i][0] == coin_comb[0][2]:
        g0[2] += int(inp[i][1])
    elif inp[i][0] == coin_comb[1][0]:
        g1[0] += int(inp[i][1])
    elif inp[i][0] == coin_comb[1][1]:
        g1[1] += int(inp[i][1])
    elif inp[i][0] == coin_comb[1][2]:
        g1[2] += int(inp[i][1])
    elif inp[i][0] == coin_comb[2][0]:
        g2[0] += int(inp[i][1])
    elif inp[i][0] == coin_comb[2][1]:
        g2[1] += int(inp[i][1])
    elif inp[i][0] == coin_comb[2][2]:
        g2[2] += int(inp[i][1])

if min(g0)+min(g1)+min(g2) < N:
    print("impossible")
