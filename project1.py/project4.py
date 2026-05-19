from utils import *

# Section 1 - setup
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # my background
set_background("monza16")

# my variables
wins = 0
cars= 0
cars_list=[]
#goal of game is to get an eagle trophy(s)
# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Getting the eagle trophy!!!
def get_control():
    global wins, cars


    cars += 1
    x = random.randint(-300,300)
    y = random.randint(-300,200)
    f1 = create_sprite("omg",x,y)
    cars_list.append(f1)


def trophy():
    global wins, cars
    if cars >= 200:
        wins += 1
        cars-=200
        x = random.randint (-200,200)
        y = random.randint (-200,200)
        create_sprite("eagle",x,y)
        for i in range(200):
            f1 = cars_list.pop()
            f1.hideturtle()

# TODO - key and action
window.onkeypress(get_control,"space")
# TODO - 2nd key and action
window.onkeypress(trophy,"p")




# Section 3 - game loop
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
window.listen()
for i in range(1000000000):
    m1.clear()
    #m1.write(f"wins:{wins}\nCost:{cost}\ncars: {cars}",font=("Arial",30,"normal") )

    # game loop
    #cars += wins
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"you have {cars} cars \n you have {wins} wins \n you need to get 200 cars to get a win!",font = ("Arial", 10, "normal"))

    # end game
    #if cars == 0:
        #break

    time.sleep(0.01)
    window.update()