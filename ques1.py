try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = a + b
    print("The Sum:", c)
except ValueError:
    print("Please enter a numerical value.")
