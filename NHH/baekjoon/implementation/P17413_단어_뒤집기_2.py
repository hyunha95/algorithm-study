S = input()

arr = []
while S:
    start_index = S.find("<")
    if start_index >= 0:
        arr.append(S[0:start_index])
        S = S[start_index:]

        end_index = S.find(">")
        arr.append(S[0:end_index + 1])
        S = S[end_index + 1:]
    else:
        arr.append(S)
        break


answer = ''
for word in arr:
    if word == '':
        continue
    elif word.startswith("<"):
        answer += word
    else:
        words = word.split()
        temp = []
        for w in words:
            w = list(w)
            w.reverse()
            temp.append(''.join(w))
        answer += ' '.join(temp)

print(answer)