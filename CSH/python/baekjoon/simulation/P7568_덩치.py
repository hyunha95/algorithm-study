n = int(input())
array = [0] * n

for i in range(n):
    array[i] = list(map(int, input().split()))

for i in range(n):
    rank = 1 # 기본 등수를 1로 설정
    for j in range(n):
        if(array[i][0] < array[j][0] and array[i][1] < array[j][1]): # 몸무게와 키 둘다 다른 사람보다 작은 경우에만 등수+1
            rank +=1
    print(rank, end=" ") # 등수 출력