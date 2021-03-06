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


    arrangements = [1]
    for i in range(1, len(adaptors)):
        arrange = arrangements[i-1]
        j = i - 2
        while j >= 0 and adaptors[i] - adaptors[j] <= 3:
            arrange += arrangements[j]
            j -= 1

        arrangements.append(arrange)


    print(f"There are {arrangements[-1]} valid arrangements")