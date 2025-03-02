is_egyptian = input("Are you egyptian type (yes) or (no)\n").lower()
print()
if is_egyptian=="yes":
    print("Good that's the first step")
    print()
    is_18 = input("Are you abov 18? type yes or no\n").lower()
    if is_18=="yes":
        print()
        print("you can have and ID")
    else:
        print("sorry, you have to be 18 or older")
        print()
        print("pleas type agein when you are 18")
else:
    print()
    print("sorry,an Egyptan ID is give only to Egyptan")