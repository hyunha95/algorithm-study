# algorithm-study
알고리즘 스터디

## 패키지 구분
ㄴ사이트(백준, 프로그래머스, ...)   
&nbsp;&nbsp;ㄴ 문제 유형

## 파일명
1. 맞은 문제   
&nbsp;&nbsp;P문제번호_문제명
2. 틀린 문제   
&nbsp;&nbsp;P문제번호_문제명_yyMMdd  

### 230630
백준:     
1. 크로아티아 알파벳(2941)
2. 분수찾기(1193)
3. 덩치(7568)
4. 제로(10773)

### 230701
백준:     
1. 요세푸스 문제(1158)
2. 통계학(2108)
3. 색종이(2563)
4. 방번호(1475)
5. 재귀함수가 뭔가요?(17478)
6. 2차원 배열의 합(2167)
7. 에라토스테네스의 체(2960)

## 파이썬 문법
### - 파이썬에서 사사오입으로 반올림 처리하기
- 파이썬에서 반올림 함수 round를 사용하면 아래와 같은 결과를 확인할 수 있다.
```
print(round(0.5))   # 0 ?
print(round(1.5))   # 2
print(round(2.5))   # 2 ?
print(round(3.5))   # 4
```
- 5 미만의 숫자는 내림, 5 초과의 숫자는 올림.
- <b>반올림할 자릿수의 숫자가 5일때는 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내린다.</b>

ㄴ 해결 방법
```python
# 함수 - 1
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

# 함수 - 2
def roundHalfUp(num):
  if (num - int(num)) >= 0.5:
    return int(num) + 1
  else:
    return int(num)

# Decimal
import decimal

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

print(round(decimal.Decimal('2.5'), 0)) # 3
```
https://hleecaster.com/python-round/#:~:text=%EA%B7%B8%EB%9F%AC%EB%82%98%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%EB%8A%94%20%E2%80%9C%EC%98%A4%EC%82%AC%EC%98%A4%EC%9E%85,%EC%98%AC%EB%A6%BC%2C%20%EC%A7%9D%EC%88%98%EC%9D%B8%20%EA%B2%BD%EC%9A%B0%20%EB%82%B4%EB%A6%B0%EB%8B%A4.

### - find() vs index() # 문자열 함수
- find 함수는 문자열 중 문자가 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다. (리스트에는 존재하지 않음)
- index 함수는 문자열 중 문자가 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 오류가 발생한다.(리스트에서도 동일하게 오류 발생)

### - join
```python
a = ",".join('abcd')
print(a) # 'a,b,c,d'
```

### - remove vs del vs pop
- remove() 함수는 매개인자로 전달된 값으로 리스트의 요소를 삭제한다.(첫 번째로 나오는 값을 삭제)
```python
a = [1, 2, 3]
a.remove(2) # a = [1, 3]
```
- del a[x]는 x번째 요소값을 삭제한다. del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수이며 다음과 같이 사용한다.
```python
a = [1, 2, 3]
del a[1] # a = [1, 3]

# 슬라이싱 기법 활용
a = [1, 2, 3, 4, 5]
del a[2:] # a = [1, 2]
```
- pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
```python
a = [1, 2, 3]
print(a.pop(1)) # 2
print(a) # [1, 3]
```
-> remove는 값으로 요소 삭제. del과 pop은 인덱스로 요소를 삭제

### - extend vs append 
- extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
```python
# extend
a = [1, 2, 3]
a.extend([4, 5])
print(a) # [1, 2, 3, 4, 5]

# append
a = [1, 2, 3]
a.append([4, 5])
print(a) # [1, 2, 3, [4, 5]]
```
