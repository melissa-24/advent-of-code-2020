import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as infile:

    total = 0
    groups = infile.read().split('\n\n')
    groups = [g.replace('\n', '') for g in groups]
    yeses = [len(set(answers)) for answers in groups]

    print(f"Total number of \"yes\" answers is {sum(yeses)}")