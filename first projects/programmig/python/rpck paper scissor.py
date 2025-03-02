print("welcome to the rock, paper, Scissore game")
import random
print()
help_or_Enter = input("press Enter to continue or tyep (Help) for the rules: ").capitalize()
if help_or_Enter == 'help'.capitalize():
    print()
    print("""********* RULES *********
          1) you choose and the computer choose
          2) Rock smashes Scissore -> Rock wins
          3) Scissore cut paper -> Scissore wins
          4) paper cover Rock -> paper wins
""")
    your_choose = input("Enter your choicy (rock, paper, scissore): ")
else:
    print()
    your_choose = input("Enter your choicy (rock, paper, scissore): ")
random_choose = random.randint(0,2)
if random_choose == 0 :
    random_choose = 'rock'
elif random_choose == 1 :
    random_choose = 'paper'
else:
    random_choose = 'scissore'
if random_choose == your_choose:
    print()
    print("you won")
elif random_choose != your_choose:
    print()
    print("you loist")
    print(f"your choice is {your_choose} computer choice {random_choose}")
else :
    print()
    print("invalid choice")