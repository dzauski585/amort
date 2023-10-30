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
    
    df = pd.DataFrame(payments) #make a dataframe from the amortization table to utilzie pandas functions
    
    create_excel(df)
    
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    
    create_chart(df)
    
    extra_payments = extra_amort(p,i,n)
    extradf = pd.DataFrame(extra_payments)
    print(tabulate(extradf, headers = 'keys', tablefmt = 'psql'))
    #create_excel(extradf) # make new excel file if needed
    
def amort(p, i ,n):
    payments = []
    while n > 0 :
        a = total_monthly_amount(p,i,n)
        
        b = calculate_monthly_interest(p,i)
        
        p = p - (a - b)
                 
        payments.append({'Month' : n,
            'Payment' : a,
            'Principle' : (a-b),
            'Interest' : b,
            'Balance' : p })
        
        n = n - 1
        
    return payments

def extra_amort(p, i ,n): #function for adding extra payments
    extra_payments = []
    e = 2500 #extra payment amount change as needed
    
    while p > 0 :
        a = total_monthly_amount(p,i,n)
                
        b = calculate_monthly_interest(p,i)
                
        p = p - (a - b) - e
                        
        extra_payments.append({'Month' : n,
            'Payment' : a,
            'extra' : e, 
            'Principle' : (a-b),
            'Interest' : b,
            'Balance' : p })
                
        n = n - 1
        
    return extra_payments
 
def create_chart(df): # function for the graph
    sns.lineplot(data=df['Balance'], color='g').set_title("Amortization Table") #line one
    ax2 = plt.twinx()
    sns.lineplot(data=df['Principle'], ax = ax2, color='b') #line two ax changes the type of plot allowed in seabord to matplotlib multi graphs 
    sns.lineplot(data=df['Interest'], ax = ax2, color='r')  #line three
    plt.show()    

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

def create_excel(df): #takes the dateframe and makes it into excel file with pandas
    # Create a DataFrame from the loan schedule
    df = pd.DataFrame(df)

    # Export DataFrame to Excel
    output_file = 'loan_schedule.xlsx'
    df.to_excel(output_file, index=False)

  
if __name__ == "__main__":
    main()