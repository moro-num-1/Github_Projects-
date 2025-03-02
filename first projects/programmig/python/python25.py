travel_list = input ("please type the names of the countries separated by comman: ").split()
for y in travel_list:
    print(f'\n{y}\n')
    yes_or_no = input(f"Have you ever visited {y} before (yes/no)\n").lower()
    if yes_or_no == 'yes':
        print("I hope you had a  wonderful time\n")
    else:
        print('I hopr you get to visit it soon\n')
    print("----------")
input("press enter to exit....")