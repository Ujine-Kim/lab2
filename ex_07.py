n = input("Вы в затерянном лесу\n*********************\n*********************\n:)\n*********************\n"
          "*********************\nИдти налево или направо? ")
while n == "направо" or n == "Направо":
    n = input("Вы в затерянном лесу\n*********************\n******          ***\n:)\n*********************\n"
              "*********************\nИдти налево или направо? ")
print("\n Вы вышли из затерянного леса! \n \o/")
n = 0
while n < 5:
    print(n)
    n += 1

import random

print("Игра угадай число. Диапазон от 1 до 100. 6 попыток")
n = 6
secret_number = random.randrange(1, 101)
while n != 0:
    guess = int(input(str(n) + " попытка: "))
    if secret_number < guess:
        print("Неверно. Число меньше")
        n -= 1
    elif secret_number > guess:
        print("Неверно. Число больше")
        n -= 1
    else:
        print("Поздравляю, вы угадали! \n Правильный ответ: " + str(secret_number))
        break
if n == 0:
    print("Сожалею вы проиграли, попробуйте снова. \n Правильный ответ был: " + str(secret_number))
