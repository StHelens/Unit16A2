def convertValues():
    L = input("Enter loan amount ")         #local variable L defined by user
    i = input("Enter intereset rate ")
    n = input("Enter number of payments ")
    L = int(L)                              #cast string value to an integer
    i = float(i)/12                         #cast string value to a float
    n = int(n)
    M=L*(i*(1+i)**n)/((1+i)**n-1)           #formula to calculate monthly repayements
    return M                                #return result of formula


MonthlyPayment = convertValues()            #call convertValues function store result in MonthlyPayment variable
print(MonthlyPayment)

MonthlyPayment = convertValues()
print(MonthlyPayment)
