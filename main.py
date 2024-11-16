first = int(input("Введите число:"))
second = int(input("Введите число:"))
third = int(input("Введите число:"))
if first != second and first != third and third != second:
    print(3)
if first == second or first == third or second == third:
    print(2)
if first == second == third:
    print(0)
