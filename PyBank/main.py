from ast import If
import os
import csv
import sys
#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))
file1=os.getcwd() # Current working directory name is stored in variable file
# Optional: print the current working directory
#print("This program is running from: " + os.getcwd())
#print(file1)
#-----------------------------------------------------
pybank_csv=os.path.join("C:/Users/archa/OneDrive/Desktop/homework/Python_challenge/PyBank/Resources", "budget_data.csv")
#print(pybank_csv)
with open(pybank_csv,'r') as csv_file:
     csv_reader= csv.reader(csv_file,delimiter=",")
     csv_header=next(csv_file)
     #print(f"Reader:{csv_reader}")
     #print(f"Header:{csv_header}")
     rows=[]
     total_rows=0
     col=[]
     avg_change=[]
     avg_changeval=0
     change=0
     total_profitloss=0
     incprofit=0
     decprofit=0
     val0=0
     val1=0
     for row in csv_reader:
      val1=row[1]
      rows.append(row)
      col.append(row[1])
      if total_rows>=1:
       change= int(val1)-int(val0)
       avg_change.append(change)
       if(change>0):
          if(incprofit<change):
           incprofit=change
           incdate=row[0]
          
       else:
          if(decprofit>change):
           decprofit=change
           decdate=row[0]
          
      total_rows=total_rows+1
      val0=row[1]
      avg_changeval=avg_changeval+int(change)
      #print(col)
      #total_profitloss=total_profitloss
     
     for i in col:
      #print(i)
      total_profitloss=total_profitloss+int(i)
      
     avg_changeval=round(avg_changeval/(total_rows-1),2)
      #print(avg_change)
     print("Financial Analysis") 
     print("----------------------------------------------------------------")
     print("Total months: " + str(total_rows))
     print("Total Profit/Loss: $"+ str(total_profitloss))
     print("Average change: $"+ str(avg_changeval))
     print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
     print("Greatest Derease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")

     sys.stdout = open("Analysis/test.txt", "w")
     print("Financial Analysis") 
     print("----------------------------------------------------------------")
     print("Total months: " + str(total_rows))
     print("Total Profit/Loss: $"+ str(total_profitloss))
     print("Average change: $"+ str(avg_changeval))
     print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
     print("Greatest Derease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")
     sys.stdout.close()  
     
    


