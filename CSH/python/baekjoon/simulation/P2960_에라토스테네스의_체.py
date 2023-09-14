# 한번에 모든 수가 지워지지 않는다면 2번단계로 다시 돌아가야하기 때문에 재귀로 풀었음

n, k = map(int, input().split())
num = [] # 2부터 N까지의 숫자가 담길 배열
remove = [] # 지워진 숫자가 담길 배열

# 2부터 N 까지 모든 정수를 넣는다.
for i in range(2,n+1):
    num.append(i)

# 재귀 함수 작성
def solution(arr) :
    minNum = min(arr) # 가장 작은 수를 찾는다.
    for i in arr:
        if (i % minNum == 0): # 가장 작은수의 배수라면
            num.remove(i) # 배열에서 해당 숫자 삭제
            remove.append(i) # 지운 수 배열에 방금 삭제한 숫자를 삽입  

    if(len(arr) != 0): # 숫자가 담인 배열의 길이가 0이 안됐다면 위에 과정들을 반복하기 위해 재귀함수를 호출한다=
        solution(arr)

solution(num) # 함수 실행
print(remove[k-1]) # k 인덱스에 맞는 숫자 출력