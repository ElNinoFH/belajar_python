import argparse

parser = argparse.ArgumentParser(
    description = 'Just provide your name!'
)

parser.add_argument(
    '-n',
    '--name',
    required = True,
    help='show hello word to a name'
)

parser.parse_args()
args = parser.parse_args()

print(f"Hello, {args.name}! How are you?")