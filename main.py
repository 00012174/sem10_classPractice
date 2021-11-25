class Person:
	def __init__(self, first, last):
		self.first = first
		self.last = last
	def printname(self):
		print(self.first, self.last)
class DogName:
	def __init__(self, first):
		self.first = first
	def printname(self):
		print(self.first)


if __name__ == '__main__':
	Person1 = Person("Max", "Khabarov")
	Person2 = Person("Sardorchik", "Shukurov")
	DogName1 = DogName("Sharik")
	Person1.printname()
	Person2.printname()
	DogName1.printname()
