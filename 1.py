from aoc import nums, read_input

lines = read_input(split_lines=False)
ns = nums(lines)

total = sum(ns[:59])
count = 0
for i, n in enumerate(ns[59:]):
    total += n
    avg = total / 60
    if avg < 1500 or avg > 1600:
        count += 1
    total -= ns[i]


print(count)
