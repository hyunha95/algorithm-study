T = int(input())

for _ in range(T):
    s = input()
    array = []
    for i in s:
        if i == '(': # ( 가 나왔다면
            array.append(i) # 스택에 추가 해준다.
        elif i == ')' and len(array) > 0: # )가 나왔는데 array에 괄호가 있다면
            if array[-1] == '(': # 스택에서 마지막 문자가 (일 경우에만
                array.pop() # 짝이 맞으므로 빼준다.
            else: # 마지막 문자가 ) 라면
                break # 반복문 탈출
        elif i == ')' and len(array) == 0: # )이고 array에 (가 없다면
            array.append(i) # array에 추가

    if len(array) == 0:
        print("YES")
    else:
        print("NO")