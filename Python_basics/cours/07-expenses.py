expenses = [10.50, 8, 5, 15, 20, 5, 3]

mysum = 0

for x in expenses:
    mysum = mysum + x

print('You spent $', mysum, sep = '')
print('You spent $', mysum, sep = '/')


total = sum(expenses) + 200 
print('You spent $', total, sep = '')

#use range -> ex8
total = 0
expenses = []
for i in range(2):
    expenses.append(float(input("Enter your seven last expense: ")))

total = sum(expenses)
print("You spent $", total, sep='')


#Inifinite number of expense
total = 0
expenses = []
num_expenses = int(input("Enter number# of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

print("You spent $", total, sep='')