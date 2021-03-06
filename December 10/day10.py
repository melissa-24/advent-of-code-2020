import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as infile:

    # dictionary of dictionaries
    adaptors = [int(line.strip()) for line in infile.readlines()]
    # outlet jolts rate
    adaptors.append(0)
    adaptors.sort()
    # built in device rate
    adaptors.append(adaptors[-1]+3)


    differences = {}
    for a, b in zip(adaptors[1:], adaptors[:-1]):
        if a - b not in differences:
            differences[a-b] = 1
        else:
            differences[a-b] += 1
    

    print("Differences :", differences)
    print(f"Result is {differences[1] * differences[3]}")