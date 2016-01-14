#width = 20
#height = 5

#area = width * height
#print(area)

#perimeter = 2*height + 2 *width
#print(perimeter)
#perimeter = 2*(width+height)
#print(perimeter)

salary = input("Please enter your salary ") #prompt for salary and store in global variable as a string
bonus = input("Please enter your bonus ")
salary = int(salary)                        #cast the string variable to an integer
bonus = int(bonus)
payCheck = salary + bonus                   #calculate the total
print (payCheck)