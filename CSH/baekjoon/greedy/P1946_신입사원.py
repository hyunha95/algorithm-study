import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(input())
    array = []
    count = 1 #  성적 1위는 무조건 합격이라서 count를 1로 초기화

    for _ in range(n):
        array.append(list(map(int,sys.stdin.readline().rstrip().split())))

    array.sort() # 서류 심사 성적을 기준으로 순위 오름차순 정렬 (면접 순위만 비교하기 위해서)

    score = array[0][1] # 서류 1등의 면접 성적
    for i in range(1, n): # 서류 2등부터 비교
        num = array[i][1] # 서류 1등을 제외한 다른 지원자들의 면접 순위

        if score > num: # 서류 성적은 이미 밀렸기 때문에 면접 순위는 더 높아야 한다 (num이 더 작다는 말은 앞의 지원자보다 면접 순위가 높다는 뜻)
            count += 1 # 앞에 뽑힌 사람보다 면접 순위가 높다면 뽑힌다
            score = num # 뽑힌 사람의 면접 순위 기록 (앞에서 뽑힌 사람한텐 이미 서류 성적순으로 밀렸기 때문에 면접 순위가 높아야 하기 때문에 뽑힌 사람의 면접 순위를 기록)

    print(count)




