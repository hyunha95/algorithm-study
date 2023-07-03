s = input()
N = int(s.split(' ')[0])
K = int(s.split(' ')[1])

lst = []
# Initialize Array
for i in range(1, N + 1):
    lst.append(i)

count = 1
result = []
while len(lst) > 0:
    if count % K == 0:
        result.append(lst[0])
        lst.pop(0)
    else:
        lst.append(lst[0])
        lst.pop(0)
    count += 1

# 결과값 출력 Format 맞추기
print_result = '<'
for i in result:
    print_result += str(i) + ', '
print_result = print_result[:-2]
print_result += '>'

print(print_result)