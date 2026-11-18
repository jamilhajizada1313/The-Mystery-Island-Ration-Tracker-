# Case Study 3: The Mystery Island Ration Tracker 🏝️
# The Logic Focus: Accumulators, while loops, and breaking out of loops.
# The Scenario: A survival text-adventure game requires a system to track food rations. A player starts with total_food = 100 units. Each "day" of the game, a random or user-inputted amount of food is consumed.
# The Rules:
# Prompt the user to enter how much food was eaten today.
# Subtract that from the total.
# If the total drops to 20 or less, print a warning: "Alert: Rations dangerously low!".
# If the total hits 0 or goes negative, the loop must end immediately and print: "Game Over: Out of food. You survived X days!".


totalfood =100
foodEaten=0
days=0

while totalfood > 0:
    foodEaten=float(input('How much food did you eat today? '))
    totalfood=totalfood-foodEaten
    days=days+1
    if totalfood <= 0:
        print('Game Over: Out of food. You survive', days, 'day')
    elif totalfood <=20:
        print('Rations dangerously low!')

    





