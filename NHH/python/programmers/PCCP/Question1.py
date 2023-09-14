def solution(input_string):
    answer = ''

    # current = input_string[0]
    # for i in range(len(input_string)):
    #     ch = input_string[i]
    #     if ch.isupper():
    #         answer += ch
    #         continue
    #
    #     input_string = input_string.replace(current, current.upper())
    #     if current != ch:
    #         current = ch
    #
    # answer = answer.lower()
    # list(answer).sort()
    #
    # return "".join(set(answer))

    for i in range(len(input_string) -1):

        if input_string[i] == input_string[i+1]:
            continue

        if answer.count(input_string[i+1]) > 0:
            answer += input_string[i]



print(solution("zbzbz"))

