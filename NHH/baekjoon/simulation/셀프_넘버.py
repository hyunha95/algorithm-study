arr = [i for i in range(1, 10000+1)]

for index in range(1, 10000+1):
    self_number = index
    for char in str(index):
        self_number += int(char)

    if arr.count(int(self_number)) > 0:
        arr.remove(int(self_number))

for not_self_number in arr:
    print(not_self_number)


# d(75) = 75+7+5
# d(d(75)) =  d(75+7+5) = 87+8+7