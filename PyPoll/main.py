from ast import If
import os
import csv
import sys
from tkinter import N
#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))
file1=os.getcwd() # Current working directory name is stored in variable file
# Optional: print the current working directory
#print("This program is running from: " + os.getcwd())
#print(file1)
#-----------------------------------------------------
pypoll_csv=os.path.join("C:/Users/archa/OneDrive/Desktop/homework/Python_challenge/PyPoll/Resources", "election_data.csv")
#print(pybank_csv)
with open(pypoll_csv,'r') as csv_file:
     csv_reader= csv.reader(csv_file,delimiter=",")
     csv_header=next(csv_file)
     #print(f"Reader:{csv_reader}")
     #print(f"Header:{csv_header}")
     rows=[]
     total_rows=0
     col=[]
     uniqval=''
     avg_change=[]
     avg_changeval=0
     change=0
     total_profitloss=0
    
     val0=0
     val1=0
     for row in csv_reader:
      val1=row[1]
      rows.append(row)
      if total_rows==0:
       col.append(row[2])
      if total_rows>=1:
        if uniqval!=row[2]:
          
             col.append(row[2])
         
      total_rows=total_rows+1
      uniqval=row[2]
      #avg_changeval=avg_changeval+int(change)
      #print(col)
      #total_profitloss=total_profitloss
     
     
      
     avg_changeval=round(avg_changeval/(total_rows-1),2)
      #print(avg_change)
     print("Election results") 
     print("----------------------------------------------------------------")
     print("Total votes: " + str(total_rows))
     print(col)
    # print("Total Profit/Loss: $"+ str(total_profitloss))
    # print("Average change: $"+ str(avg_changeval))
    # print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
    # print("Greatest Derease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")

     sys.stdout = open("Analysis/test.txt", "w")
     print("Election results") 
     print("----------------------------------------------------------------")
     print("Total votes: " + str(total_rows))
     #print("Total Profit/Loss: $"+ str(total_profitloss))
     #print("Average change: $"+ str(avg_changeval))
     #print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
     #print("Greatest Derease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")
     sys.stdout.close()  
     
    


