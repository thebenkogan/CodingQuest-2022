import math
from aoc import nums, read_input

lines = read_input()
total = 0
for i in range(len(lines) - 1):
    a1, b1, c1 = nums(lines[i])
    a2, b2, c2 = nums(lines[i + 1])
    total += int(math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2 + (c1 - c2) ** 2))
print(total)
