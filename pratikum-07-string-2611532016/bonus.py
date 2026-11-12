# name gilang adhatul sukri
# nim 2611532016
# bonus

sentence = "Kasur ini rusak"
clean = sentence.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")