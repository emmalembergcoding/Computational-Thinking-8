orangutan_points = 0
chimpanzee_points = 0
capuchin_points = 0

print ("Take this mystery quiz to see what you are?")
print ("")
print ("")
print ("")

answer1 = input ("What is your ideal day? A: Sushi on the beach B: Walking in the amazon rainforest C: Going to the maldives ")
if answer1 == "A" or answer1 == "a":
    orangutan_points += 1
elif answer1 == "B" or answer1 == "b":
    chimpanzee_points += 1
if answer1 == "C" or answer1 == "c":
    capuchin_points += 1
 
print ("")
print ("")
print ("")
print ("")

answer2 = input ("What is your favorite weather? A: Rainbow B: Rainy C: Sunny?  ")
if answer2 == "A" or answer2 == "a":
    orangutan_points += 1
if answer2 == "B" or answer2 == "b":
    chimpanzee_points += 1
if answer2 == "C" or answer2 == "c":
    capuchin_points += 1
print ("")
print ("")
print ("")
print ("")
print ("")

answer3 = input("What is your favorite color A: orange B: black C: yellow?")
if answer3 == "A" or answer3 == "a":
    orangutan_points += 1
if answer3 == "B" or answer3 == "b":
    chimpanzee_points += 1
elif answer3 == "C" or answer3 == "c" :
    capuchin_points += 1
print ("")
print ("")
print ("")
print ("")

answer4 = input ("Which food is your favorite? A: Bananas B: Coconut C: Dragonfruit ")
if answer4 == "A" or answer4 == "a":
    orangutan_points += 1
if answer4 == "B" or answer4 == "b" :
    chimpanzee_points += 1
if answer4 == "C" or answer4 == "c":
    capuchin_points += 1

print ("")
print ("")
print ("")
print ("")
print ("")


answer5 = input ("What is your ideal vacation A: LA B: Greece C: South Korea?")
if answer5 == "A" or answer5 == "a":
    orangutan_points += 5
if answer5 == "B" or answer5 == "b":
    capuchin_points += 1
if answer5 == "C" or answer5 == "c":
    chimpanzee_points += 1
print ("")
print ("")
print ("")
print ("")

answer6 = input ("Pick a drink A: Cannon ball starbucks drink B: Lemonade C:Coca cola?")
if answer6 == "A" or answer6 == "a":
    orangutan_points += 2
if answer6 == "B" or answer6 == "b":
    chimpanzee_points += 2
if answer6 == "C" or answer6 == "c":
    capuchin_points += 2
print ("")
print ("")
print ("")
print ("")
if orangutan_points > chimpanzee_points and orangutan_points > capuchin_points:
    print("You are most alike an orangutan!")
elif chimpanzee_points > capuchin_points and chimpanzee_points > capuchin_points:
    print("You are most alike an chimpanzee monkey!")
elif capuchin_points > orangutan_points and capuchin_points > chimpanzee_points:
    print("You are most alike a capuchin monkey")







    