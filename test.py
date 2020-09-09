# pROJECT USING TURTLE graphics in Python.
# Let's make spaceship-2d game in Python.
# You need to import turtle graphics module first.
import turtle as joy
from random import choice
# enemies are located randomly at x,y position  that's why import choice from 
# random module.

joy.bgpic('space.png')
screen=joy.Screen()
screen.screensize(1000,1000)
# screen setup 1000,1000 is the height,width of the screen.
x=[]
y=[]
total_enemy=10
for i in range(total_enemy):
	x1=choice(range(-500,300))
	y1=choice(range(-500,500))
	x.append(x1)
	y.append(y1)
# 100 enemies are there.
# YOu can make 200 or 500 or 1000 enemies. Just chenge the value of total_enemy.


# mac is a player who kill all the enemies. 
mac=joy.Turtle()
# shape of ypur player is turtle. and its size is 2 
mac.shape('turtle')
mac.turtlesize(2)
mac.color('red')
# mac color is red
mac.penup()
mac.seth(90)
mac.goto(-600,-280)
# mac goto the corner of the windows screen..

def fd():
	mac.fd(10)
def bd():
	mac.back(10)
def rt():
	mac.right(90)

def lt():
	mac.left(90)	

# when you press key 'a' than it will go forward .
# IF you type 'a' key 10 times so it will go 10 times 10 step forward with speed. 
# IF you type 'b' key 10 times so it will go 10 times 10 step backward with speed. 
# IF you type 'c' key 10 times so it will go 10 times 10 times rotate 90 degrees right. 
# IF you type 'd' key 10 times so it will go 10 times rotate 90 degrees. 

joy.listen()
joy.onkeypress(fd,'a')
joy.onkeypress(bd,'b')
joy.onkeypress(rt,'c')
joy.onkeypress(lt,'d')

	
name=['p','q','r','s','t','u','v','w','x','y','z']
# name list is the name of all the enemies. IF you make 20 enemies so used 20 names.
def rulers():
	for i in range(10):
		name[i]=joy.Turtle()
		name[i].shape('turtle')
		name[i].penup()
		name[i].goto(x[i],y[i])

rulers()
# rulers function is used to create and set enemies at desired location.
def pos():
	a,b=mac.pos()
	angle=mac.heading()
	c=joy.Turtle()
	# C is the new turtle. so this is used for your shooting.
	# when your player shoot than it will create dots.
	c.shape('circle')
	# dots are circle.

	c.penup(),c.speed('fastest')
	angle=mac.towards(0,0)
	#print(angle)
	if angle<90:
		c.seth(90)
		c.goto(a,b+100)
		v1,v2=a,b+100
	elif angle<180 and angle>=90:
		c.goto(a+100,b+100)
		v1,v2=a+100,b+100
	elif angle>180 and angle<270 :
		c.goto(a+100,b)
		v1,v2=a+100,b
	elif angle>270 and angle<360:
		c.goto(a-100,b)
		v1,v2=a-100,b	
	else:
		c.goto(a+30,b+30)		
		v1,v2=a+30,b+30
	#print(a,b)
	for i in range(len(x)):
		
		if ((x[i]-v1)**2+(y[i]-v2)**2 )**0.5 <50:
			print('win')
			name[i].hideturtle()
		else:
			pass
joy.onkeypress(pos,'w')
# when you type w key it will do shoot and shoot. 10 times w key than 10 times shoot.
# when your one  enemy kill  you get win in output and enemy kill it means it hide.
# so this is all about Space ship game.

#print(x,y)
#for i in range(10):
#	a=joy.Turtle()
#	a.shape('turtle')
#	a.penup()
#	a.goto(x[i],y[i])
	


joy.mainloop()

