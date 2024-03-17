mesto = int(input("Введите номер места: "))

if mesto > 55:
    print("Боковое")
elif mesto % 2:
    print("Купе внизу")
else:
    print("Купе наверху")
