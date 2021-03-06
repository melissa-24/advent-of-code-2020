import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)

mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open(sys.argv[1]) as infile:

    passports = infile.read().split('\n\n')
    valid = 0
    not_valid = 0
    for pp in passports:
        data = {dd.partition(':')[0] : dd.partition(':')[2] for dd in pp.split()}
        if all(field in data.keys() for field in mandatory):
            valid += 1
        else:
            not_valid += 1

    print(f"There are {valid} valid passports")
    print(f"There are {not_valid} not valid passports")