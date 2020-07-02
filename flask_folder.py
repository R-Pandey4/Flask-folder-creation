import sys

# Checking for Exception in case no Arguments are provided 
try:
    project_name = sys.argv[1]
except:
    project_name = input("Enter the name of the Flask Project: ")

print(f"\n {project_name}")