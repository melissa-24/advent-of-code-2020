import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as infile:

    total = 0
    groups = infile.read().split('\n\n')
    for group in groups:
        group = group.split()
        yeses = set(group[0])
        for answer in group[1:]:
            yeses = yeses.intersection(set(answer))
            
        total += len(yeses)

    print(f"Total number of unique \"yes\" answers is {total}")