import turtle

#screen
WIDTH, HEIGHT = 900, 900
screen = turtle.Screen()
screen.setup(width=0.8, height=0.8)
screen.screensize(1000, 800)
screen.colormode(255)
screen.bgcolor(52, 46, 55)
screen.delay(0)

#turtle
leo = turtle.Turtle()
leo.pensize(2)
leo.speed(0)
leo.color(240, 168, 104)


# l-system settings
gens = 20
axiom = 'A'
chr_1 , rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'
step = 30
angle = 60

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
    return ''.join([rule_1 if chr == chr_1 else rule_2 for chr in axiom])

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
    if chr == chr_1:
        leo.left(60)
        leo.forward(step)
    elif chr == chr_2:
        leo.right(60)
        leo.forward(step)

screen.exitonclick()

