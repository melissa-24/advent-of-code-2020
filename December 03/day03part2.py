import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)


with open(sys.argv[1]) as infile:
    move = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    result = 1
    iterfile = list(infile) # can loop over and over on file
    for x, y in move:
        cx = 0
        cy = 0
        trees = 0
        for slope in iterfile:
            cy += 1
            if (cy - 1) % y:
                continue

            slope = slope.strip()
            if slope[cx % len(slope)] == '#':
                    trees += 1
            cx += x
        print(f"Going {y} down and {x} right you hit {trees} trees")
        result *= trees

    print (f"Result is {result}")

    # To run py day03part1.py list.txt