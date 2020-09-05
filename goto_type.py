f = float('1')
print(f)

try:
    i = int('2.5')
    print(i)
except ValueError:
    #print("Неправильный тип")
    pass
finally:
    i = 2
    print(i)
b1 = bool(1)
print(b1)

b2 = bool('')
print(b2)

b3 = bool(0)
print(b3)