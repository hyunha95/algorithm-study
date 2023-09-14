import re

S = input()

nums = re.split(r'[-+]', S)
operators = list(filter(lambda x: x != '', re.split(r'[0-9]', S)))

minusStatus = False
answer = int(nums[0])
for i in range(0, len(nums) - 1):
    if operators[i] == "-" or minusStatus:
        answer -= int(nums[i + 1])
        minusStatus = True
    elif not minusStatus:
        answer += int(nums[i + 1])

print(answer)
