N, K = input().split()

cards = ["2","3","4","5","6","7","8","9","X","J","Q","K","A"]
commun = {}
mine = {}
impossible = False
total = 0

for i in cards:
    commun[i] = -1
    mine[i] = 0
    
deck = input()
moves = input()

for i in range(int(N)):
    if moves[i] == "n":
        if commun[deck[i]] == 0:
            impossible = True
            break
        else:
            commun[deck[i]] = 0
    elif commun[deck[i]] == -1:
        commun[deck[i]] = 1
        mine[deck[i]] = 1
        total += 1
    elif commun[deck[i]] >= 1:
        commun[deck[i]] += 1
        
if total > int(K) or impossible:
    print("impossible")
else:
    left = int(K) - total
    step = 0
    hand = ""
    
    while left:
        commun_sort = sorted(commun.items(), reverse=True, key=lambda x: x[1])
        
        if commun_sort[step][1] == 0:
            step += 1
        elif commun_sort[step][1] > 0 and commun_sort[step][1] + mine[commun_sort[step][0]] < 4:
            mine[commun_sort[step][0]] += 1
            left -= 1
        elif mine[commun_sort[step][0]] < 4:
            mine[commun_sort[step][0]] += 1
            left -= 1
        else:
            step += 1
        
        if step > 12:
            impossible = True
            break
        
    for i in mine:
        for j in range(mine[i]):
            hand += i
    
    if impossible:
        print("impossible")
    else:
        print(hand)