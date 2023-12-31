import sys

dic = dict() # 딕셔너리 생성
cnt = 1 # 숫자 세트 개수는 1개부터 시작

# 숫자당 카드 개수를 표현하기 위해 값을 넣어줌 (맨 처음엔 각 숫자가 1개씩 있음)
# {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}
for i in range(10):
    dic[str(i)] = 1

num = sys.stdin.readline().rstrip() # 방 번호 입력 (각 숫자 하나당 포함되어 있는지 판단해야하기 때문에 str로 입력 받음)

for i in num: # 숫자 한개씩 반복문을 돌린다.
    if(dic[i]== 0): # 해당 숫자(번호)에 맞는 개수가 0개라면
        if i=='6' and dic['9'] > 0 : # 만약 6일 경우 9를 뒤집어서 사용할 수 있기 때문에 9의 개수를 체크한다. 만약 9가 0개 이상이라면 뒤집어서 사용할 수 있다.
            dic['9'] -= 1 # 9를 뒤집어서 사용한다면 9의 개수를 -1 해줘야한다.
        elif i == '9' and dic['6'] > 0: # 9일 경우도 6과 마찬가지로 진행한다.
            dic['6'] -= 1
        else : # 6과 9가 아니라면
            cnt += 1 # 숫자 세트가 통째로 하나 더 필요하다.
            for j in range(10): # 필요한 숫자는 세트를 사자마자 다시 사용해야하므로 필요한 숫자를 제외한 숫자에게만 +1을 해준다.
                if (i != str(j)):
                    dic[str(j)] += 1
    else : # 해당 숫자에 맞는 개수가 0이 아니라면
        dic[i] -= 1 # 사용할 수 있다 (-1해준다.)

print(cnt) # 개수를 출력한다.

# 간단한 풀이 ver
# 해당 숫자가 출연한 횟수중에서 가장 큰 값이 숫자 세트의 개수
# 6과 9는 뒤집어서 사용할 수 있으므로 두 숫자의 인덱스 값을 비교하여 더 작은 인덱스의 값을 +1 시켜줌
# 배열에는 각 숫자가 등장한 수만큼 값이 있으므로 그 중에서 가장 많이 등장한 횟수가 숫자 세트의 개수이다.
num = input()
checked = [0]*10

for i in num:
    if i == '6' or i == '9':
        if checked[6] <= checked[9]:
            checked[6] += 1
        else:
            checked[9] += 1
    else:
        checked[int(i)] += 1

print(max(checked))