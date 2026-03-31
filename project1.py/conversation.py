# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("capybara_sunset")

s1 = create_sprite("lebron(1)", -200, 0)
s2 = create_sprite("fox", 200, 0)

s1.color("pink")
s2.color("white")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("Inside a capybra sunsets!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s2.write("Check New York City! They love to go there.", font = ("Arial", 12, "normal"))
window.update ()
time.sleep(1)

set_background("nyc")

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()