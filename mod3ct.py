meal = float(input("enter meal total: ")) #this will tell the user to enter the total amount of the meal at the reataraunt and assign it to a variable
tip = float(0.18 * meal) #this calculates a value for the tip variable to be added to the equation for the bill
tax = float(0.07 * meal) #this calculates a value to the tax variable to be added to the equation for the bill
bill = meal + tip + tax # this will calculate the total cost of the meal with tip and tax included
print("The tip for this meal is:, $", tip) #this will display the dollar amount of the tip
print("the tax for this meal is:, $", tax) #this will display the dollar amount of the tax
print("The total of your bill is: $", bill) #this will dsiplay the total dollar amount of the bill