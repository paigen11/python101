print "Paige Niedringhaus"

# Arrays ... psyche. Lists.

animals = ['wolf', 'giraffe', 'hippo']
print animals
print animals[0]
print animals[-1]

# How do we push to the array / list? -- APPEND!
animals.append("croc")
print animals

# What about delete?
animals.remove('wolf')
print animals

# Error!
# animals.prepend('wolf')
# We can insert at any position with ... INSERT
animals.insert(0, 'zebra')
print animals
animals.insert(0, 'dog')

# remove via del
del animals[0]
print animals

# Pop, is just good old Pop
dc_class = ["Summer", "Jackson", "Danny", "Dave", "JT", "Eric", "Paige", "Brett", "Danielle", "Alex", "Dan", "Shirlette"]
# will sort, but not change the actual array
print sorted(dc_class)
# will sort and change the list
dc_class.sort()
# will reverse and change the list
dc_class.reverse()
print dc_class

# len method will work like .length in JS
print len(dc_class)

# indentation matters to Python!
for student in dc_class:
	print student

for i in range(1,10):
	print i
for i in range(1,len(dc_class)):
	print i

# a function is not called a function. It's defined by: def
def sayHello():
	print "Hello"

sayHello()

def say_hello_with_name(name):
	print "Hello, " + name

say_hello_with_name("Paige")

# make squares
squares = []
for i in range(1, 11):
	square = i ** 2
	squares.append(square)
print squares

# random list of digits
digits = [12, 235, 15, 213, 42, 23, 3215, 245, 342, 1234, 23, 41234214, 123, 2]
# max and min
print min(digits)
print max(digits)
print sum(digits)

# this is called 'list comprehension' - it's very succinct code
squares = [i** 2 for i in range(1,11)]
print squares

# step = the increment
print range(1,11,2)

# slice in python is all about the :
dc_team = ["Max", "Jake", "Rob", "Toby", "Natalie"]
team_part = dc_team[1:3]
print team_part
team_part = dc_team[1:-1]
print team_part
team_part = dc_team[:1]
print team_part
team_part = dc_team[2:]
print team_part
team_copy = dc_team
print dc_team
print team_copy
# will keep a connection so both will change when one does

# make a new list, independent
team_copy = list(dc_team)
team_copy.append("DeAnn")
print team_copy
print dc_team

team_copy = dc_team[:]
team_copy.append("DeAnn")
print team_copy
print dc_team
