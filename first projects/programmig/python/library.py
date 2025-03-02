print("""
█  █ █▀▀█ █  █ █▀▀█    █    ▀  █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █  █ 
█▄▄█ █  █ █  █ █▄▄▀    █   ▀█▀ █▀▀▄ █▄▄▀ █▄▄█ █▄▄▀ █▄▄█ 
▄▄▄█ ▀▀▀▀  ▀▀▀ ▀ ▀▀    ▀▀▀ ▀▀▀ ▀▀▀  ▀ ▀▀ ▀  ▀ ▀ ▀▀ ▄▄▄█
""")
your_library = []
your_wishlist = []
your_books = input("Enter the nema of a book you own: ")
your_library.append(your_books)
print()
nema = input("Enter the nema of another a book ypu own (or please Enter to skipe): ")
if nema:
    your_library.append(nema)
    print()
    print(f'your library: {your_library}')
else:
    print()
    print(f"your library: {your_library}")
your_books_2 = input("Enter the nema of a book you wish to have is the future: ")
your_wishlist.append(your_books_2)
print()
nema_2 = input("Enter the name of another book you wish to have (or press 'Enter' to skipe): ")
if nema_2:
    your_wishlist.append(nema_2)
    print()
    print(f"your wish list: {your_wishlist}")
else:
    print()
    print(f"your wish list: {your_wishlist}")
nema_3 = input("Enter the nema of a booke from your wishlist that you've ac quired (or press 'Enter' to skip): ")
if nema_3:
    print()
    your_library.append(nema_3)
    your_wishlist.remove(nema_3)
    print(f'your library: {your_library}')
    print(f"your wish list: {your_wishlist}")
else:
    print()
    print(f'your library: {your_library}')
    print(f"your wish list: {your_wishlist}")
name_5 = input("Enter the neam of a book frome your wish to don ate (or press 'Enter' to skip): ")
if name_5:
    print()
    your_library.remove(name_5)
    print(f'your library: {your_library}')
    print(f"your wish list: {your_wishlist}")
else:
    print()
    print(f'your library: {your_library}')
    print()
