#before 4 million, Fibonacci sequence but sum of all even valued terms
maximum = 4000000
total = 0
listing = [1,2]
while (int(listing[-1]) + int(listing[-2])) < maximum:
    listing.append((int(listing[-1]) + int(listing[-2])))
print(len(listing))
print(listing)
for i in range(len(listing)):
    if int(listing[i])%2 == 0:
        total += listing[i]
print(total)
