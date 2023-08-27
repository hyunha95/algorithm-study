import sys
n = int(sys.stdin.readline())
crane = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

m = int(input())
box = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

minutes = 0

if crane[0] < box[0]:
    print(-1)
    sys.exit()
else:
    while box:
        for c in crane:
            if box and c < box[-1]:
                continue
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        minutes += 1

print(minutes)
