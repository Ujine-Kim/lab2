first_num = input('Введите первое число:')
if first_num.isnumeric():
    length_f_of_num = len(first_num)
    if 1 <= length_f_of_num <= 6:
        first_num = int(first_num)
        temp_num = first_num
        # В первом блоке во-первых проверяем что введённое значение является числом. Далее присваиваем переменной
        # length_f_of_num его длину (кол-во символов) и его значение переменной temp_num, переведя в int
        second_num = input('Введите второе число:')
        if second_num.isnumeric():
            length_s_of_num = len(second_num)
            if 1 <= length_s_of_num <= 6:
                second_num = int(second_num)
                # Тут делаем тоже самое но со 2ым числом
                for s_num in range(1, length_s_of_num+1):
                    # Будем пробегаться в диапазоне от первой до последней цифры в зависимости от кол-ва символов
                    remainder_of_2_div = second_num % 10
                    div_zero_2 = second_num // 10
                    second_num = div_zero_2
                    # remainder_of_2_div - последняя цифра 2ого числа; div_zero_2 - число без последней цифры 2ого
                    # числа и это значение мы переприсваиваем 2ому числу
                    for f_num in range(1, length_f_of_num+1):
                        # Теперь делаем тоже самое для первого числа. Диапазон от 1 до кол-ва символов(включительно,
                        # т.к. плюс 1)
                        remainder_of_1_div = first_num % 10
                        div_zero_1 = first_num // 10
                        first_num = div_zero_1
                        # Тут по сути аналогичные присваивания, но с первым числом, после чего мы сравниваем
                        # полученное 2ое число с первым и если они совпадают то сообщаем об этом. Так как тут
                        # вложенный цикл то мы по сути каждой цифрой 2ого числа проходимся по первому и в случае
                        # совпадений выводим позицию
                        if remainder_of_2_div == remainder_of_1_div:
                            print(f'Число {remainder_of_1_div} расположено на {f_num} позиции')
                        elif div_zero_1 == 0:
                            first_num = temp_num
            else:
                print('Вводить можно только числа в промежутке от 1 до 999 999')
        else:
            print('Возможен только ввод целых положительных чисел')
    else:
        print('Вводить можно только числа в промежутке от 1 до 999 999')
else:
    print('Возможен только ввод целых положительных чисел')