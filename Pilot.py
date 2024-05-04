import os
import shutil
import subprocess 
import datetime

  # Splits by whitespace by default

print("""Welcome to Pilot, a versatile command-line utility designed to streamline system management and development tasks with ease. From creating directories and files to managing packages and executing scripts, Pilot empowers users to efficiently navigate their computing environment. For command help, type the word 'help' """)

Name = input("Please enter your username to begin: ")

linux 

def pilot():

    tokens = text.split()
    
    if tokens[0] == "create":
        if tokens[1] == "directory":
            directory_name = tokens[2]
            if not os.path.exists(directory_name):
                os.mkdir(directory_name)
                print(f"Directory '{directory_name}' created successfully.")
            else:
                print(f"Directory '{directory_name}' already exists.")
                
        elif tokens[1] == "file":
            file_name = tokens[2]
            if not os.path.exists(file_name):
                with open(file_name, 'w'):
                    pass  # Do nothing, effectively creating an empty file
                print(f"File '{file_name}' created successfully.")
            else:
                file_error = input("File already exists. Would you like to replace it? (y/n): ")
                if file_error.lower() == "y":
                    os.remove(file_name)
                    with open(file_name, 'w'):
                        pass  # Do nothing, effectively creating an empty file
                    print(f"File '{file_name}' replaced successfully.")
                elif file_error.lower() == "n":
                    print("Operation canceled.")
                else:
                    print("Invalid input. Operation canceled.")

    elif tokens[0] = "rename" or tokens[0] = "Rename":
        old_file_name = tokens[1]
        if tokens[2] == "to":
            new_file_name == tokens[3]
            os.rename(old_file_name, new_file_name)


        
    elif tokens[0] == "delete":
            if tokens[1] == "directory":
                Directory_path = tokens[2]
                if not os.path.exists(Directory_path):
                    print(f"Directory '{Directory_path}' does not exist.")
                else:
                    os.rmdir(Directory_path)
            if tokens[1] == "file":
                file = tokens[2]
                if not os.path.exists(file):
                    print("file does not exist")
                else:
                    os.remove(file)
                    if os.path.exists(file):
                        print("An error has occured")
                    else:
                        print("file has been deleted") 

    elif text == "time" or text =="Time":
        
        current_time = datetime.datetime.now()
    
        print(current_time) 

    elif tokens[0] == "exit" or tokens[0] == "Exit":
        print("successfully exited")
        exit()

    elif tokens[0] == "Say" or tokens[0] == "say":
        print(" ".join(tokens[1:]))

    elif tokens[0] == "move" or tokens[0] == "Move":
        if tokens[2] == "to":
            file_name = tokens[1]
            file_destination = tokens[3]
            shutil.move(file_name, file_destination)
            print(f"{file_name} has been moved to {file_destination}")
        



    

    elif tokens[0] == "packager":
        if tokens[1] == "install":
            package_name = tokens[2]
            subprocess.run(["sudo", "apt", "install", package_name])
        if tokens[1] == "delete":
            subprocess.run(["sudo", "apt", "remove", package_name])
        if tokens[1] == "autodelete":
            subprocess.run(["sudo", "apt", "autoremove"])
        if tokens[1] == "-get":
            rest_of_command = " ".join(tokens[1:])
            subprocess.run(["sudo", "apt-get", rest_of_command])
        if tokens[1] == "run":
            rest_of_command = " ".join(tokens[2:])
            subprocess.run(rest_of_command, shell=True)

    elif "+" in text or "*" in text or "-" in text or "/" in text:
        anws = eval(text)
        print(anws)

            

    elif tokens[0] == "python3" and len(tokens) > 2:
        if tokens[1] == "run":
            python_file = tokens[2]
            subprocess.run(["python3", python_file])

    elif tokens[0] == "python3" and len(tokens) < 2:
        subprocess.run(["python3"])

    elif tokens[0] == "pip":
        package_name = tokens[2]
        if tokens[1] == "show":
            subprocess.run(["pip", "show", package_name])
        if tokens[1] == "install":
            subprocess.run(["pip", "install", package_name])
        
    elif tokens[0] == "compile":
        input_file = tokens[1]
        if tokens[1] == ",":
            output_file = tokens[2]
            subprocess.run(["gcc", input_file, "-o", output_file])


    elif tokens[0] == "help":
        print("""Command-Line Tool Documentation:
        
        create directory <directory_name>:
            Create a new directory with the specified name.
        
        create file <file_name>:
            Create a new file with the specified name.
        
        delete directory <directory_path>:
            Delete the directory at the specified path.
        
        delete file <file_path>:
            Delete the file at the specified path.
        
        exit:
            Exit the program.
        
        Say <message>:
            Print a message to the console.
        
        move <file_name> to <destination>:
            Move a file to the specified destination.
        
        packager install <package_name>:
            Install the specified package using the system package manager.
        
        packager delete <package_name>:
            Delete the specified package using the system package manager.
        
        packager autodelete:
            Automatically remove unused packages using the system package manager.
        
        packager -get <function>:
            Use the apt-get command with the specified function.
        
        python3 run <python_file>:
            Run the specified Python script.
        
        pip show <package_name>:
            Display information about the specified Python package.
        
        pip install <package_name>:
            Install the specified Python package.
        
        compile <input_file> <output_file>:
            Compile the specified C file into an executable.""")

    else: 
        print("command is not accepted")
        
for i in range (1000000): 
    text = input(f"{Name}> ")
    pilot()