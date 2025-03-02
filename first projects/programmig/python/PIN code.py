import random
print()
pin_code = random.randint(1000,9999)
print()
user_input = int(input("Enter a 4-digits PIN code:\n"))
if len(str(user_input))!=4:
    print()
    print("please int a 4-digits")
elif user_input==pin_code:
    print()
    print("success! PIN code matched")
else:
    print()
    print("Failure pin code did not matched")
    print(f"the code generatedthis PIN: {pin_code}")