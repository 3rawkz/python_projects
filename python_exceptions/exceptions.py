# An example of exception handling in Python 3.xx
# Adding pets to pound inventory and keeping PETA in business
# TODO: PUT THESE CLASSES IN SEPARATE FILES YOU BUM
from string import Template

class PetTemplate(Template):
	delimiter = '#'  # changing it because the standard is '$' and there's a price field
	
class Pet:
	# note the elusive curly braces for dictionary def - this is a mutable structure
	info = {'Name':"", 'Species':"", 'Age':0, 'Price':0}
	
	# default constructor
	def __init__ (self):
		try:
			self.info['Name'] = input("Name: ")
			self.info['Species'] = input("Species: ")
			self.info['Age'] = int(input("Age: "))
			self.info['Price'] = float(input("Price: "))
		
		# would be a silly way to 'handle' this exception... would want to use diff in val
		except Exception as e:
			print (e)
			print('This is an example!\nCare about record integrity we do not!')
		
class Inventory:
	inventory = []
	
	# print current inventory
	def show(self):
		temp = PetTemplate("Name: #Name Species: #Species Age: #Age Price: $#Price")
		for pet in self.inventory:
			print(temp.substitute(pet.info))
	
	# add a new pet to the inventory
	def add(self):
		self.inventory.append(Pet())

def main():
	inventory = Inventory()

	print("What would you like to do?\nEnter add, show, or quit.")
	user_in = input('-->')
	
	# this flow subs for a switch in other languages
	while user_in != 'quit':
		if user_in == 'add':
			inventory.add()
			print("Entry successfully added.\n________________________\n")
			print("What would you like to do?\nEnter add, show, or quit.")
			user_in = input('-->')
		
		elif user_in == 'show':
			print("Current Inventory:\n___________________")
			inventory.show()
			print("\nWhat would you like to do?\nEnter add, show, or quit.")
			user_in = input('-->')
		
		else:
			print("Follow directions. Who hired you?")
			print("What would you like to do?\nEnter add, show, or quit.")
			user_in = input('-->')
		
	return ("Peace out, you benevolent kitten cuddler.")
	
if __name__ == '__main__':
    main()
