# Project started by Edius Ahlqvistus 2026-10-18 with the aim of learning Python.


def main() -> None:
    while True:
        display_main_menu()

        choice = input("Choose an option from the menu: ").strip().lower()

        match choice:
            case "1":
                print("Not implemented yet")
            case "2":
                print("Not implemented yet")
            case "3":
                print("Goodbye!")
                return
            case _:
                print("Invalid option!")


def display_main_menu() -> None:
    print("\n=== PIGEONOTCHI ===\n")
    print("1. New Game")
    print("2. Continue")
    print("3. Quit")


if __name__ == "__main__":
    main()
