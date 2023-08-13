N = int(input())

numbers = [0,1,2,3,4,5,6,7,8,9]
words = []
for _ in range(N):
    words.append(list(input().zfill(10)))

words = list(zip(*words))

print(words)

