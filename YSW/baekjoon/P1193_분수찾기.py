# 몇 번째 분수를 찾을지 입력받는다.
number = int(input())

# 위의 number를 핸들링 할것이므로 최초 입력받은 번째수를 저장해둠
saved_number = number

# 몇 번째 행에 있는지 저장하는 변수
index = 0

# number가 0보다 클 때까지 index에 1을 더한 후 number에서 빼준다.
# ex1) 4 => 4 - 1 - 2 - 3 < 2 ==> index = 3
# ex2) 10 => 10 - 1 - 2 - 3 - 4 = 0 ==> index = 4
# ex3) 14 => 14 - 1 - 2 - 3 - 4 - 5 < 0 ==> index = 5
while number > 0:
    index = index + 1
    number = number - index

# 1/1. 2/1 (1+2=3)번째. 1/3(1+2+3=6)번째. 4/1(1+2+3+4=10)번째 ...
# 즉 분모나 분자가 n인 마지막 번째 분수는 1/n(홀수) 혹은 n/1(짝수)일 때이고 해당 번째 수는 (1+2+3+...+n)번째이므로
# 해당 줄을 찾을때 유용할 것이라 판단했다.
summation = 0

# 1부터 index까지 더한 값을 summation에 저장한다.
for i in range(1, index + 1):
    summation = summation + i

# 해당 분수가 index 줄 몇번째에 있는지 확인하기 위한 변수 j
j = summation - saved_number

# 가장 큰 값이 index 이므로 index에서 j를 빼주는 변수 p
# ex) index = 5이면 분자/분모의 최대 크기는 5이므로
p = index - j

# 가장 작은 값이 1 이므로 1에서 j를 더하는 변수 q
q = 1 + j

# 홀수 혹은 짝수에 따라 p, q의 위치를 바꿔서 출력해줌
if index % 2 == 0:
    print(str(p) + "/" + str(q))
else:
    print(str(q) + "/" + str(p))

# ex) n = 14
# index = 5, summation = 15
# j = 15(summation) - 14(n) = 1, p = 5 - 1 = 4, q = 1 + 1 = 2
# index가 홀수이므로 q/p가 정답임. answer = 2 / 4
