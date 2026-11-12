# name gilang adhatul sukri
# nim 2611532016
# question 4

phone = "081234567890"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)
