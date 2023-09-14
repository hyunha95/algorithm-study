S = input()

answer = "I hate UCPC"
if S.count("U") > 0:
    S = S[S.index("U")+1:]
    if S.count("C") > 0:
        S = S[S.index("C")+1:]
        if S.count("P") > 0:
            S = S[S.index("P") + 1:]
            if S.count("C") > 0:
                answer = "I love UCPC"
print(answer)