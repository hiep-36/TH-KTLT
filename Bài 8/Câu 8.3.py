print("Le Hoa Hiep")
print("235752021610073")
import turtle

colors = ["red", "blue", "light green"]  
painter = turtle.Turtle()
painter.pensize(3)
for i in range(12):
    color = colors[i % len(colors)]  
    painter.pencolor(color)
    painter.circle(100)  
    painter.right(30)  
    painter.left(60)  
    painter.setposition(0, 0)  

painter.hideturtle()
turtle.done()
