menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(number_of_days):
    row = []
    for menu in menus:
        portion = int(input(f"Day {day + 1}, {menu}: "))
        row.append(portion)
    sales.append(row)

# Traversal per baris
print("Total per day:")
for day in range(number_of_days):
    day_total = 0
    for col in range(len(menus)):
        day_total = day_total + sales[day][col]
    print(f"Day {day + 1}: {day_total}")

# Traversal per kolom
menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for day in range(number_of_days):
        menu_total = menu_total + sales[day][col]
    menu_totals.append((menus[col], menu_total))
print("Total per menu:", menu_totals)

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
print(f"Best seller: {best_name} ({best_total})")