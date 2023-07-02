N = int(input())

white_paper = [[0]*100 for _ in range(100)]
# print(white_paper)

arr = []
for i in range(0, N):
    x, y = map(int, input().split())
    arr.append([x, y])

count = 0
for element in arr:
    for i in range(0, 10):
        for j in range(0, 10):
            if white_paper[element[0] + i][element[1] + j] == 0:
                white_paper[element[0] + i][element[1] + j] = 1
                count += 1

# for a in white_paper:
#     print(a)

print(count)