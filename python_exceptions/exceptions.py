# An example of exception handling in Python 3.xx
# Adding pets to pound inventory and keeping PETA in business
# TODO: PUT THESE CLASSES IN SEPARATE FILES YOU BUM
from string import Template
# a little module that jazzes up console output
from termcolor import*


class PetTemplate(Template):
	# changing it because the standard is '$' and there's a price field
	delimiter = '#'
	
class Pet:
	# globalClassVar = 0 ... no cool private, public kw's in Python! 

	# default constructor
	def __init__ (self):
		try:
			# note the elusive curly braces for dictionary def - this is a mutable structure
			# also note that this is how we make structures and vars assigned to an instance (private)
			self.info = {'Name':"", 'Species':"", 'Age':0, 'Price':0}
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
		temp = PetTemplate("Name: #Name \t\t Species: #Species \t\t Age: #Age \t\t Price: $#Price")
		for pet in self.inventory:
			pet_info = temp.substitute(pet.info)
			print(pet_info)
	
	# add a new pet to the inventory
	def add(self):
		self.inventory.append(Pet())
	
	# determining the total pets in inventory
	def size(self):
		print(len(self.inventory)) 

def main():
	inventory = Inventory()
	user_dirs = "\nWhat would you like to do?\nEnter add, show, size or q to quit."
	prompt = colored('-->', 'cyan')

	# this flow subs for a switch in other languages
	while 1 == 1:
		print(user_dirs)
		user_in = input(prompt)
		
		if user_in == 'add':
			inventory.add()
			print(colored("SUCCESS!\n", 'green', attrs =['underline']))
		
		elif user_in == 'show':
			print(colored("Current Inventory:",'magenta', attrs = ['underline']))
			inventory.show()
			
		elif user_in == 'size':
			print(colored("Inventory Size:", 'magenta', attrs = ['underline']))
			inventory.size()
		
		elif user_in == 'q':
			print ("Peace out, you benevolent kitten cuddler.")
			return 
		
		else:
			print(colored("Invalid input.\n",'red'))
			
if __name__ == '__main__':
    main()
