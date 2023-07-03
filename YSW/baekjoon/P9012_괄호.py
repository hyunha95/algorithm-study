n = int(input())

for i in range(0, n):
    s = input()
    lst = []

    # list가 0일때 pop을 할 수 없으므로 해당 boolean 값을 False로 변경하여 관리
    flag = True

    for alphabet in s:
        if alphabet == '(':
            lst.append(1)
        else:
            if len(lst) == 0:
                flag = False
                break
            else:
                lst.pop()
    if (len(lst) == 0) & flag:
        print('YES')
    else:
        print('NO')
