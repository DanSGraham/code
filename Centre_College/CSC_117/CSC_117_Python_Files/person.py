#
#Practice with Classes
#By Daniel Graham

class Person:
	def __init__(self, aName, isCalled, Quest):
		"This is the constructor for the Person class"
		self.name = aName
		self.called = isCalled
		self.quest = Quest
			
	def __str__(self):
		"Return a string used for printing this Person"
		result = self.name
		if self.called:
			result = result + '  (' + self.called +')' + ", who's quest is " + self.quest
		return result
			
def TestPerson():
	"This runs a simple test of the Person class"
	bugs = Person('Bugs Bunny', 'Dat Wascally Rabbit', 'to seek the holy grail')
	runner = Person('Road Runner', 'Speedy', 'to venture to Camelot')
	tom = Person('Tom Riddle', 'Voldemort', "to slay HARRY POTTER!")
	print bugs
	print runner
	print tom
TestPerson()
