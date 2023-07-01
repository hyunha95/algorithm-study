import sys

word = sys.stdin.readline().rstrip()
q = []
result = ''
flag = False  # 괄호가 나왔을 경우 True / 괄호 밖인 경우 False

for i in word:
    if i == '<':
        while q: # 괄호가 나왔을 경우 괄호 전까지 삽입된 문자가 남아 있다면 거꾸로 꺼내서 result에 넣어준다.
            result += q.pop() # 거꾸로 꺼냄
        flag = True # 괄호가 나왔다는 표시를 해준다.

    elif i == '>': # 닫는 괄호가 나왔다면
        flag = False # 괄호가 끝났다는 표시를 해준다.
        result += '>' # result에 더해준다.
        continue

    if flag: # 괄호가 열렸다면
        result += i # 뒤집을 필요가 없기 때문에 문자 순서대로 result에 더해준다.
    else: # 괄호가 닫힌상태 또는 괄호가 없다면
        if i == ' ': # 문자가 공백이라면
            while q: # 그 전까지 삽입된 문자열을 거꾸로 result에 더해준다.
                result += q.pop()
            result += ' ' # 다 더해준 후 공백을 더해준다 (공백은 위치 고정)
        else : # 문자가 공백이 아니라면
            q.append(i) # 리스트에 문자를 계속해서 삽입해준다.

if (len(q) != 0): # 맨 끝이 일반 문자인 경우에는 q(리스트)에 남아있게돼서 마저 거꾸로 뺴줘서 result에 더해준다.
    while q:
        result += q.pop()

print(result) # result 출력
