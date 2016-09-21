# 1. Start with a message:
#  -- you encountered a dragon
# 2. while loop will keep the game going. 
# -- User must enter 1 or 2
# -- if user enteres something else, let them know they screwed up and give them option again
# 3. If they choose "run" (1 or 2), call them a coward and give them the option of playing again.
# -- if they don't want to play again you can run sys.exit (import sys)
# 4. if they choose "fight" (the not run option), then init the hero and dragon health
# -- ideally/bonus, hero and dragon are classes
# 5. ask the the user if they want to 1,2,3 (attack, spell, or defend)
# -- if user enteres something bogus, handle it (dragon gets a free shot or you just ask them again)
# -- optionally add a method to the hero class. hero.fight(), hero.spell()
# 6. update the dragon health based on the outcome
# -- import random
# 7. randomize the dragon's attack (based on the hero's ... did defend or spell)
# 8 update hero health
# 9. check if anyone is dead and handle
# 10. if both alive, repeat to 5

import random
import sys
import time

class Hero(object):
	def __init__(self):
		self.health = 10
		self.strength = 5
		self.defense = 0

	def alive(self):
		return self.health > 0

	def attack(self, enemy):
		damage = random.randint(0,3)
		if damage == 0:
			slowType("You missed the dragon!\n")
		else:
			enemy.health -= damage
			slowType("You got a hit on the dragon for " +str(damage)+ " damage points!\n")
			slowType("Now the dragon's health is " + str(enemy.health)+". Keep it up!\n")
		return damage

	def defend(self):
		self.defense = random.randint(0,3)

	def spell(self, enemy):
		spell_effect = random.randint(0,1)
		if spell_effect == 0:
			slowType("Your spell didn't affect the dragon. Quick attack before it burns you up!\n")
		else:
			enemy.health -= 5
			slowType("That spell you cast did a lot of damage! Nice magic!\n")
			slowType("The dragon's health is " +str(enemy.health)+ "\n")	

class Dragon(object):
	def __init__(self):
		self.health = 10
		self.strength = 5

	def alive(self):
		return self.health > 0

	def attack(self, hero, defense):
		damage = random.randint(0,3)
		if damage == 0:
			slowType("The dragon missed you!\n")
		else:
			if hero.defense:
				if damage - defense < 0:
					slowType("Your defense blocked the dragon\n")
				elif defense == 0:
					hero.health -= damage
					slowType("You failed to get your shield up in time.\n")
					slowType("The dragon hit you for " +str(damage)+ " damage points!\n")
				else:	
					hero.health -= (damage - defense)
					if defense > 0:
						slowType("You absorbed %s \n") % defense
					slowType("The dragon hit you for " +str(damage - defense)+ " damage points!\n")
			else:
				hero.health -= damage
				slowType("The dragon hit you for " +str(damage - defense)+ " damage points!\n")
		slowType("Now your health is " + str(hero.health)+". Watch out!\n")
		return damage				

def slowType(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

def play():
	slowType("You encounter a scary dragon!\n")
	slowType("What will you do?\n")
	fighting = True
	hero = Hero()
	dragon = Dragon()

	
	while fighting:
		hero.defense = 0

			slowType("Press 1 to fight...\n")
			slowType("Or 2 to flee.\n")
			player_move = input(">")

			if player_move not in {1,2}:
				slowType("Wrong. Enter a 1 or 2.\n")
				player_move = input(">")

			elif player_move == 2:
				slowType("You're running? Man, you're such a coward!\n")
				fighting = False

				slowType("Do you want to play again?\n")
				slowType("Press 1 for yes or 2 for no.\n")
				player_answer = input("Play again: yes or no?")
				if player_answer == 1:
					play()
				elif player_answer not in {1,2}:
					slowType("Invalid response.\n")
					slowType("Enter a 1 or 2.\n")
					player_answer = input("Play again: yes or no?")
				elif player_answer == 2:	
					slowType("Goodbye\n")
					sys.exit

			elif player_move == 1:
				slowType("Ok, you're going to fight this dragon!\n")
				slowType("What do you want to do?\n")
				slowType("Press 1 for attack...\n")
				slowType("Press 2 to defend with your shield...\n")
				slowType("Press 3 to launch a spell...\n")
				player_fight = input(">")

				if player_fight == 1:
					hero.attack(dragon)
					
					if not dragon.alive():
						slowType("You killed the dragon!\n")
						slowType("Do you want to play again?\n")
						slowType("Press 1 for yes or 2 for no.\n")
						player_answer = input("Play again: yes or no?")
						if player_answer == 1:
							play()
						elif player_answer not in {1,2}:
							slowType("Invalid response.\n")
							slowType("Enter a 1 or 2.\n")
							player_answer = input("Play again: yes or no?")
						elif player_answer == 2:	
							slowType("Goodbye\n")
							sys.exit

				elif player_fight == 2:
					hero.defend()
				
				elif player_fight == 3:
					hero.spell(dragon)
						
					if not dragon.alive():
						slowType("You killed the dragon!\n")
						slowType("Do you want to play again?\n")
						slowType("Press 1 for yes or 2 for no.\n")
						player_answer = input("Play again: yes or no?")
						if player_answer == 1:
							play()
						elif player_answer not in {1,2}:
							slowType("Invalid response.\n")
							slowType("Enter a 1 or 2.\n")
							player_answer = input("Play again: yes or no?")
						elif player_answer == 2:	
							slowType("Goodbye\n")
							sys.exit				
			
				else:
					slowType("That was a dumb move, what do you really want to do? Choose 1, 2 or 3.\n")
					player_fight = input(">")
					continue

				if dragon.alive():
					dragon.attack(hero, hero.defense)	
					
					if hero.health <= 0:
						slowType("The dragon burned you to a crisp and you're dead.\n")
						slowType("Want to play again?\n")
						slowType("Press 1 for yes or 2 for no.\n")
						player_answer = input("Play again: yes or no?")
						if player_answer == 1:
							play()
						elif player_answer not in {1,2}:
							slowType("Invalid response.\n")
							slowType("Enter a 1 or 2.\n")
							player_answer = input("Play again: yes or no?")
						elif player_answer == 2:	
							slowType("Goodbye\n")
							sys.exit
				
		# fighting = False
play()					