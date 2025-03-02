print("""
█▀▀█ █▀▀█ █▀▀▄ █▀▀▄  ▀  ▀▀█▀▀    █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ 
█▄▄▀ █▄▄█ █▀▀▄ █▀▀▄ ▀█▀   █      █ ▀█ █▄▄█ █ ▀ █ █▀▀ 
▀ ▀▀ ▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀   ▀      ▀▀▀▀ ▀  ▀ ▀   ▀ ▀▀▀
""")
print("wellcome to place the rabbit")
farme   =[["🌿","🌿","🌿"], ["🌿","🌿","🌿"], ["🌿","🌿","🌿"]]
print()
print(f'{farme[0]} \n{farme[1]} \n{farme[2]}')
print()
print("where should the rabbit go? 🐰")
position = (input("please choose aro and a column"))
row = int(position[0])
column = int(position[1])

farme[row-1][column-1] = "🐰"

print(f'{farme[0]},\n{farme[1]},\n{farme[2]}')
