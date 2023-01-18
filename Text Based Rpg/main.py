#importing modules
import random

#player classes
class Knight:
    def __init__(self):
        self.health = 150
        self.damage = 15
        self.money = 80

class Archer:
    def __init__(self):
        self.health = 100
        self.damage = 25
        self.money = 60

class Merchant:
    def __init__(self):
        self.health = 80
        self.damage = 5
        self.money = 1000

#enemy class
class Enemy:
    def __init__(self):
        self.name = random.choice(["Suspicious Turtle", "Python", "Giant Lizard", "Baby Seal", "Elite Grasshopper", "Flying Fish", "Wandering Eye", "Dung Beetle"])
        self.health = random.randint(50, 120)
        self.damage = random.randint(10, 15)
  
#Main program
def startGame():
    print("Welcome Adventurer, which class would you want to become?")
    print("Start by choosing one of the following classes")
    print("1. Knight (Tank)")
    print("2. Archer (Damage)")
    print("3. Merchant (Special)")

    choice = int(input("Choose your class: "))
    # Knight
    if choice == 1:
        player = Knight()
        print("\nKnight Stats:")
        print("Health:", player.health)
        print("Damage", player.damage)
        print("Gold:", player.money)
    # Archer
    elif choice == 2:
        player = Archer()
        print("\nArcher Stats:")
        print("Health:", player.health)
        print("Damage:", player.damage)
        print("Gold:", player.money)
    # Merchant
    elif choice == 3:
        player = Merchant()
        print("\nMerchant Stats:")
        print("Health:", player.health)
        print("Damage:", player.damage)
        print("Gold:", player.money)
        
    # Randomly Generate an enemy
    enemy = Enemy()
    print("\nWhile curiously exploring the world you have encountered a wild", enemy.name)
    while player.health > 0 and enemy.health > 0:
        
        # Action Phase
        print(enemy.name, "Health:", enemy.health)
        print("Your health:", player.health)
        print("\nWhat do you want to do?")
        print("1. Attack (Attack the enemy for the players damage value)" )
        print("2. Run (End player run)")
        print("3. Heal (70) (Randomly heal for a certain amount)")
        print("4. Special Attack (80) Extra rewards if enemy killed by this attack)")
        
        # Player input
        action = int(input())
        # Action 1 (Attack)
        if action == 1:
            enemy.health -= player.damage
            if enemy.health <= 0:
                print("You have defeated the enemy!")
                print("A wild", enemy.name, "has appeared")
                # Gain a flat bonus if enemy killed by special attack
                player.health += 10
                player.damage += 5
                player.money += 10
                enemy = Enemy() 
                # Scale the enemy
                enemy.health += random.randint(25, 45)
                enemy.damage += random.randint(2, 4)
            else:
                player.health -= enemy.damage  

                print("You have been hit! Your health is now", player.health)
                print("You hit the", enemy.name, "for", player.damage, "damage")
                
        # End the game if player chooses to run away
        elif action == 2:  

            print("You have ran away from the monster however as you were running you were too careless about your surrounding falling to your death")
            # End game
            break
    
        
        #heal the player for a random amount for money
        elif action == 3:  

            player.health += player.health * random.random()
            player.money -= 80

            print("You have healed, your health is now", player.health)
        #special attack that costs money 
        elif action == 4:  
            if player.money >= 20:
                print("You have this much gold left", player.money - 20)
                print("The", enemy.name, "has taken a hit")
                enemy.health -= random.randint(30, 60)
                # Reduce 20 gold
                player.money -= 80
                # Defeated the enemy
                if enemy.health <= 0:
                    # Defeating the enemy allows the player to gain some health and gold while increasing their damage
                    print("You have defeated the enemy!")
                    print("\nPlayer Status:")
                    print("Player Health:", player.health)
                    print("Player Damage:", player.damage)
                    print("Total Gold:", player.money)
                    # Enemy killed by special attack might give bonus stats
                    # Increase the players stats more since enemy killed by special attack instead of a normal attack
                    player.health += random.randint(30, 50)
                    player.damage += random.randint(2, 5)
                    player.money += random.randint(20, 60) 
                    
                    # Generate a random enemy
                    enemy = Enemy()  
                    print("\nYou have encountered another enemy:", enemy.name)
                    # Enemy difficulty scaling so they don't get one shot 
                    enemy.health += random.randint(25, 45)
                    enemy.damage += random.randint(2, 4)
            

                else:
                    # Player takes damage from enemy
                    player.health -= enemy.damage 

            else:  
              # if the player does not have enough gold display this and show them their money
              print("You don't have enough money to use this action!", "Gold:", player.money)
    # Print Game Over
    print("Game Over! You died")
              

# StartGame function
startGame()
