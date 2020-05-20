print("This is a basic calculator with basic operator")

print("1. Enter the first number")
print("1. Enter the second number")
print("1. Enter the operator")
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# print("First Number: " + str(num1))
# print("Second Number: " + str(num2))

operator = input("Enter Operator: ")

if (operator == "+"):
    print ("Result is equal to :" + str(num1 + num2))