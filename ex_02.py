hi = "Привет"
name = "Вася"
name1 = "Света"

# как в примере
greet = hi + name
print(greet)

greeting = hi + ' ' + name
print(greeting)

silly = hi + (' ' + name)*3
print(silly)

#Упрощенная версия
print(f'{hi} {name}, {name1}!')

