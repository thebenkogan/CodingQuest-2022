from aoc import nums, read_input

ln = set([12, 48, 30, 95, 15, 55, 97])
winnings = {3: 1, 4: 10, 5: 100, 6: 1000}

lines = read_input()
total = 0
for line in lines:
    ns = nums(line)
    shared_count = sum(1 for n in ns if n in ln)
    if shared_count in winnings:
        total += winnings[shared_count]

print(total)
