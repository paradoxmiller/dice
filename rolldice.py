#!/usr/bin/env python3

from graphics import *
import random
import sys

#roll = input("Would you like to roll the die? Y or N")

dienum = random.randrange(1,7)



if dienum == 1:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(100,100),20)
		c.setFill("red")
		c.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()

if dienum == 2:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(50,50),20)
		c.setFill("red")
		c.draw(win)
		c2 = Circle(Point(150,150),20)
		c2.setFill("red")
		c2.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()

if dienum == 3:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(100,100),20)
		c.setFill("red")
		c.draw(win)
		c2 = Circle(Point(50,50),20)
		c2.setFill("red")
		c2.draw(win)
		c3 = Circle(Point(150,150),20)
		c3.setFill("red")
		c3.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()

if dienum == 4:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(150,50),20)
		c.setFill("red")
		c.draw(win)
		c2 = Circle(Point(50,50),20)
		c2.setFill("red")
		c2.draw(win)
		c3 = Circle(Point(150,150),20)
		c3.setFill("red")
		c3.draw(win)
		c4 = Circle(Point(50,150),20)
		c4.setFill("red")
		c4.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()
		
if dienum == 5:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(100,100),20)
		c.setFill("red")
		c.draw(win)
		c2 = Circle(Point(50,50),20)
		c2.setFill("red")
		c2.draw(win)
		c3 = Circle(Point(150,150),20)
		c3.setFill("red")
		c3.draw(win)
		c4 = Circle(Point(50,150),20)
		c4.setFill("red")
		c4.draw(win)
		c5 = Circle(Point(150,50),20)
		c5.setFill("red")
		c5.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()


if dienum == 6:
	def main():
		win = GraphWin("Circle", 200,200)
		win.setBackground("black")
		c = Circle(Point(150,150),20)
		c.setFill("red")
		c.draw(win)
		c2 = Circle(Point(150,50),20)
		c2.setFill("red")
		c2.draw(win)
		c3 = Circle(Point(150,100),20)
		c3.setFill("red")
		c3.draw(win)
		c4 = Circle(Point(50,150),20)
		c4.setFill("red")
		c4.draw(win)
		c5 = Circle(Point(50,100),20)
		c5.setFill("red")
		c5.draw(win)
		c6 = Circle(Point(50,50),20)
		c6.setFill("red")
		c6.draw(win)
		win.getMouse() # pause for mouse click in window
		win.close()
	main()

