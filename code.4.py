menu = [("Pizza", 250), ("Burger", 150), ("Pasta", 200)]
sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)
print("Sorted menu:", sorted_menu)
