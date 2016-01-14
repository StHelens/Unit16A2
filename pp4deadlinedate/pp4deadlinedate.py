import datetime


currentDate = datetime.date.today()
print(currentDate)


def dateFunction(deadlinelv):
    deadlineDate = datetime.datetime.strptime(deadlinelv,'%d/%m/%Y').date()
    currentDate = datetime.date.today()
    result = deadlineDate - currentDate
    result = str(result.days)
    return result

deadlinegv = input('Enter the deadline date (dd/mm/yyyy) ')
numOfDays = dateFunction(deadlinegv)
print('There are ' + numOfDays + ' days until your deadline')
