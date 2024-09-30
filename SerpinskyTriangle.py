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
leo.speed(0)
leo.setpos(-WIDTH // 4, -HEIGHT // 4)
leo.color('green')


# l-system settings
gens = 7
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'
step = 5
angle = 120

'''def apply_rules(axiom):
   res = ''
    for chr in axiom:
        if chr ==chr_1:
            res+= rule_1
        else:
            res+= rule_2
    return res

    for gen in range(gens):
    input()
    print(f'generation {gen}: {axiom}')
    axiom = apply_rules(axiom)


    '''


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else
                    rule_2 if chr==chr_2 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-screen.window_width() // 2 + 20, -screen.window_height() // 2 + 20)
turtle.clear()
turtle.write(f'generation {gens}', align="left", font=("Arial", 30, "normal"))

axiom = get_result(gens, axiom)

for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        leo.forward(step)
    elif chr == '+':
        leo.right(angle)
    elif chr == '-':
        leo.left(angle)

screen.exitonclick()

