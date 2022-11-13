# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:59:14 2022

@author: jiaxi
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# enter input data
Sales_Price = float('400000')

Down_Payment =  float('20')
Loan_Amount = Sales_Price*(1-Down_Payment/100)
Mortgage_Type =  float('30')
Loan_Term = int(12*Mortgage_Type)
Interest_Rate =  float('7.1')

# calculate monthly interest rate 
r = (Interest_Rate)/(12*100)
R = 1 +(Interest_Rate)/(12*100)

# enter formular 
X = Loan_Amount * r * (1 + r)** Loan_Term / ((1 + r)** Loan_Term - 1)

Monthly_Interest = []
Monthly_Balance  = []
for i in range(1,Loan_Term+1):
    Interest = Loan_Amount*(R-1)
    Loan_Amount = Loan_Amount - (X-Interest)
    Monthly_Interest = np.append(Monthly_Interest,Interest)
    Monthly_Balance = np.append(Monthly_Balance, Loan_Amount)
    
    
# Question a)
print("a1. Monthly Payment for this Mortgage(P & I) is: = " + str('$')+str(np.round(X,2)))

print("a2. Final payment is: = " + str('$')+str(np.round(Monthly_Balance[358],2)))

print("a3. Final balance is: = " + str('$')+str(np.round(Monthly_Balance[359],2)))

print("a4. Total principal paid over the life of the loan: = " + str(np.round(Loan_Term*X-sum(Monthly_Interest),2)))

print("a5. Total interest paid over life cycle of the loan is: = " + str('$') + str(np.round(np.sum(Monthly_Interest),2)))

print("a6. Total  paid over the life of the loan: = " + str(np.round(Loan_Term*X,2)))


# Question b)
plt.plot(range(1,Loan_Term+1),Monthly_Balance,'b',lw=2)
plt.xlabel('month')
plt.ylabel('monthly loan balance ($)')
plt.show()
plt

# Question c)
c = pd.DataFrame(Monthly_Interest)
c.columns = ["Monthly_Interest"]
c["Monthly Payment"] = X
c["Monthly Principal Payment"] = X - Monthly_Interest
c2= c.drop('Monthly Payment', 1)
c2.plot()
print("c. Around the 245th month, the principal and interest payments cross")

plt.plot(range(1,Loan_Term+1),Monthly_Interest, 'r',lw=2)
plt.xlabel('month')
plt.ylabel('monthly interest ($)')


# Question d)

rinv = float('0.04')
# enter points
# when point = 0
points = float('0')

second = []

for j in range(0, Loan_Term - 1):
    second2 = np.exp(j * rinv/12)
    pmt_second = X * second2
    second = np.append(second, pmt_second)


first =( Sales_Price*(Down_Payment/100) + points/1000 * Loan_Amount ) * np.exp(rinv * Loan_Term / 12)

FutureValue = first + np.sum(second)

print("d1. future value with 20% down payment and 7.1% annual mortgage is" + str('$') + str(np.round(FutureValue,2)))

## re- run 
# enter points
# when point = 0
points = float('1')

Sales_Price = float('400000')

Down_Payment =  float('20')
Loan_Amount = Sales_Price*(1-Down_Payment/100)
Mortgage_Type =  float('30')
Loan_Term = int(12*Mortgage_Type)
Interest_Rate2 =  float(7.1*(1-0.25/100))

# calculate monthly interest rate 
r = (Interest_Rate2)/(12*100)
R = 1 +(Interest_Rate2)/(12*100)

# enter formular 
X = Loan_Amount * r * (1 + r)** Loan_Term / ((1 + r)** Loan_Term - 1)
    
second = []

for j in range(0, Loan_Term - 1):
    second2 = np.exp(j * rinv/12)
    pmt_second = X * second2
    second = np.append(second, pmt_second)


first =( Sales_Price*(Down_Payment/100) + points/1000 * Loan_Amount ) * np.exp(rinv * Loan_Term / 12)

FutureValue2 = first + np.sum(second)

print("d2. future value purchasing one point is" + str('$') + str(np.round(FutureValue2,2)))

differene = str(np.round(FutureValue - FutureValue2,2))

print("d3. the future value of the total cost dropped when you purchase the point on the mortgage " + str('$') + str(differene))

    
