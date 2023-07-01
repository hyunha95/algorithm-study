# 입력받을 갯수를 input으로 받음
num = int(input())

# 앞으로 입력할 element를 담을 list를 선언
lst = []

for i in range(0, num):
    element = int(input())

    # 입력받은 값에 따른 구분
    if element == 0:
        lst.pop()
    else:
        lst.append(element)

# result
print(sum(lst))