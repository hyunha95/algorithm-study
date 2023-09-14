import sys

M = int(sys.stdin.readline().rstrip())
S = set()
for i in range(0, M):
    word = sys.stdin.readline().rstrip().split()
    if len(word) == 1:
        command = word[0]
    else:
        command, num = word[0], word[1]
        num = int(num)

    if command == "add":
        S.add(num)
    elif command == "remove":
        S.discard(num)
    elif command == "check":
        print("1" if num in S else "0")
    elif command == "toggle":
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif command == "all":
        S = set([i for i in range(1, 20 + 1)])
    else:
        S = set()