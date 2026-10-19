class Pigeon:
    def __init__(self, name: str) -> None:
        self.name = name
        self.life_stage = "Adult"  # probably use enum for stages later

        # basic needs
        self.hunger = 5

        # effects
        self.overeating = 0

    def feed(self) -> None:
        food_amount = 10

        if self.hunger - food_amount < 0:
            self.overeating += food_amount - self.hunger
            print(f"Test: {self.overeating} (overeating)")

        self.hunger = max(0, self.hunger - food_amount)
