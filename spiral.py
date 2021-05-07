import turtle
# Создаем черепашку
t = turtle.Turtle()
# Скорость и цвет
t.speed(0)
colors= ('red', 'purple', 'blue', 'green', 'orange', 'yellow')
# Цикл спирали
for x in range (500) :
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)