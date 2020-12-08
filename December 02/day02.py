from collections import namedtuple
from typing import List

with open('list02.txt') as f:
    input_list = [line.strip() for line in f]

# example group in input_list: ['3-8 t', ' wttlmpdkfkf']

Validator = namedtuple('Validator', ['min_num', 'max_num', 'let'])

class Password_Validator:
    def __init__(self, policy: List[str]):
        policy = policy.split(" ")
        self.policy = Validator(int(policy[0].split("-")[0]),
                                int(policy[0].split("-")[1]),
                                policy[1].strip(":"))
        self.password = policy[2].strip()


    def validate(self):
        if self.policy.min_num <= self.password.count(self.policy.let) <= self.policy.max_num:
            return True
        return False


def check_passwords(input: List[str]) -> int:
    count = 0
    for group in input:
        x = Password_Validator(group)
        if x.validate():
            count += 1
    return count

print(check_passwords(input_list))