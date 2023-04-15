import os
from time import sleep
# cookbook = {
# 'ingredients': []str(""),
# 'meal': 'Yukihiro Matsumoto',
# 'prep_time': 'Rasmus Lerdorf',
# }
cookbook = {
'Sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10),
'Cakes': (['flour', 'sugar', 'eggs'], 'dessert', 60),
'Salads': (['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)}
# for dato in cookbook:
#     print("{}, {}".format(dato, cookbook[dato][-1]))
def printnames():
    for recipe in cookbook:
        print("{}".format(recipe))

def printrecipes():
	dato = str(input("What recipe do you want:\n"))
	dato = dato.capitalize()
	if dato in cookbook.keys():
		print(" Recipe for {}:".format(dato))
		print("   Ingredients list:	{}".format(cookbook[dato][0]))
		print("   To be eaten for	{}.".format(cookbook[dato][1]))
		print("   Takes {} minutes of cooking.".format(cookbook[dato][2]))
		input("\n\n\nPress Enter key for continue")
		os.system('clear')
	else:
		print("El producto no es")

def	add():
	Name = "Cakes"
	while Name in cookbook.keys():
		Name = str(input("What´s the name of the recipe do you want to add:\n"))
		Name = Name.capitalize()
		if Name in cookbook.keys(): print("This recipe already exists")
	ingredients = str(input("What´s the name of the ingredients:\n").split(' '))
	meal = str(input("Enter a meal type:\n"))
	cooktime = int(input("Enter a preparation time:\n"))
	cookbook[Name] = (ingredients, meal, cooktime)
	print("Your recipe was added!!")

def delete():
	Name = input("What recipe do you want to remove?\n").capitalize()
	while Name not in cookbook.keys():
		Name = input("This recipe does not exist, what recipe do you want to remove?\n").capitalize()
	del cookbook[Name]
	print("The recipe {} was deleted from the cookbook".format(Name))

def getchoice():
	while True:
		print("List of available option:\n	1: Add a recipe\n	2: Delete a recipe\n	3: Print a recipe\n	4: Print the cookbook\n	5: Quit\n")
		choice = input("Please select an option:	")
		if choice == '1':
			add()
		elif choice == '2':
			delete()
		elif choice == '3':
			printrecipes()
		elif choice == '4':
			printnames()
		elif choice == '5':
			quit()
		else:
			print("		Wrong character :/		")
			sleep(1)
			os.system('clear')
if __name__ == "__main__":
	print("Welcome to the Python Cookbook !\n")
	getchoice()