s = input()

a = s.replace("XXXX","AAAA") # 사전 순으로 가장 앞서는 답을 출력해야하므로 A 부터 치환한다
b = a.replace("XX", "BB")

print(-1 if "X" in b else b)
