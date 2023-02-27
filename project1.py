#sum of all multiples of 3 and 5 below 1000
justmultiples = []
alsomultiples = []
sum_of_all = 0
add = 0
for i in range(1000):
    if i%3 == 0 and i%5 == 0:
        alsomultiples.append(i)
    elif (i%3 == 0 and i%5 != 0) or (i%3 != 0 and i%5 == 0):
        justmultiples.append(i)
for x in range(len(justmultiples)):
    sum_of_all += int(justmultiples[x])

for y in range(len(alsomultiples)):
    add += int(alsomultiples[y])

print(sum_of_all + add)
