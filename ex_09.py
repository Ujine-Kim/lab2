ans = 0
neg_flag = False
x = int(input("Введите число: "))
if x < 0:
    neg_flag = True
while ans ** 2 < x:
    ans = ans + 1  # ans изначально 0, и нас необходимо прибавлять к нему 1 пока квадрат этого числа не будет равен или больше
    # введённом изначально x
if ans ** 2 == x:  # теперь когда это произошло мы можем с уверенностью сказать что квадратный корень из x будет равен
    # ans
    print("Квадратный корень из ", x, "равен", ans)
else:  # для всех остальных случаев так как ans в квадрате не равен x - идеальный корень из него не извлечь,
    # об этом и сообщаем и дополнительно, отправляем уточнение про отрицательное число, если флаг отрицания
    # (neg_flag) у нас в True
    print(x, "это не идеальный квадрат")
    if neg_flag:
        print("Просто проверял ... ты имел в виду", -x, "?")

ans = 0
neg_flag = False
x = int(input("Введите число: "))
if x < 0:  # Если ввели отрицательное число меняет влаг на True и в конце уточняем имелось ли ввижу положительное число
    x = -x
while ans ** 2 < x:
    ans = ans + 1  # ans изначально 0, и мы будем прибавлять к нему 1 пока квадрат этого числа не будет равен или больше
    # введённом узначально x
if ans ** 2 == x:  # теперь когда это произошло мы можем с уверенностью сказать что квадратный корень из x будет равен
    # ans
    print("Квадратный корень из", x, "равен", ans)
else:  # для всех остальных случаев так как ans в квадрате не равен x - идеальный корень из него не извлечь,
    # об этом и сообщаем и дополнительно, отправляем уточнение про отрицательное число, если флаг отрицания
    # (neg_flag) у нас в True
    print(x, "это не идеальный квадрат")