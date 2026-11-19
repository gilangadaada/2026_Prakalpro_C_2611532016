number_of_rows = 4
seats_per_row = 5
# Write your code below
seats = []
for r in range(number_of_rows):
    seats.append(["."] * seats_per_row)   # list baru tiap baris

taken = 0
while True:
    for r in range(number_of_rows):
        print(f"Row {r + 1}: " + " ".join(seats[r]))
    row = int(input("Row (0 to stop): "))
    if row == 0:
        break
    seat = int(input("Seat: "))
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif seats[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row - 1][seat - 1] = "X"
        taken = taken + 1
        print("Seat booked.")
print("Seats taken:", taken)