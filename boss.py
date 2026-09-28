import random
from enemy import Enemy 

class BOSS(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100)
        self.attack_power = 15

    def attack(self):
        """Return a random amount of damage."""
        attackStyle = random.randint(1, 3)
        if attackStyle == 1:
            print("FIREBALL")
            return 4 * random.randint(1, 2)
        elif attackStyle == 2:
            print("LAZZERBEAM")
            return 20
        elif attackStyle == 3:
            print("SWORD SWING")
            return self.attack_power() * random.randint(1, 3)

