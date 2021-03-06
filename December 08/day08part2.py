import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)


with open(sys.argv[1]) as infile:

    # dictionary of dictionaries
    instructions = []
    for instruction in infile.readlines():
        instruction = instruction.split()
        instructions.append((instruction[0], int(instruction[1])))

    visited = set()
    changed = set()
    acc = 0
    i = 0
    edited = False
    wrong = 0
    while i < len(instructions):
        if i in visited:
            print(f"Operation {i} ({instructions[i]}) already visited")
            visited.clear()
            acc = 0
            i = 0
            edited = False
            
        visited.add(i)

        if instructions[i][0] == "acc":
            acc += instructions[i][1]
            i += 1
        elif instructions[i][0] == "jmp":
            if not edited and not i in changed:
                changed.add(i)
                # becomes no op
                wrong = i
                edited = True
                i += 1
            else:
                i += instructions[i][1]
        else:
            if not edited and not i in changed:
                changed.add(i)
                # becomes jump
                wrong = i
                edited = True
                i += instructions[i][1]
            else:
                i += 1

    print(f"Operation to change is {wrong} ({instructions[wrong]})")
    print(f"The accumulator is at {acc}")