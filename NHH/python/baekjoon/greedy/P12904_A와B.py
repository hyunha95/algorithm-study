S = input()
T = input()

while len(S) != len(T):
    char = T[-1]
    T = T[:-1]
    if char == 'B':
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)


