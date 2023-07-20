# 최대한 적게 뒤집어야 하므로 적게 나온 숫자를 뒤집는게 최소한으로 뒤집는 것
# 0001100 -> 0이 많으므로 1을 뒤집는게 최소한으로 뒤집는다

s = input() # 0001100

one_list = s.split("1")  # 1로 split을 한다 // ['000', '', '00']
one = [s for ss in one_list if s != ""] # 이 과정을 해줘야 같은 숫자가 연속으로 나왔을때 나오는 공백을 없애 줄 수 있음 // ['000', '00']

zero_list = s.split("0") # ['', '', '', '11', '', '']
zero = [s for s in zero_list if s != ""] # ['11']

l_one = len(one) # 길이 2
l_zero = len(zero) # 길이 1 --> 연속된 1을 한번 뒤집는게 최소한으로 뒤집는 횟수


print(l_zero) if l_one > l_zero else print(l_one) # one과 zero 중에 적은 횟수를 출력한다.