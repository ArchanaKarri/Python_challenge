from ast import If
import os
import csv
import sys
#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))
file=os.getcwd() # Current working directory name is stored in variable file
#-----------------------------------------------------
pybank_csv=os.path.join(file,"Resources/budget_data.csv") # Setting path variable to the location where the csv file is stored

with open(pybank_csv,'r') as csv_file: #Opening the csv file in reading mode using the stored path variable
     csv_reader= csv.reader(csv_file,delimiter=",") # Reading the csv file and setting the delimiter as ","
     csv_header=next(csv_file) # Retrieving the Csv header information from the Csv file
  
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
     for row in csv_reader: # reading the csv_file into row 
      val1=row[1]      # val1 holds the data in 2nd column of the csv file
      col.append(row[1]) # list COL holds the data in column 2
      if total_rows>=1: #This if condition calculates the differnece of  2 conseccutive columns for the whole data given
       change= int(val1)-int(val0)
       avg_change.append(change)  # the difference calculated is stored in the avg_change list
       if(change>0):            # this if compares  the change and if the change is more than the previous one, then increased profit data is stored
          if(incprofit<change): # Subsequent date value will be stored in the incdate variable
           incprofit=change
           incdate=row[0]
          
       else:                    #this if compares  the change and if the change is less than the previous one, then decreased profit data is stored
          if(decprofit>change):
           decprofit=change
           decdate=row[0]        # Subsequent date value will be stored in the decdate variable
          
      total_rows=total_rows+1  # counts the total rows by incrementing by 1 each time the for loop is executed
      val0=row[1]               # val0 stores the value of profit/Loss for comparing with the next row data
      avg_changeval=avg_changeval+int(change) # avg_changeval is calcualting the total for all the data
      
     
     for i in col:
         total_profitloss=total_profitloss+int(i)   # for all data in col, total_profitloss is calculating the total
      
     avg_changeval=round(avg_changeval/(total_rows-1),2)   # calculating the mean change for the given data
     # this section prints the oputput in the terminal in the desired format
     print("Financial Analysis") 
     print("----------------------------------------------------------------")
     print("Total months: " + str(total_rows))
     print("Total Profit/Loss: $"+ str(total_profitloss))
     print("Average change: $"+ str(avg_changeval))
     print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
     print("Greatest Decrease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")
     
      # this section writes the oputput in a text file which is in the Analysis folder
     sys.stdout = open("Analysis/test.txt", "w")
     print("Financial Analysis") 
     print("----------------------------------------------------------------")
     print("Total months: " + str(total_rows))
     print("Total Profit/Loss: $"+ str(total_profitloss))
     print("Average change: $"+ str(avg_changeval))
     print("Greatest Increase in profits:"+ str(incdate) + " ($" +str(incprofit)+")")
     print("Greatest Decrease in profits:"+ str(decdate) + " ($" +str(decprofit)+ ")")
     sys.stdout.close()  
     
    


