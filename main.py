# Project started by Edius Ahlqvistus 2026-10-18 with the aim of learning Python.

from pigeon import Pigeon

DEBUG_MODE = True
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
        pigeon.check_welfare()

        if pigeon.is_adopted:
            print(
                f"{pigeon.name} has been rescued by the local animal welfare authorities. "
                "After a full recovery, your former companion has found a new home.\n\n"
                "Perhaps you should collect stones instead?"
            )
            return

        display_pigeon_menu(pigeon)
        choice = input("Choose an option from the menu: ").strip().lower()

        match choice:
            case "1":
                examine_pigeon(pigeon)
            case "2":
                pigeon.feed()
            case "3":
                return
            case _:
                print("Invalid option!")


def examine_pigeon(pigeon: Pigeon) -> None:
    print(f"\nYou carefully examine {pigeon.name} to see how it is doing.\n")
    print(f"Health: {pigeon.current_health} / {pigeon.max_health}")
    print(f"Hunger: {pigeon.hunger}")

    if DEBUG_MODE:
        print("\033[93mDebug mode:\033[0m")
        print(f"\033[93mOvereating: {pigeon.overeating}\033[0m")


def display_pigeon_menu(pigeon: Pigeon) -> None:
    print(f"\n=== {pigeon.name.upper()} ===\n")
    print(f"1. Examine {pigeon.name}.")
    print(f"2. Feed {pigeon.name}.")
    print("3. Main menu.")


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
