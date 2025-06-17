print("simple calculator")
print("select operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("enter choice (1/2/3/4): ")

n1 = float(input("enter first number: "))
n2 = float(input("enter second number: "))

if choice == '1':
    print("result:", n1 + n2)
    
elif choice == '2':
    print("result:", n1 - n2)

elif choice == '3':
    print("result:", n1 * n2)

elif choice == '4':
    if n2 != 0:
        print("result:", n1 / n2)
    else:
        print("cannot divide by zero")
else:
    print("invalid input")