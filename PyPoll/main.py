from ast import If
import os
import csv
import sys
from tkinter import N
#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))
file=os.getcwd() # Current working directory name is stored in variable file
# Optional: print the current working directory
#print("This program is running from: " + os.getcwd())
#-----------------------------------------------------
pypoll_csv=os.path.join(file,"Resources/election_data.csv") # Sets the path variable to get the location of csv file by using join 
with open(pypoll_csv,'r') as csv_file:                  # opening csv file in read mode using the path variable
     csv_reader= csv.reader(csv_file,delimiter=",")      # csv reader variable declaration
     csv_header=next(csv_file)                           #sv_header variable declaration
     rows=[]                                      #Declaration of lists and varaibles that will be used in the program
     total_rows=0  
     col=[]
     uniqval=''                                     # This variable holds the name of unique variable the contestant
     county=[]                                        #this list holds the list of County in the given data
     names=[]
     uniqcounty=''
     count=0
     votecount=[]
     total_votes=0
     list=[]


     def countvotes(list, x,votes):          # Defining function to count the total votes by taking list , contestant name and total votes casted
      count = 0
      local=0
      percent=0
      for ele in list:                   #This loop counts the total votes casted for each contestant
        if (ele == x):
            count = count + 1
      percent= (count/votes)*100         # Counts the total percentage of votes for each contestant
      print("Total votes for "+ str(x) +" : "+str(round(percent,3))+ "%"+" ("+ str(count)+")") # Command to print the total votes for each contestant
      return(count)                        # countvotes is returning the count value to the variable where the function is called
      
     for row in csv_reader:
      #if uniqcounty!=row[1]:              optional code if name of county needs to be captured
       #county.append(row[1])
      list.append(row[2])                # This list holds the data of all votes casted for each contestant
      if uniqval==row[2]:         
        count=count+1
      
      if uniqval!=row[2]:              # This if loops adds unique contestant values the list named col
        if row[2] not in col:
         col.append(row[2]) 
      total_rows=total_rows+1            # total_rows count the total number of votes casted in the election
      #uniqcounty=row[1]
      uniqval=row[2] 

      #This section prints the output in the terminal in the desired format
     print("Election results") 
     print("----------------------------------------------------------------")
     print("Total votes: " + str(total_rows))
     print("----------------------------------------------------------------")
     result=0
     for i in col: 
      count=countvotes(list,i,total_rows)  
      if(result<count):                                                        # comparing the votes for each contestant and announing  the winner with highest votes
        result=count
        winner=i
     print("----------------------------------------------------------------")
     print("Winner is: "+ winner)
     print("----------------------------------------------------------------")
      
#   This section writes the output in a text file stored in the Analysis folder
     sys.stdout = open("Analysis/test.txt", "w")
     print("Election results") 
     print("----------------------------------------------------------------")
     print("Total votes: " + str(total_rows))
     print("----------------------------------------------------------------")
     result=0
     for i in col: 
      count=countvotes(list,i,total_rows)  
      if(result<count):
        result=count
        winner=i
     print("----------------------------------------------------------------")  # comparing the votes for each contestant and announing  the winner with highest votes
     print("Winner is: "+ winner)
     print("----------------------------------------------------------------")
     sys.stdout.close()  
     
    


