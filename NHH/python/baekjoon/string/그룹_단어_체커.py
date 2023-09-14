n = int(input())

arr = []
for i in range(n):
    arr.append(input())

answer = 0
for str in arr:
    answer += 1
    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            if str[i] in str[i + 1:]:
                answer -= 1
                break

print(answer)