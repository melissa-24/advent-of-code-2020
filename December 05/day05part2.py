import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

def to_index(bpass):
    bpass = bpass.strip()

    bpass = bpass.replace('F', '0')
    bpass = bpass.replace('L', '0')
    bpass = bpass.replace('B', '1')
    bpass = bpass.replace('R', '1')

    return int(bpass, 2)

with open(sys.argv[1]) as infile:

    passes = infile.read().split('\n')
    passes = [to_index(p) for p in passes if p]
    passes.sort()

    for p, n in zip(passes[:-1], passes[1:]):
        if n - p > 1:
            print(f"There is an empty seat at {p+1}")
            break