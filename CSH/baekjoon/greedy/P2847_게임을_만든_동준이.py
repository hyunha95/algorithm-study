n = int(input())
score = [int(input()) for _ in range(n)]
result = 0

# 앞 레벨의 증가 점수가 큰 경우 뒷 레벨 점수와 1 차이나게 하는게 최소한으로 하는 방법

for i in range(n-2, -1, -1): # 점수를 거꾸로 돈다. [처음 ~ 마지막 -1] ex) [5, 3, 7, 5]이면 [5, 3, 7] 만 반복문으로 돈다.
    if score[i] >= score[i+1]: # 앞에 점수가 뒤에 점수보다 크다면 앞 점수를 뒷 점수 -1 만큼 만들어 줘야 한다.
        result += (score[i] - score[i+1] + 1) # 앞점수 - 뒷점수만 하면 앞점수가 뒷 점수랑 똑같은 숫자가 되므로 1점 더 감소 시켜줘야 한다.
        score[i] = score[i+1]-1 # 현재 점수를 뒷점수 -1 숫자를 대입한다.

print(result)
