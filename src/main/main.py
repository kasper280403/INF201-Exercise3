def main():
    print("Program is running. Type q/Q to quit.")

    while True:

        user_input = input()
        if user_input.lower() == "q":
            print("Program terminated...")
            break

        # Her kan du legge til annen funksjonalitet som skal kjøre kontinuerlig


if __name__ == "__main__":
    main()