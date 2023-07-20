S = sorted(list(input()))
dic = dict()
for s in S:
    if s in dic.keys():
        dic[s] += 1
    else:
        dic[s] = 1

arr = list(dic.keys())
answer = ''
if len([x for x in list(dic.values()) if x % 2 != 0]) > 1:
    print("I'm Sorry Hansoo")
else:
    if len(S) % 2 == 0:
        answer += "".join(arr[:len(S)//2])
        answer += "".join(reversed(answer))
        print(answer)
    else:
        max_arr = []
        for key in dic.keys():
            if dic[key] % 2 != 0:
                max_arr.append(key)
        last = max(max_arr)

        for i in range(len(arr)):
            answer += arr[i] * (dic[arr[i]] // 2)

        answer += last
        answer += "".join(sorted(answer[:-1], reverse=True))
        print(answer)


