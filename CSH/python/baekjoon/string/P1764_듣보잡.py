# 처음에 list로 풀었더니 시간초과 나서 교집합 풀이로 변경
import sys

n , m = map(int, sys.stdin.readline().split())
set1 = set()
set2 = set()

for i in range(n):
    set1.add(sys.stdin.readline().rstrip())

for i in range(m):
    set2.add(sys.stdin.readline().rstrip())

array = list(set1 & set2) # 교집합
array.sort() # 사전 순으로 정렬

print(len(array)) # 길이 출력
print('\n'.join(array)) # 이름 출력
