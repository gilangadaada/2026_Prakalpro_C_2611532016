LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

total = 0
highest_day = 1
days_above = 0
for i in range(len(expenses)):
    total = total + expenses[i]
    if expenses[i] > expenses[highest_day - 1]:
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above = days_above + 1
average = total / len(expenses)

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({expenses[highest_day - 1]})")
print("Days above limit:", days_above)