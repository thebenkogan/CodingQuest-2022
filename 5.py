from aoc import read_input
import hashlib


def correct_line(parts):
    for mined_number in range(10000000000):
        to_hash = f"{parts[0]}|{mined_number}|{parts[2]}"
        hash_object = hashlib.sha256(to_hash.encode("utf-8"))
        hx = hash_object.hexdigest()
        if hx[:6] == "000000":
            return to_hash + "|" + hx

    raise "number not found"


lines = read_input()
for index, line in enumerate(lines):
    parts = line.split("|")
    target_hash = parts[3]
    to_hash = "|".join(parts[:3])
    hash_object = hashlib.sha256(to_hash.encode("utf-8"))
    hx = hash_object.hexdigest()
    if hx == target_hash:
        continue

    lines[index] = correct_line(parts)
    break

for i, line in enumerate(lines):
    if i <= index:
        continue
    prev_hash = lines[i - 1].split("|")[3]
    parts = line.split("|")
    parts[2] = prev_hash
    lines[i] = correct_line(parts)

print(lines[-1].split("|")[3])
