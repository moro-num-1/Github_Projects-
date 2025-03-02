colors = []
your_choose = input("Add your First color you like: ")
print()
your_choose_2 = input("do you want add more colors? yes or no? ")
if your_choose_2 == 'yes':
    print()
    your_choose_3 = input ("add another color to the list: ")
    print()
    colors.append(your_choose)
    colors.append(your_choose_3)
    print("the colors you like are:")
    print(colors)
elif your_choose_2 == 'no':
    print()
    colors.append(your_choose)
    print("the colors you like are:")
    print(colors)
else:
    print()
    print("please invalid choice")