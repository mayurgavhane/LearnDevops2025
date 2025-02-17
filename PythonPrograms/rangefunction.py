# for i in range(10):
#     print(i)

# total = 0
# expenses = []
# for i in range (7):
#     expenses.append(float(input('Enter your expenses:')))

#     total = sum (expenses)

#     print ("Your total spend was: ", total, sep='')  


total = 0
expenses = []

num_expenses = int (input("Enter your expense: "))

for i in range (num_expenses):
    expenses.append(float (input('Enter your expenses: ')))
    
    total= sum (expenses)