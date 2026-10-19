# Project started by Edius Ahlqvistus 2026-10-18 with the aim of learning Python.
from pigeon import Pigeon

MAX_PIGEON_NAME_LENGTH = 20


def main() -> None:
    while True:
        display_main_menu()

        choice = input("Choose an option from the menu: ").strip().lower()

        match choice:
            case "1":
                pigeon = new_game()
                game_loop(pigeon)
            case "2":
                print("Not implemented yet")
            case "3":
                print("Goodbye!")
                return
            case _:
                print("Invalid option!")


def game_loop(pigeon: Pigeon) -> None:
    while True:
        print(f"\nYou are taking care of {pigeon.name}!")
        break


def new_game() -> Pigeon:
    pigeon_name = get_valid_pigeon_name()
    pigeon = Pigeon(pigeon_name)
    return pigeon


def get_valid_pigeon_name() -> str:
    while True:
        pigeon_name = input("What would you like to name your pigeon? ").strip()

        if not pigeon_name or len(pigeon_name) > MAX_PIGEON_NAME_LENGTH:
            print(f"A pigeon name needs to be between 1 and {MAX_PIGEON_NAME_LENGTH} characters long!")
        else:
            return pigeon_name


def display_main_menu() -> None:
    print("\n=== PIGEONOTCHI ===\n")
    print("1. New Game")
    print("2. Continue")
    print("3. Quit")


if __name__ == "__main__":
    main()
