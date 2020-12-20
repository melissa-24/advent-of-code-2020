import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)


with open(sys.argv[1]) as infile:
    x = 0
    trees = 0
    for slope in infile:
        slope = slope.strip()
        if slope[x % len(slope)] == '#':
                trees += 1
        x += 3

    print(f"You hit {trees} trees")

    # To run py day03.py list.txt