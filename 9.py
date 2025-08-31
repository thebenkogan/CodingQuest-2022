from collections import deque
from aoc import DIRS, read_input

lines = read_input()
grid = [[c for c in row] for row in lines]
sy = 0
sx = grid[0].index(" ")

q = deque([(sx, sy, 1)])
seen = set([(sx, sy)])
while len(q) > 0:
    x, y, c = q.popleft()
    if y == len(grid) - 1:
        print(c)
        break

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < len(grid[0])
            and 0 <= ny < len(grid)
            and (nx, ny) not in seen
            and grid[ny][nx] != "#"
        ):
            seen.add((nx, ny))
            q.append((nx, ny, c + 1))
