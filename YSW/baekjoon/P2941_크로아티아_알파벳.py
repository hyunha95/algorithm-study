# 문자열 input을 받음
s = input()

# 크로아티아 알파벳 리스트 정의
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳이 있는 경우 a로 치환해줌
# 크로아티아 알파벳 길이를 1로 줄이는게 목적이므로 크로아티아 알파벳에 포함되지 않은 임의의 문자열로 replace 해주면 된다
for alphabet in croatian_alphabet:
    s = s.replace(alphabet, 'a')

# Solution
print(len(s))