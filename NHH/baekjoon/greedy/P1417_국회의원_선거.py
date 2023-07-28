N = int(input())
people = [int(input()) for _ in range(N)]

if len(people) == 1:
    print(0)
else:
    dasom = people.pop(0)
    max_num = max(people)
    if dasom == max_num:
        print(1)
    else:
        answer = 0
        while dasom <= max_num:
            people[people.index(max_num)] -= 1
            max_num = max(people)
            dasom += 1
            answer += 1
        print(answer)

