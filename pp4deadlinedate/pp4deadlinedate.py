import datetime     #import the datetime library


currentDate = datetime.date.today()     #display todays date using the date.today() method from the datetime library
print(currentDate)


def dateFunction(deadlinelv):           #parameter passed a string value containing a date
    deadlineDate = datetime.datetime.strptime(deadlinelv,'%d/%m/%Y').date() #cast the locally scoped variable to datetime format
    result = deadlineDate - currentDate #global variable currentDate used inside scope of the function
    result = str(result.days)           #.days function returns a total value formatted to days
    return result                       #return the total days to the function call

deadlinegv = input('Enter the deadline date (dd/mm/yyyy) ')
numOfDays = dateFunction(deadlinegv)    #call the dateFunction and store the return value in the numOfDays variable
print('There are ' + numOfDays + ' days until your deadline')
