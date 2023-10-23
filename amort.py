import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tabulate import tabulate

def main():
    #inputs
    p = int(input("Principle: "))
    i = int(input("Rate: "))
    n = int(input("Length in years: "))
    
    #Constants for testing
    #p = 500000
    #i = 8
    #n = 30
    
    #Run the functions, convert years to months and interest to a non percentage
    n = time_convert(n)
    i = interest_annual_to_monthly_convert(interest_percentage_convert(i))
    
    #Do the amortization, print a table, and display a graph
    payments = amort(p, i, n)
    
    df = create_chart(payments)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

    
def amort(p, i ,n):
    payments = []
    while n > 0 :
        a = total_monthly_amount(p,i,n)
        
        b =calculate_monthly_interest(p,i)
        
        p = p - (a - b)
                 
        payments.append({'Month' : n,
            'Payment' : a,
            'Principle' : (a-b),
            'Interest' : b,
            'Balance' : p })
        
        n = n - 1
        
    return payments
          
    
def create_chart(payments):
    df= pd.DataFrame(payments)
        
    sns.lineplot(data=df['Balance'], color='g').set_title("Amortization Table")
    ax2 = plt.twinx()
    sns.lineplot(data=df['Principle'], ax = ax2, color='b') 
    sns.lineplot(data=df['Interest'], ax = ax2, color='r') 
    plt.show()   
    return df  

def interest_percentage_convert(i):
    i = float((i / 100)) #convert percentage to a decimal
    return i

def interest_annual_to_monthly_convert(i):
    i = ((1 + i)**(1 / 12)) - 1
    return i

def time_convert(n):
    return n * 12 #convert years to months

def total_monthly_amount(p, i, n):
      a = (p * i) * ((1 + i)**n) / (((1 + i)**n) - 1)
      return round(a, 2)
  
def calculate_monthly_interest(p, i):
    a = p * i
    return round(a, 2)  
  
if __name__ == "__main__":
    main()