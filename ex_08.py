for n in range(5):
    print(n)

mysum = 0
for i in range(10):
    mysum += i
print(mysum)

mysum=0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)

