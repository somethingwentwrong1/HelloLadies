## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## is-a
class Dog(Animal):

	def _init_(self, name):
		## has-a
		self.name = name
		
## is-a
class Cat(Animal):

	def _init_(self, name):
		## has-a
		self.name = name
		
## is-a
class Cat(Animal):

	def __init__(self, name):
		## has-a
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## has-a
class Employee(Person):

	def __init__(self, name, salary):
		## has-a
		super(Employee, self).__init__(name)
		## is-a
		self.salary = salary
		
## has-a
class Fish(object):
	pass
	
## is-a
class Salmon(Fish):
	pass
	
## is-a
class Halibut(Fish):
	pass

	
## rover is-a Dog
rover = Dog("Roger")

## is-a
satan = Cat("Satan")

## has-a
mary = Person("Mary")

## is-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## has-a
harry = Halibut()