# dictionaries function like JS objects
# key-value pairs

zombie0 = {
	'speed':10,
	'power':6,
	'hunger':5,
	'name':'Joe'
}

print zombie0
print zombie0['speed']

zombie0['weapon'] = 'axe'
zombie0['position_x'] = 23
print zombie0


# You can delete with the del keyword
zombie0['huh'] = 'pointless'
del zombie0['huh']
print zombie0

# for loops through dictionaries start with the property placeholder followed by key-value
for key, value in zombie0.items():
	print "The key is " + key + " with a value of: " + str(value)
	print zombie0[key]

# eliminate value and just get the value from the dict[key]
for key in zombie0:
	print zombie0[key]

# you can sort the dictionary in natural order
for key in sorted(zombie0):
	print key+': '+str(zombie0[key])

# like JS, you can put your dictionaries in lists! (or tuples)
zombies = [] # zombies is an empty list
zombies.append({
	'speed':5,
	'power':16,
	'hunger':9,
	'name':'Tim'
})

for zombie in zombies:
	print zombie['name']

# just like JS you can assign a list, to a dictionary
zombies[0]['victims'] = ['Jane', 'Zane', 'Bill']
print zombies

# just like JS you can assign a dictionary to a dictionary
zombies[0]['super_mode'] = {
	#at night...
	'power': 23,
	'hunger': 20,
	'weapon': 'bat'
}			

# zombies[0].super_mode.power -- in JS
print zombies[0]['super_mode']['power']