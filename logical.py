# A Simple Calculator App

print("Welcome To Our Simple Calculator App")
print('''
**************
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Exponential
**************
''')

# Addition

print("Enter two numbers to add")
firstNumber = input("Enter first number: ")
secondNumber = input("Enter second number: ")

total = float(firstNumber) + float(secondNumber)

print(f"{firstNumber} + {secondNumber} = {total:.2f}")




# Substraction

print("**************")
print("Substraction")
print("**************")
print("Enter two numbers to substract")
firstNumber = input("Enter first number: ")
secondNumber = input("Enter second number: ")

total = float(firstNumber) - float(secondNumber)

print(f"{firstNumber} - {secondNumber} = {total:.2f}")


# Multiplication

print("**************")
print("Multiplication")
print("**************")
print("Enter two numbers to multiply")
firstNumber = input("Enter first number: ")
secondNumber = input("Enter second number: ")

total = float(firstNumber) * float(secondNumber)

print(f"{firstNumber} * {secondNumber} = {total:.2f}")



# Division

print("**************")
print("Division")
print("**************")
print("Enter two numbers to divide")
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

total = firstNumber / secondNumber

print(f"{firstNumber} / {secondNumber} = {total:.2f}")




# Exponential

print("**************")
print("Exponential")
print("**************")
print("Enter two numbers to perform exponential operation on")
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

total = firstNumber ** secondNumber

print(f"{firstNumber} ** {secondNumber} = {total:.2f}")




