from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 20
x2 = -300
y2 = 190
x3 = -300
y3 = -80
x4 =-300
y4 =-200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("moon")
t1 = create_sprite("rory",x1,y1)
t2 = create_sprite("orantu",x2,y2)
t3 = create_sprite("devi",x3,y3)
t4 = create_sprite("circusmonk",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower
for i in range(33):
    x1 += 12
    x2 += 5
    x3 += 9
    x4 += 6

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.5)


# Section 4 - Winner
# TODO - complete the elif for player 2 winner

# - write another elif for player 3 and player 4
s5 = create_sprite("turtle",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("rory wins!")
 
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("orangutan wins!")

elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("devi wins!")

elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    s5.write("adopt me circus monkey wins!")


turtle.exitonclick()