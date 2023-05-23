import random
from utils.killers import Killers
from utils.survivors_perks import Perks

def generate_random_killer_survivor():
    random_killer = random.choice(Killers.killers)
    print("Random Killer:", random_killer)

def generate_random_perks():
    random_survivor = random.choice(list(Perks.__dict__.keys()))
    random_perks = getattr(Perks, random_survivor)
    random_perk = random.choice(random_perks)
    print("Random Perk from" + " " + random_survivor + ":", random_perk)    

def main():
    while True:
        print("\nChoose an option:")
        print("1. Random Killers")
        print("2. Random Perks")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            generate_random_killer_survivor()
        elif option == '2':
            generate_random_perks()
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()