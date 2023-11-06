import turtle 

a = 10 # no of times
b = 255 #
c = 135 # angle
t = turtle.Turtle() # Define turt
turtle.colormode(b) #
t.fillcolor((a,b,c)) # All must be between 0 and 255
t.pencolor("red")

t.begin_fill()
for i in range(a): # Loops for length of a
	t.forward(b%c)
	t.left(c) # Must total to something divisible by 270
t.end_fill()


turtle.done()

print(a*b*c)

# Result: 344250