area = input("Chose an area: (Cairo), (Giza), or (Tanta)\n")
print()
if area.lower()=='cairo'or area.lower()=="giza"or area.lower()=="tanta":
    print(f'{area} is on list')
else:
    print(f"sorry , {area} is not on our list!")