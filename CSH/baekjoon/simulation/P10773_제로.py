K = int(input())
answer = []

for _ in range(K):
    n = int(input())

    if(len(answer) != 0 and n==0) : # answer의 길이가 0이 아니고 n이 0이라면
        answer.pop() # 최근에 쓴 수를 지운다.
    else:
        answer.append(n) # n이 0이 아니라면 배열에 추가해준다.

print(sum(answer))