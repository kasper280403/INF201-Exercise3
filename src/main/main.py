import findFriends
from src.main import fileTree, sortFiles


def main():
    fileTree.print_tree("resources")

    sortFiles.sort_files("resources/test_files")

    fileTree.print_tree("resources")

    findFriends.find_friends(string)


string = """
Ali and Per and friends.
Kari and Joe know each other.
James has known Peter since school days.
"""

if __name__ == "__main__":
    main()