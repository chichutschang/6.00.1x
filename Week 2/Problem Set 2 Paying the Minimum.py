#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
monthlyUnpaidBalance = balance
totalPayment = 0
month = 0

for month in range(12):
    month += 1
    print 'Month: %d' % month
     
    minimumMonthlyPayment = balance * monthlyPaymentRate   
    totalPayment += minimumMonthlyPayment
    print 'Minimum monthly payment: %.2f' % round(minimumMonthlyPayment, 2)   
        
    monthlyUnpaidBalance = (balance - minimumMonthlyPayment)
    
    interest = round(monthlyUnpaidBalance * (annualInterestRate / 12.0), 2)
    
    balance = round((monthlyUnpaidBalance + interest),2)
    print 'Remaining balance: %.2f' % balance 
    
print 'Total paid: %.2f' % totalPayment
print 'Remaining balance: %.2f' % round(balance, 2)
