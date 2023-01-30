print("Введите год: ")
year = int(input())
summa = 0
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if(year % 4 == 0):
    summa += 1
for x in range(1, len(days)+1):
    day = days[x]
    i = 1
    while day >= i:
        if(i >= 10):
            stroka = str(i)
            summa += int(stroka[0]) + int(stroka[1])
        else:
            summa += i
        i += 1
print(summa)