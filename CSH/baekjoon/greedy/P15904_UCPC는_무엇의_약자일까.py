string = input()
ucpc = ['U', 'C', 'P', 'C']

for s in string:
    if ucpc:
        if s == ucpc[0]:
            del ucpc[0]

if not (len(ucpc)):
    print("I love UCPC")
else:
    print("I hate UCPC")
