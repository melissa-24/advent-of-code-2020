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

    print(f"Looking for a range that sums up to {data[m]}")

    i = 0
    while i < len(data):
        c = i
        sum = 0
        while sum < data[m]:
            sum += data[c]
            c += 1

        if sum == data[m]:
            break
        i += 1

    small = min(data[i:c])
    large = max(data[i:c])
        
    print(f"Result is {small} + {large} = {small+large}")