n = int(input())
alpha = [input()   for _ in range(n)]
dic = dict()
num = 9
result = 0

for i in alpha:
    cnt=len(i)
    for j in i:
        if j not in dic:
            dic[j]=(10**(cnt-1))
        else:
            dic[j]+=(10**(cnt-1))
        cnt-=1
digit = sorted(list(dic.values()), reverse=True)

for i in digit:
    result += (num * i)
    num -= 1

print(result)
