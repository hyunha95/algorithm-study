def solution(today, terms, privacies):
    dic = dict()
    for term in terms:
        key, value = term.split()
        dic[key] = int(value)

    answer = []
    for i in range(0, len(privacies)):
        full_date, type = privacies[i].split()

        year = int(full_date[0:4]) # 2021
        month = int(full_date[5:7]) # 5
        date = int(full_date[8:]) # 19

        period = dic[type] # 6 달

        if period > 12:
            year += period // 12
            month += period - ((period // 12) * 12)
        elif period == 12:
            year += 1
        else:
            month += period

        if month > 12:
            year += 1
            month -= 12

        month = f'0{month}' if month < 10 else month
        date = f'0{date}' if date < 10 else date

        if ".".join([str(year), str(month), str(date)]) <= today:
            answer.append(i + 1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01"	, ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2016.02.15"	, ["A 100"], ["2000.06.16 A", "2008.02.15 A"])) # [1]

