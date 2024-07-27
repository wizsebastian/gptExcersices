print("Welcome to calculator mini console app")
print("-~-----------WIZ--------------~-")
print("This app work with to numbers only for now")
print("You pass two numbers to the app, and we will do the math for you")
print("-~-----------WORK--------------~-")

first_val = input("Enter the first number")
second_val = input("Enter the second number")

if type(first_val) != int and type(second_val) != int:
    print(isinstance(first_val, second_val))
    first_val = ""
    second_val = ""
    print("-~-----------OBSERVATION--------------~-")
    print("We are thinking you try to joking us")
    print("please pass some numbers when you come back... See you.")
    print("-~-----------OBSERVATION--------------~-")
else:
    print("The SUM: " + str(first_val + second_val))
    print("The DIFFERENCE: " + str(first_val - second_val))
    print("The PRODUCT: " + str(first_val * second_val))
    print("The QUOTIENT: " + str(first_val / second_val))
