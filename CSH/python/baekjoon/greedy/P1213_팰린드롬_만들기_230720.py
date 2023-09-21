# 메모리 초과
from itertools import permutations

s = list(input())
result = ''
flag = False

per_set = set(permutations(s, len(s)))
per_list = [''.join(per) for per in per_set]

per_list.sort()

for word in per_list:
    if word == word[::-1] :
        result = word
        flag = True
        break

if flag:
    print(result)
else:
    print("I'm Sorry Hansoo")