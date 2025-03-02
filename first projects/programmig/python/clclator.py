print("Welcom to our calcculator")
print()
mark_str = input("Choose one of these marks:(+),(-),(*),(/): ")
print()
num1_int = int(input("type first number: "))
print()
num2_int = int(input("type second number: "))
if mark_str=="+":
    print()
    result = num1_int + num2_int
    print(f"result is: {result}")
elif mark_str=="-":
    print()
    result = num1_int - num2_int
    print(f"result is : {result}")
elif mark_str == "*":
    print()
    result = num1_int * num2_int
    print(f"result is : {result}")
elif mark_str == "/":
    print()
    result = num1_int / num2_int
    print(f"resuls is : {result}")
else:
    print()
    print("invalid choice")