Nof_hideouts = int(input())
hides = input().split()

soldiers = 0

for i in hides:
    soldiers += int(i)

days = int(input())
rescue = 0

for i in range(days):
    vals = input().split()
    rescue += int(vals[2])

if soldiers < rescue:
    print(soldiers)
else:
    print(rescue)