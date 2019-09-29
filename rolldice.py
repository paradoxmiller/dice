#!/usr/bin/env python3

from graphics import *
import random
import sys

def yorn(question):
	reply = str(input(question+' Would you like to roll the dice? Y or N: ')).lower().strip()
	if reply[0] == 'y':
		return 0
	elif reply[0] == 'n':
		return 1
	else:
		return yorn("Please enter y or n: ")


while True:
	if(yorn('Roll?')):
		break
	dienum = random.randrange(1,7)
	x = 195
	y = 60
	xx = 400
	yy = 140

	#def die2():
		#roledie2()

	if dienum == 1:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
			c = Circle(Point(100,100),20)
			c.setFill("red")
			c.draw(win)
		main()

	if dienum == 2:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
			c = Circle(Point(50,50),20)
			c.setFill("red")
			c.draw(win)
			c2 = Circle(Point(150,150),20)
			c2.setFill("red")
			c2.draw(win)
		main()

	if dienum == 3:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
			c = Circle(Point(100,100),20)
			c.setFill("red")
			c.draw(win)
			c2 = Circle(Point(50,50),20)
			c2.setFill("red")
			c2.draw(win)
			c3 = Circle(Point(150,150),20)
			c3.setFill("red")
			c3.draw(win)
		main()
	
	if dienum == 4:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
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
		main()
		
	if dienum == 5:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
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
		main()
	

	if dienum == 6:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, x, y))
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
		main()

	#def roledie2():

	dienum = random.randrange(1,7)
	x = 450
	y = 90

	if dienum == 1:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
			c = Circle(Point(100,100),20)
			c.setFill("red")
			c.draw(win)
			win.getMouse() # pause for mouse click in window
			win.close()
		main()

	if dienum == 2:
		def main():
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
			win = GraphWin("Dice", 200,200)
			win.setBackground("black")
			win.master.geometry('%dx%d+%d+%d' % (200, 200, xx, yy))
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
