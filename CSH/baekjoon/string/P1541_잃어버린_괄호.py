import sys
num = []

# -가 있는 경우에는 - 뒤에 나오는 숫자들을 다 빼줘야 제일 작은 숫자가 나온다.
# -가 있다면 -뒤로 나오는 숫자들을 다 더해주기 위해 -로 split
expression = sys.stdin.readline().rstrip().split('-')  # 55-50+40 --> ['55', '50+40']

for exp in expression:
    plus = exp.split('+') # 55 , [50, 40]
    temp = 0

    for number in plus:
        temp += int(number) # +로 나눠진 값들에 대해서는 다 더해준다. (55 - (50+40)) 일때가 가장 작다.
    num.append(temp) # (55 - (90))을 해주기 위한 과정

result = num[0] # num = [55,90] 이 담겨 있게 된다.

for i in range(1,len(num)):
    result -= num[i] # num에 있는 값들을 다 빼준다. (-로 split을 했기 때문에 빼줘야 한다.)

print(result)





