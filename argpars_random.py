import argparse
import random

name_list = [
    'Alice', 'Bob', 'Charlie', 'Diana', 'Ethan',
    'Fiona', 'George', 'Hannah', 'Ian', 'Julia',
    'Kevin', 'Laura', 'Michael', 'Nina', 'Oscar'
]

parser = argparse.ArgumentParser(
    description='Generate random names'
)

parser.add_argument(
    '-n', '--number',
    type=int,
    required=True,
    help='Numbers to be displayed | max = 10'
)

args = parser.parse_args()

max_names = 10
if args.number > max_names:
    print(f"Maximum number allowed is {max_names}. Showing {max_names} names instead.")
    args.number = max_names

random_names = random.sample(name_list, args.number)

for name in random_names:
    print(name)