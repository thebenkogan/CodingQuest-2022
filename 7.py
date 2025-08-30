from aoc import nums, read_input

grid_height = 100_000
grid_width = 20_000

lines = read_input()
rects = []
x_coords = set([0, grid_width])
y_coords = set([0, grid_height])
for line in lines:
    x, y, w, h = nums(line)
    x_coords.update([x, x + w])
    y_coords.update([y, y + h])
    rects.append({"x": x, "y": y, "w": w, "h": h})


x_coords = sorted(x_coords)
y_coords = sorted(y_coords)

uncovered_area = 0

for i in range(len(x_coords) - 1):
    for j in range(len(y_coords) - 1):
        x1, x2 = x_coords[i], x_coords[i + 1]
        y1, y2 = y_coords[j], y_coords[j + 1]

        covered = False
        for r in rects:
            if (
                r["x"] <= x1
                and r["y"] <= y1
                and r["x"] + r["w"] >= x2
                and r["y"] + r["h"] >= y2
            ):
                covered = True
                break

        if not covered:
            uncovered_area += (x2 - x1) * (y2 - y1)

print(uncovered_area)
