print("Введите кол-во всех цифр.")
Numbers = int(input())
list = list()
for Number in range(Numbers):
    list.append(int(input()))
print("Введите число под которым описана ваша операция для чисел 1. Сложить 2. Умножить 3. Разделить 4. Вычесть")
operator = int(input())
Result = 0
if operator == 1:
    for Number in list:
        Result += Number
if operator == 2:
    Result += 1
    for Number in list:
        Result *= Number
if operator == 3:
    Result = list[0]
    for Number in range(1, len(list)):
        if list[Number] != 0:
            Result /= list[Number]
        else:
            print("Была обнаружена цифра 0 при делении, мы её пропустим и поделим на следующее число")
if operator == 4:
    for Number in list:
        Result -= Number
print("Ответ:", Result)