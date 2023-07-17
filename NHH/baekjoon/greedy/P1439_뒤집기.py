S = list(map(int,list(input())))

count = 1
prev = S[0]
for i in range(1, len(S)):
    if prev == S[i]:
        continue
    else:
        prev = S[i]
        count += 1

print(count // 2)