from aoc import read_input

secret_key = "Roads? Where We're Going, We Don't Need Roads."
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
char_set = {c: i for i, c in enumerate(chars)}
rev_char_set = {i: c for i, c in enumerate(chars)}


data = read_input(split_lines=False)
decoded = []
si = 0
for c in data:
    if c not in char_set:
        decoded.append(c)
        continue
    move_by = char_set[secret_key[si]] + 1
    decoded.append(rev_char_set[(char_set[c] - move_by) % len(chars)])
    si = (si + 1) % len(secret_key)

print("".join(decoded))
