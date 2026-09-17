a1_2016 = (
	input("input nilai boolean-1 (true/false): ").strip().lower() == "true"
)
a2_2016 = (
	input("input nilai boolean-2 (true/false): ").strip().lower() == "true"
)

print("\nA1 = ", a1_2016)
print("A2 = ", a2_2016)

hasil = a1_2016 and a2_2016
print("\nKonjungsi AND:")
print("A1 and A2 =", hasil)

hasil = a1_2016 or a2_2016 
print("\nDisjungsi OR:")
print("A1 or A2 =", hasil)

hasil = not a1_2016
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

hasil = not a2_2016
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)
