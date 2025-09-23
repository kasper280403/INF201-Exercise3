import findFriends
from src.main import fileTree


def main():
    print("Program is running. Type q/Q to quit.")

    while True:
        find_friends = findFriends.find_friends(string)
        findFriends.print_nice(find_friends)

        fileTree.print_tree("resources")


        user_input = input()
        if user_input.lower() == "q":
            print("Program terminated...")
            break

        # Her kan du legge til annen funksjonalitet som skal kjøre kontinuerlig


string = """
Ali and Per and friends.
Kari and Joe know each other.
James has known Peter since school days.
"""

if __name__ == "__main__":
    main()