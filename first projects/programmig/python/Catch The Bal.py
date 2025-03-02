import random
import os
import time

# Game settings
WIDTH = 10  # Screen width
player_pos = WIDTH // 2  # Player's starting position
ball_pos = random.randint(0, WIDTH - 1)  # Ball's starting position
missed = 0  # Missed ball counter
score = 0  # Score counter

while missed < 3:
    # Clear screen (Windows/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Draw screen
    screen = [" "] * WIDTH
    screen[player_pos] = "🟦"  # Player
    screen[ball_pos] = "⚪"  # Ball
    
    print("".join(screen))  # Print screen
    
    # Move playera
    move = input("Move [a] left / [d] right: ").strip().lower()
    if move == "a" and player_pos > 0:
        player_pos -= 1
    elif move == "d" and player_pos < WIDTH - 1:
        player_pos += 1

    # Check if ball is caught
    if player_pos == ball_pos:
        score += 1
        print("✅ You caught the ball! Score:", score)
    else:
        missed += 1
        print("❌ You missed! Misses:", missed)

    # Generate new ball position
    ball_pos = random.randint(0, WIDTH - 1)
    time.sleep(0.5)  # Small delay for better experience

print("\n💀 Game Over! Your final score:", score)