#!/usr/bin/python3

from models.rectangle import Rectangle
class Square(Rectangle):
	def __init__(self, size,  x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	def __str_(self):
		return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

	@property
	def size(self):
		return self.width

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("x must be an integer")
		elif value < 0:
			raise ValueError("x must be >= 0")
		self.width = value
		self.height = value

