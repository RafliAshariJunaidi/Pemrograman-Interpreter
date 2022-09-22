sum = 0
n = 0

for i in range(1,101):
    sum = sum + i
    n += 1

avg = sum / n
print("Sum: " + str(sum))
print("Avg: " + str(avg))
sum2 = 0
for i in range(1,101):
    sum2 = sum2 + (i - avg)* (i - avg)
    varian = sum2/(n-1)
print("Varian: " + str(varian))