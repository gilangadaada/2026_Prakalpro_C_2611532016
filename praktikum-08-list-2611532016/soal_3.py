temperatures = [-3, -1, -5, -2, -4, -1, -6]
highest = 0
lowest = temperatures[0]
for i in range(1, len(temperatures) + 1):
    if temperatures[i] > highest:
        highest = temperatures[i]
    if temperatures[i] < lowest:
        lowest = temperatures[i]
print("Highest:", highest)
print("Lowest:", lowest)
