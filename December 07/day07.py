import sys

if len(sys.argv) < 1:
    print("Input file expected", file=sys.stderr)
    sys.exit(1)


key_color = "shiny gold"

def check_in_bag(color, rules):
    if key_color in rules[color]:
        return True

    return any(check_in_bag(name, rules) for name in rules[color].keys())


with open(sys.argv[1]) as infile:

    # dictionary of dictionaries
    rules = {}
    for instruction in infile.readlines():
        instruction = instruction.strip()[:-1]    # remove full stop
        words = instruction.split()
        bag_color = ' '.join(words[:2])

        # list of bags contained in upper bag
        contains = instruction[instruction.find("contain")+8:]
        rule = {}
        if "no other" in contains:
            rules[bag_color] = {}
        else:
            for con in contains.split(','):
                con = con.strip()
                bags = con.split()
                rule[' '.join(bags[1:3])] = int(bags[0])
            rules[bag_color] = rule

    valid = 0
    for name in rules.keys():
        if check_in_bag(name, rules):
            print(f"A {name} bag can contain a {key_color} one")
            valid += 1

    print(f"There are {valid} valid bags")