print("""
     ▄   ▄
 ▄█▄ █▀█▀█ ▄█▄
▀▀████▄█▄████▀▀
     ▀█▀█▀
""")
import random
print("Welcome to my island adventure! 🏝️")
print()
doors = input("""There are two doors in front of you. 🚪̶ a red door and 🚪̶ a blue door

which door do you want to open?\n""")
print()
if doors.lower()=="red":
    print("Great! now you entered a room.")
    print()
    boxes_room = input("""you found three boxes:🎁 white, 🎁 blak, 🎁 green
    
which box do you open?\n""")
    if boxes_room.lower()=="green":
        print()
        print("Congratulations! you found the treasure!💰💰💰")
    elif boxes_room.lower()=="blak":
        print()
        print("Oops! you opened a box filled with spidars Game over! 🕸 🕸 🕸")
    elif boxes_room.lower()=="white":
        print()
        print("Oops! you opend a box filled with snakes Game over! 🐍 🐍 🐍 ")
    else:
        print()
        print("invalid choice")
elif doors.lower()=="blue":
    print()
    print("Oops you chose the crocodile door. Game over! 🐊🐊🐊")
else:
    print()
    print("invalid choice")
    