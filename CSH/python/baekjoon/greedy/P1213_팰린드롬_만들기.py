from collections import Counter

s = list(input())
s.sort()
count = Counter(s)
odd = 0 # 홀수 개 수
odd_s = ''
result = ''

for i in count:
    if count[i] %2 != 0: # 홀수라면 odd를 늘려준다.
        odd += 1
        odd_s += i

    for _ in range(count[i] // 2) : # 양쪽 대칭이 되어야 하므로 한쪽만 먼저 구해준다. 한쪽만 구해줘야 하기 때문에 //2 를 해준다.
        result += i # 나누기 2만 만큼의 개수를 더해준다.

if odd == 0: # 홀수가 하나도 없다면 AABB면 AB만 구해주고 거꾸로 BA를 더해준다.
    print(result + result[::-1])
elif odd == 1:
    print(result + odd_s + result[::-1])
else:
    print("I'm Sorry Hansoo")
