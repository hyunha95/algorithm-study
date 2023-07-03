s = input()
N = int(s.split(' ')[0])
K = int(s.split(' ')[1])

# Initialize Array
lst = []
for i in range(1, N + 1):
    lst.append(i)

count = 0

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if lst[j - 1] == 0:
            continue

        lst[j - 1] = 0
        count += 1

        if count == K:
            print(j)
