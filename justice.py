# author: Hendrix2005

import turtle
hendrix = turtle.Turtle()
sides = 5
angle = 150 - (180 * (sides - 2) / sides)
length = 100
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for number in numbers:
	hendrix.forward(100)
	hendrix.left(angle)


