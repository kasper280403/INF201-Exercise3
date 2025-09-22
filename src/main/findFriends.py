import re

name_pattern = re.compile(r'\b[A-ZÆØÅ][a-zæøå]+\b')

def is_friends(s):
    names = name_pattern.findall(s)
    if len(names) <= 1:
        return None
    return names


def find_friends(s):
    friend_pairs = []
    for line in s.splitlines():
        friend_pair = is_friends(line)
        if friend_pair is None:
            continue

        friend_pairs.append(friend_pair)

    return friend_pairs

def print_nice(data):
    rows = [f"{a} - {b}" for a, b in data]

    heading = "Friendships"
    width = max(len(heading), max(len(r) for r in rows))

    print(heading.center(width))
    print("-" * width)

    for r in rows:
        print(r.center(width))

