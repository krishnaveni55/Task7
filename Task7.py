#1.the function will create a text file with the current timestamp,the file content should have the content of current timestamp
import datetime #Timestamp (a)
current_time = datetime.datetime.now()

file_name = current_time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

with open(file_name, "w") as file:
    file.write("This is a text file created at {}\n".format(current_time))
    file.write("You can write anything you want here.\n")
    file.write("This file will have a unique name based on the current timestamp.")
    
print("Text file '{}' has been created.".format(file_name))

import datetime
current_time = datetime.datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open("timestamp.txt", "w") as file:
    file.write(formatted_time)

print("Text file 'timestamp.txt' has been created with the content of the current timestamp.")
#2.write python function to lead from a textfile.display the content of the file into condole
def readfile(filename):
    path=f"C:\Users\HP\Desktop\create\\{filename}"
    f=open(path,"r")
    return(f.read())
filename=input("enter the file name")
readfile(filename)