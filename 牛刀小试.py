import turtle
turtle.bgcolor("black")
turtle.pensize(1)
colors=["red","yellow","blue","green","orange","purple"]
for x in range(200):
    turtle.forward(x*3/6+x)
    turtle.color(colors[x%6])
    turtle.left(360/6+1)
    turtle.width(x*6/200)
done
	
