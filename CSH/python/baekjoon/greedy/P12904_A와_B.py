s = input()
t = input()

while t != s:
    if (len(t)==0):
        print(0)
        break

    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    else:
        print(0)
        break
else: # break를 안타고 끝났을 때 타는 조건문
    print(1)
