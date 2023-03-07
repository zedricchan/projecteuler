#Largest palindrome made from the procduct of two 3-digit number
a = 0 #a refers to the largest palindrome (always initialise with the lowest possible number)
# Loop through all possible 3-digit numbers
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if str(product) == str(product)[::-1]:
            if product > a:
                a = product

print(a)
