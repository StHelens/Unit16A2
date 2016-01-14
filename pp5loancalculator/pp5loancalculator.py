def convertValues():
    L = input("Enter loan amount ")
    i = input("Enter intereset rate ")
    n = input("Enter number of payments ")
    L = int(L)
    i = float(i)/12
    n = int(n)
    M=L*(i*(1+i)**n)/((1+i)**n-1)
    return M


MonthlyPayment = convertValues()
print(MonthlyPayment)

MonthlyPayment = convertValues()
print(MonthlyPayment)
