import random

def print_art():
    print("""
     ▄   ▄
 ▄█▄ █▀█▀█ ▄█▄
▀▀████▄█▄████▀▀
     ▀█▀█▀
    """)

def start_game():
    print_art()
    print("Welcome to my island adventure! 🏝️")
    player_hp = 100
    print(f"Your HP: {player_hp} ❤️")
    print()
    
    choice = choose_action("You wake up on a mysterious island. What do you do?", [
        ("Explore the island", "explore"),
        ("Look for weapons", "weapons"),
        ("Find food", "food")
    ])
    
    if choice == "explore":
        player_hp = explore_island(player_hp)
    elif choice == "weapons":
        player_hp = find_weapon(player_hp)
    elif choice == "food":
        player_hp = find_food(player_hp)
    
    if player_hp > 0:
        challenge_room(player_hp)
    else:
        print("Game Over! You didn't survive the island. 💀")

def choose_action(question, options):
    print(question)
    for i, (desc, key) in enumerate(options, 1):
        print(f"{i}. {desc}")
    
    while True:
        choice = input("Choose an option (1-3): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice)-1][1]
        print("Invalid choice! ❌ Try again.")

def explore_island(hp):
    print("You explore the island and find an ancient ruin. 🏛️")
    event = random.choice(["trap", "treasure", "enemy"])
    
    if event == "trap":
        print("Oh no! You triggered a trap! ⚠️ You lose 20 HP.")
        return hp - 20
    elif event == "treasure":
        print("You found a hidden treasure chest! 💰 +20 HP.")
        return hp + 20
    elif event == "enemy":
        print("A wild creature attacks! 🐺 You fight and lose 30 HP.")
        return hp - 30
    return hp

def find_weapon(hp):
    print("You search for weapons and find a rusty sword. ⚔️")
    return hp

def find_food(hp):
    print("You find some edible fruits and regain energy! 🍎 +10 HP.")
    return hp + 10

def challenge_room(hp):
    print("You enter a new chamber filled with riddles and traps! 🏺")
    choice = choose_action("What will you do?", [
        ("Solve a riddle 🤔", "riddle"),
        ("Run through the traps 🏃", "traps")
    ])
    
    if choice == "riddle":
        print("You answer correctly and a secret door opens! 🎉")
        boss_fight(hp)
    else:
        print("⚠️ You triggered a hidden trap! -30 HP.")
        hp -= 30
        if hp > 0:
            boss_fight(hp)
        else:
            print("Game Over! 💀")

def boss_fight(hp):
    print("🔥 A giant guardian appears! Time for battle! ⚔️")
    boss_hp = 150
    
    while hp > 0 and boss_hp > 0:
        action = choose_action("What will you do?", [
            ("Attack with sword (-30 HP to boss) ⚔️", "attack"),
            ("Defend (-10 HP to you) 🛡️", "defend"),
            ("Try to escape (50% chance) 🏃", "escape")
        ])
        
        if action == "attack":
            boss_hp -= 30
            print(f"⚔️ You hit the boss! Boss HP: {boss_hp}")
            hp -= 20
            print(f"The boss counterattacks! Your HP: {hp}")
        elif action == "defend":
            hp -= 10
            print(f"🛡️ You blocked the attack but took some damage. Your HP: {hp}")
        elif action == "escape":
            if random.choice([True, False]):
                print("🏃 You successfully escape! You survive!")
                return
            else:
                print("The boss stops you! Prepare to fight! ⚔️")
                hp -= 20
    
    if hp <= 0:
        print("💀 You were defeated by the boss! Game over!")
    elif boss_hp <= 0:
        print("🎉 You defeated the boss and won the game! 🏆")

# Start the gamr