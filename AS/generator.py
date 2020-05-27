#!/usr/bin/env python3

group = []
i = 0

g = int(input("Enter generator: "))
base = int(input("Enter base: "))

while True:
    if str(pow(g, i, base)) not in group:
        group += str(pow(g, i, base))
        i += 1
    else:
        break

# Sort for better visualization     
group.sort()

print("Your cyclic group is:", group)