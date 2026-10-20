class Pigeon:
    def __init__(self, name: str) -> None:
        self.name = name
        self.is_adopted = False
        self.life_stage = "Adult"  # probably use enum for stages later
        self.max_health = 100
        self.current_health = 100

        # basic needs
        self.hunger = 5

        # effects
        self.overeating = 0

    def feed(self) -> None:
        food_amount = 10

        if self.hunger - food_amount < 0:
            self.overeating += food_amount - self.hunger

        self.hunger = max(0, self.hunger - food_amount)

        self.apply_overeating_effects()

    def apply_overeating_effects(self) -> None:
        if self.overeating <= 20:
            return

        self.current_health = max(
            0, self.current_health - (self.overeating - 20)
        )

    def check_welfare(self) -> None:
        if self.current_health <= 0:
            self.is_adopted = True
