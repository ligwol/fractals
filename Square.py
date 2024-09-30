import turtle

# screen
WIDTH, HEIGHT = 900, 900
screen = turtle.Screen()
screen.setup(width=0.8, height=0.8)
screen.screensize(1000, 800)
screen.colormode(255)
screen.bgcolor(20, 20, 20)
screen.delay(0)

# turtle
leo = turtle.Turtle()
leo.pensize(1)
leo.speed(1)
leo.setpos(-screen.window_width() // 5 , screen.window_height() // 10 )
leo.color('white')


# l-system settings
gens = 3
axiom = 'F+F+F+F'
chr_1, rule_1 = 'F', 'FF+F+F+F+FF'
step = 3
angle = 90

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

for gen in range(gens):
    turtle.pencolor('white')
    turtle.goto(-screen.window_width() // 2 + 20, -screen.window_height() // 2 + 20)
    turtle.clear()
    turtle.write(f'generation {gens}', align="left", font=("Arial", 30, "normal"))

    axiom = get_result(gens, axiom)

    leo.setheading(0)
    leo.goto(-screen.window_width() // 5 , screen.window_height() // 10)
    leo.clear()

    length = step / pow(3, gen)
    for chr in axiom:
        if chr == chr_1:
            leo.forward(length)
        elif chr == '+':
            leo.right(angle)
        elif chr == '-':
            leo.left(angle)

screen.exitonclick()

