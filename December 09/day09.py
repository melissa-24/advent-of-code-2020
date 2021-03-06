import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

def xmas(data, m):
    if m < 25:
        return True

    for j in range(m - 25, m):
        for k in range(j + 1, m):
            if data[j] + data[k] == data[m]:
                return True

    return False

with open(sys.argv[1]) as infile:

    # dictionary of dictionaries
    data = [int(line.strip()) for line in infile.readlines()]
    m = 25
    while m < len(data):
        if not xmas(data, m):
            break
        m += 1

    print(f"Entry {data[m]} (line {m}) is not valid")