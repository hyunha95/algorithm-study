# 1시간 20분 걸렸음..

def solution(today, terms, privacies):
    answer = []
    term = {}

    # 약관 종류와 기간을 key와 value로 딕셔너리에 담는다.
    # {'A': '6', 'B': '12', 'C': '3'}
    for t in terms:
        x, y = t.split()
        term[x] = y

    idx = 0 # 몇 번째 데이터인지 세기 위한 변수

    # 개인 정보를 한개씩 돌면서
    for p in privacies:
        idx += 1 # 번호가 1부터 시작하므로 +1 해준다
        date, type = p.split() # 공백을 기준으로 개인정보 수집 일자와 약관 종류를 나눈다. //date: 2021.05.02 / type: A

        year, month, day = date.split('.') # 개인정보 수집 일자를 .을 기준으로 년,월,일로 나눈다. // year: 2021 / month: 05 / day: 02

        period = term.get(type) # 해당 약관에 해당하는 유효 기간 조회

        # 개인 정보 수집 일자의 '월'과 약관 유효 기간을 더해서 12가 넘지 않는다면
        if int(month) + int(period) <= 12:
            change_month = str(int(month) + int(period)) # 월 , 유효기간을 더해줘서 최대 보관 일자의 '월'을 계산 해준다.

            # 최대 보관 일자의 '일'은 항상 -1을 해줘야 한다.
            # 만약 개인 정보 수집 일자의 '일'이 01이면 28일로 바꿔주고, '월'을 -1 해준다.
            if day == "01":
                day = "28"
                change_month = str(int(change_month) - 1)

            # '일'이 01이 아니라면 그냥 day -1을 해준다.
            else:
                day = str(int(day)-1)

            # 한 자리수라면 앞에 0을 붙여주기 위한 코드
            if len(day) == 1:
                day = "0"+day

            if len(change_month) == 1:
                change_month = "0"+change_month

            date = '.'.join([year, change_month, day])

            if today > date:
                answer.append(idx)
        else:
            diff = str((int(month) + int(period)) % 12)
            year = str(int(year) + ((int(month) + int(period)) // 12))

            if day == "01":
                day = "28"
                diff = str(int(diff) - 1)
            else:
                day = str(int(day)-1)

            if diff == "0":
                diff = "12"
                year = str(int(year)-1)

            if len(day) == 1:
                day = "0"+day

            if len(diff) == 1:
                diff = "0"+diff

            date = '.'.join([year, diff, day])

            if today > date:
                answer.append(idx)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today, terms, privacies))