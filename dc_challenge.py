# 1) Declare two variables, a string and an integer named "fullName" and "age". Set them equal to your name and age.

# Python is dynamic so we don't need a var. Just make them
full_name  ="Paige Niedringhaus"
age = 27


# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

# No such thing as push, but who cares, there's no such thing as an array.
# There are lists. And lists have append
my_array = []
my_array.append(full_name)
my_array.append(age)


# // 3) Write a simple function that takes no parameters called "sayHello". 
# // Make it print "Hello!" to the console when called.
# // Call the function.
def say_hello():
	print "Hello!"

say_hello()

# // 4) Declare a variable named splitName and set it equal to
# // fullName split into two seperate objects in an array.
# // (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# // equal ["John", "Smith"].)
# // Print splitName to the console.
# // HINT: Remember to research the methods and concepts listed in the instructions PDF.
split_name = full_name.split()
print split_name


# // 5) Write another simple function that takes no parameters called "sayName".
# // When called, this function should print "Hello, ____!" to the console, where the blank is 
# // equal to the first value in the splitName array from #4.
# // Call the function.  (In our example, "Hello, John!" would be printed to the console.)
def say_name():
	print "Hello, %s!" % split_name[0]
	string = "Hello, {}"
	print string.format(split_name[0], 'DigitalCrafts')
say_name()

# // 6) Write another function named myAge.  This function should take one parameter: the year you 
# // were born, and it should print the implied age to the console.
# // Call the function, passing the year you were born as the argument/parameter.
# // HINT: http://www.w3schools.com/js/js_functions.asp
import datetime
def myAge(birth_year):
	now = datetime.datetime.now()
	print now.year - birth_year

myAge(1989)

# // 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# // HINT: Consider using a 'for loop'.

# function sum_odd_numbers() {
#     var sum = 0;

#     // Write your code here

#     console.log(sum);
# }

def sum_odd_numbers():
	sum = 0
	for i in range(1, 5000):
		if i % 2 != 0:
			sum += i
	print sum		

sum_odd_numbers()