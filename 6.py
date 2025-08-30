from collections import defaultdict
from aoc import nums, read_input

mem = defaultdict(int)


def resolve(v):
    ns = nums(v)
    if len(ns) > 0:
        return ns[0]
    return mem[v]


lines = read_input()
pc = 0
recent_compare = True
while pc < len(lines):
    start_pc = pc
    line = lines[pc]
    split = line.split(" ")
    command = split[0]
    match command:
        case "ADD":
            mem[split[1]] += resolve(split[2])
        case "MOD":
            mem[split[1]] = mem[split[1]] % resolve(split[2])
        case "DIV":
            mem[split[1]] = mem[split[1]] // resolve(split[2])
        case "MOV":
            mem[split[1]] = resolve(split[2])
        case "JMP":
            pc += resolve(split[1])
        case "JIF":
            if recent_compare:
                pc += resolve(split[1])
        case "CEQ":
            recent_compare = resolve(split[1]) == resolve(split[2])
        case "CGE":
            recent_compare = resolve(split[1]) >= resolve(split[2])
        case "OUT":
            print(resolve(split[1]))
        case "END":
            break
    if pc == start_pc:
        pc += 1
