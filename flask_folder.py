import sys
import os

# Checking for Exception in case no Arguments are provided 
try:
    project_name = sys.argv[1]
except IndexError:
    project_name = input("Enter the name of the Flask Project: ")

# Now creating Main Project folder

try:
    # Create target Directory
    os.mkdir(project_name)
    print("Directory " , project_name ,  " Created ") 
except FileExistsError:
    print("Directory " , project_name ,  " already exists")

