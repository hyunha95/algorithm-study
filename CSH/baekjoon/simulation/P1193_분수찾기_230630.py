x = int(input())
end = 0 # 그 라인의 마지막 값
line=0 # 라인

while x > end : # 입력 받은 값이 그 라인의 마지막 값 보다 큰 경우에 반복 실행
    line += 1 # 라인 1개 증가
    end += line # 라인 만큼 더해준다. (1라인엔 1, 2라인의 끝값은 3, 3라인의 끝 값은 6...)

diff = end - x # 라인의 끝 값과 입력 받은 값의 차이를 구한다.

# 라인의 끝 값을 기준으로 계산한다.
if line % 2 == 0:
    print(line -diff, "/", diff+1, sep='')
else :
    print(diff+1, "/", line -diff, sep='')
