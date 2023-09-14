n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

dic = dict()

for n in n_arr:
    if n in dic.keys():
        dic[n] += 1
    else:
        dic[n] = 1

for m in m_arr:
    if m in dic:
        print(dic[m], end=' ')
    else:
        print(0, end=' ')