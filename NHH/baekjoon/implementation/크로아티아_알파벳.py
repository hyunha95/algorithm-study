s = input()
alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = 0
while len(s) > 0:

    found = False
    for alphabet in alphabets:
        if s.startswith(alphabet):
            s = s[len(alphabet):]
            answer += 1
            found = True

    if not found:
        s = s[1:]
        answer += 1

print(answer)