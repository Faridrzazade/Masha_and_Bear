
import os
from random import randint

class Masha:
    def __init__(self, name, hand_strength, power_sword, max_soul=100, min_soul=0):
        self.name = name
        self.hand_strength = hand_strength
        self.power_sword = power_sword
        self.max_soul = max_soul
        self.min_soul = min_soul
        self.extra_soul = randint(30, 80)
        self.soul = max_soul
        self.sword_uses = 3
        self.extra_soul_used = False

    def attack(self):
        if self.sword_uses > 0:
            damage = self.hand_strength + self.power_sword
            print(f"{self.name} attacks with a damage of {damage}!")
            self.sword_uses -= 1
            if self.sword_uses == 0:
                print("Masha's sword has been used up!")
            return damage
        else:
            print("Masha's sword has already been used up!")
            return 0

    def use_extra_soul(self, bear):
        if not self.extra_soul_used:
            self.soul += self.extra_soul
            if self.soul > self.max_soul:
                self.soul = self.max_soul
            self.extra_soul_used = True
            print(f"{self.name} used extra soul. Soul is increased to {self.soul}!")
            
    def take_damage(self, damage):
        self.soul -= damage
        if self.soul <= 0:
            print(f"{self.name} lost the battle!")
            return True
        else:
            print(f"{self.name} has {self.soul} soul left.")
            return False


class Bear:
    def __init__(self, name, paw_damage, max_soul=150, min_soul=0):
        self.name = name
        self.paw_damage = paw_damage
        self.max_soul = max_soul
        self.min_soul = min_soul
        self.soul = max_soul

    def attack(self):
        print(f"{self.name} attacks with a damage of {self.paw_damage}!")
        return self.paw_damage

    def take_damage(self, damage):
        self.soul -= damage
        if self.soul <= 0:
            print(f"{self.name} lost the battle!")
            return True
        else:
            print(f"{self.name} has {self.soul} soul left.")
            return False


def main():
    masha = Masha("Masha", randint(10, 15), randint(15, 20))
    bear = Bear("Bear", randint(17, 23))

    while True:
        action = input("Press Enter to attack or 'e' to use extra soul: ")
        os.system("clear")

        if action.lower() == "e":
            masha.use_extra_soul(bear)
        
            
        elif masha.sword_uses > 0:
            masha_attack_damage = masha.attack()
        else:
            masha_attack_damage = masha.hand_strength 
        if bear.take_damage(masha_attack_damage):
                break
            
        bear_attack_damage = bear.attack()
        if masha.take_damage(bear_attack_damage):
                break
                


if __name__ == "__main__":
    main()
