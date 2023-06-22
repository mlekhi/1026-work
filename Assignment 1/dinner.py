# Developed by: Maya Lekhi
# Date: Feb 2, 2023
# Desc: a program to find the meals that match the dietary preferences of dinner invitees and finds according cost
# Inputs: invitee number, dietary preferences for each invitee, tip amount
# Output: orders of each meal, cost per meal, total cost (before and after tax & tip)

# user will input number of invitees here
invitees = int(input('Please enter the number of invitees:'))

# declaring and initializing cost & count variables for each food
pizzaCount = 0
pastaCount = 0
falafelCount = 0
steakCount = 0
bevCount = 0
pizzaCost = 0
pastaCost = 0
falafelCost = 0
steakCost = 0
bevCost = 0

# loop to determine the dietary preferences of each invitee and add to the cost accordingly
for i in range(invitees):
    # user will input the dietary preferences of each individual invitee
    print('Please enter the order details for invitee Number {}/{}'.format(i+1,invitees))
    ketoMeal = input('Do you want a keto friendly meal?')
    veganMeal = input('Do you want a vegan meal?')
    glutenFreeMeal = input('Do you want a Gluten-free meal?')
    print('--------------------')
    if ketoMeal == 'y' and veganMeal == 'y' and glutenFreeMeal == 'y':
        falafelCount += 1
        falafelCost += 52.99
    elif ketoMeal == 'y' and veganMeal == 'y':
        pizzaCount += 1
        pizzaCost += 44.50
    elif ketoMeal == 'y' and glutenFreeMeal == 'y':
        steakCount += 1
        steakCost += 49.60
    elif veganMeal == 'y':
        pastaCount += 1
        pastaCost += 48.99
    else:
        bevCount += 1
        bevCost += 5.99

# calculating total cost
dinnerCost = pizzaCost + pastaCost + falafelCost + steakCost + bevCost

# user will input tip amount here
tipAmount = int(input('How much do you want to tip your server (% percent)?'))

# printing invitees with each meal & cost of each meal type based on their dietary preferences inputted earlier
print('\nYou have %d invitees with the following orders:' %(invitees))
print('%d invitees ordered Pizza. The cost is: $%.2f'%(pizzaCount, pizzaCost))
print('%d invitees ordered Pasta. The cost is: $%.2f'%(pastaCount, pastaCost))
print('%d invitees ordered Falafel. The cost is: $%.2f'%(falafelCount, falafelCost))
print('%d invitees ordered Steak. The cost is: $%.2f'%(steakCount, steakCost))
print('%d invitees ordered only beverage. The cost is: $%.2f\n'%(bevCount, bevCost))


# calculating total cost, including with tax and tip
print('The total cost before tax is $%.2f'%(dinnerCost))
print('The total cost after tax is $%.2f'%(dinnerCost*1.13))
finalCost = round(dinnerCost * 1.13 * (1+(tipAmount / 100)))
print('The total cost after %d%% tip is $%d' %(tipAmount, finalCost))


