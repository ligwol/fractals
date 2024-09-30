import turtle

# Screen settings
WIDTH, HEIGHT = 900, 900
screen = turtle.Screen()
screen.setup(width=0.8, height=0.8)
screen.screensize(1000, 800)
screen.colormode(255)
screen.bgcolor(20, 20, 20)
screen.delay(0)

# Turtle settings
leo = turtle.Turtle()
leo.pensize(2)
leo.speed(0)  # Fastest drawing speed
leo.penup()
leo.goto(0, -screen.window_height() // 3)  # Start higher up
leo.pendown()
leo.color('green')
leo.setheading(90)  # Facing up

# L-system settings
gens = 6
axiom = 'XY'  # Start with 'X'
chr_1, rule_1 = 'F', 'FF'  # For 'F'
chr_2, rule_2 = 'X', 'F[+X]F[-X]+X'  # For 'X'
step = 3  # Length of each segment
angle = 22.5  # Angle to turn
stack = []

def apply_rules(axiom):
    new_axiom = ''
    for chr in axiom:
        if chr == 'X':
            new_axiom += rule_2  # Apply rule for X
        elif chr == 'F':
            new_axiom += rule_1  # Apply rule for F
        else:
            new_axiom += chr  # Keep the character as is
    return new_axiom

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

# Generate the complete axiom after all generations
axiom = get_result(gens, axiom)

# Draw the L-system
for chr in axiom:
    if chr == chr_1:  # Move forward for 'F'
        leo.forward(step)
    elif chr == '+':  # Turn right for '+'
        leo.right(angle)
    elif chr == '-':  # Turn left for '-'
        leo.left(angle)
    elif chr == '[':  # Save state on '['
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif chr == ']':  # Restore state on ']'
        angle_, pos_ = stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

# Finalize drawing
screen.exitonclick()
