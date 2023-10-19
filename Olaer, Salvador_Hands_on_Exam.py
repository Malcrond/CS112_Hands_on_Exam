print("################################")
print("| NUMBER SYSTEM CONVERSION WOW |")
print("################################")
print("By: Kurt Andrey Olaer, Mon Nikolai R. Salvador")
print("\n1 = BINARY /// 2 = OCTAL /// 3 = HEXA")
number = int(input("\nEnter a number: "))
if number == 1:
    number = int(input("Input a number to convert to Binary: "))
    print(format(number, "b"))
elif number == 2:
    number = int(input("Input a number to convert to Octal: "))
    print(format(number, "o"))
elif number == 3:
    number = int(input("Input a number to convert to Hexadecimal: "))
    print(format(number, "x"))
else:
    print("Invalid input. Please try again.")
