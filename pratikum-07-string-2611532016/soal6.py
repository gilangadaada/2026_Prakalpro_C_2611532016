# name gilang adhatul sukri
# nim 2611532016
# question 5

full_name = " Siti Aisyah "
nim = "2610511023"

clean = full_name.strip().lower()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]
username = first + nim[-3:]
print(username)