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
except FileExistsError:
    print("Directory " , project_name ,  " already exists")


# Moving inside the Main Project Folder
os.chdir(project_name)

# Now creating Sub folder
os.mkdir("app")
os.mkdir("migrations")
os.mkdir("tests")

# Now creating the files
os.system("pip3 freeze >> requirements.txt")
os.system("touch config.py")
os.system(f"touch {project_name}.py")

# Now moving inside app
os.chdir("app")

os.mkdir("templates")
os.mkdir("static")
os.mkdir("main")

# Now creating the files
os.system("touch __init__.py")
os.system("touch models.py")

# Moving inside main 
os.chdir("main")

# Now creating the files
os.system("touch __init__.py")
os.system("touch errors.py")
os.system("touch views.py")

os.chdir("..")
os.chdir("..")

# Moving inside tests
os.chdir("tests")

# Now creating the files
os.system("touch __init__.py")
os.system("touch test*.py")

print("Flask project Structure Ready")

