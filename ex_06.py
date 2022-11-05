num = int(input("Введите число: "))

if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

#Более оптимально
def checker(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print('Число четное')
        else:
            print('Число нечетное')
    except:
        print('этот символ не номер')
number = input("Введите число: ")

checker(number)