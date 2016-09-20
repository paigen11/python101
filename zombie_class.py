class Zombie(object):
	def __init__(self, type, speed, strength, weapon, health, hunger):
		self.type = type
		self.speed = speed
		self.strength = strength
		self.weapon = weapon
		self.health = health
		self.hunger = hunger

zombie0 = Zombie('basic', 5, 12, 'axe', 23, 9)
print zombie0
print zombie0.speed
print zombie0.weapon