from itertools import *

def solution(s, N):
    numbers = []
    for i in range(1, N+1):
        numbers.append(str(i))

    numbers = list(permutations(numbers, N))
    print(numbers)

    arr = []
    for number in numbers:
        number = ''.join(number)
        if number in s:
            arr.append(number)


    answer = int(max(arr)) if len(arr) > 0 else -1
    return answer


print(solution("1451232125", 2))
print(solution("313253123", 3))