print("Введите год: ")
years = int(input())
result = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if(years % 4 == 0):
    result += 11
for i in range(len(month)):
    day = month[i]
    number = 1
    while day >= number:
        if(number >= 10):
            perevod = str(number)
            result += int(perevod[0]) + int(perevod[1])
        else:
            result += number
        number += 1
print(result)