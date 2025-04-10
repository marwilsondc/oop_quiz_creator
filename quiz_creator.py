#import time and os.path
#time is to record dates of file creation within files, while pathlib is for easy file handling 
import time
from pathlib import Path

#initialize new_line, and file_path and create file
#file_path contains "questions.txt" as default
#program attempts to create the file every time it opens, it will do nothing if file already exists
new_line = "\n"
file_path = Path("~", "Documents", "questions.txt").expanduser()
file_path.parent.mkdir(exist_ok = True, parents = True)

#define add_question(string: str, code: int):
#to add questions, contains specific formatting for questions, this function also categorizes its input as such.
def add_question(string: str, code: int):
    with open(file_path, "a") as file:
        file.write(f"{new_line}<{code:b}> <question>:{string}{new_line}")
        file.close()

#define add_choices(string: str, code: int):
#to add choices, specific formatting for choices, categorizes written input as such
def add_choices(string: str, code:int):
    with open(file_path, "a") as file:
        file.write(f"<{code:b}> <choice>:{string}{new_line}")
        file.close()

#define add_correct(string: str, code: int):
#to add correct answers to the file, same formatting with choices, but categorizes it as <correct>
def add_correct(string: str, code: int):
    with open(file_path, "a") as file:
        file.write(f"<{code:b}> <correct>:{string}{new_line}")
        file.close()

#define change_path(new_file: str = "questions.txt"):
#this function modifies the global variable, file_path, into the user input 
#function creates the file if it does not exist, also initializing date of creation within the file
#If no input was given, function will use default parameter
def change_path(new_file: str):
    global file_path
    file_path = Path("~", "Documents", new_file + ".txt").expanduser()
    file_path.parent.mkdir(exist_ok = True, parents = True)

    try:
        with open(file_path, "x") as file:
            file.write(f"File created at: {time.asctime()}")
        file.close()
        print(f"File is stored at {Path(file.name)}")

    except FileExistsError:
        with open(file_path, "r") as file:
            print(f"File is stored at {Path(file.name)}")

#define ques_count() -> int:
#this function is used to count the questions within the selected file
#used in the main menu to give user quick info about the file contents5
def ques_count() -> int:
    with open(file_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    file.close()

#define current_dir() -> str:
#this function is used to return the current file directory, to be called out within the while loop
def current_dir() -> str:
    with open(file_path, "r") as file:
        return Path(file.name)

#define edit_content(filename: str, line_num: int, text: str):
#this function converts the file into a list of its lines and changes specific line contents through indexing
#then the function rewrites the whole file again. This method may cause issues with bigger files but works fine with smaller files
def edit_content(line_num: int, text: str):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    bin_code = lines[line_num].split(":")
    bin_code = bin_code[0]

    if line_num <= len(lines):
        if "<question>" in bin_code:
            lines[line_num] = f"{bin_code}:{text}{new_line}"
        
        elif "<choice>" in bin_code or "<correct>" in bin_code:
            lines[line_num] = f"{bin_code}:{text}{new_line}"

        with open(file_path, "w") as file:
            for line in lines:
                file.write(line)
    
    else: 
        print("Line", line_num, "not in file.")
        print("File has", len(lines), "lines.")
    
    file.close()

#def clear_contents():
#this function opens the file and overwrites the whole thing with an initialization of date of creation
def clear_contents():
    with open(file_path, "w") as file:
        file.write(f"File cleared at: {time.asctime()}")
        file.close()

#create the file, startup for the program
try:
    with open(file_path, "x") as file:
        file.write(f"File created at: {time.asctime()}")
        file.close()
    print(f"File is stored at {Path(file.name)}")

#if file is already created, echo the file directory
except FileExistsError:
    print("questions.txt is already created")
    with open(file_path, "r") as file:
        print(f"File is stored at {Path(file.name)}")

#while loop to continue asking user for input until ended
while True:
    local_count = ques_count()
    local_path_var = current_dir()

    #Main menu for the program, where the user will select from options
    print(f"""Welcome to Quiz Creator! 

Main Menu:
          
File opened: {local_path_var}

Questions added: {local_count} 
[1] Add Question Set
[2] View File Contents
[3] Edit File Contents
[4] Clear File Contents
[5] Change File Directory
[6] Quit""")
    
    #A while loop to continue usage for the user until they quit the program
    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 7:
            break
        else:
            continue

    #This option is for creating question sets, utilizing local_count, add_question, add_choices, and add_correct.
    #This option records question count to correctly format the binary code and the specific functions handle input categorization
    #Inputs to the file are also separated by a colon, separating the formatting and the actual user inputs
    if user_select == "1":
        user_input = input("Input the question you want to add: ")
        add_question(user_input, local_count + 1)
        local_count = ques_count()
        for i in range(0, 4):
            user_input = input("Input the choices that you want to add to your question: ")
            add_choices(user_input, local_count)
        user_input = input("Input the correct answer from your choices in the question: ")
        add_correct(user_input, local_count)
        print("New question added!")
        continue

    #This option lets the user view the whole contents of the file, also including the line numbers for each line
    #The line numbers in this option's output starts from 0. These line numbers are to be utilized by the user when editing the file
    #This option initializes line_count = 0, opens the file, and uses a for loop to iterate through the lines of the file then prints line number and line itself
    elif user_select == "2":
        line_count = 0
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"<line {line_count}>: {line}")
                line_count += 1
        continue
    
    #This option lets the user edit the file contents; asking the user what line number they want to edit and what to replace the line with
    #This option stores the user input into variables and puts them to the parameters of edit_content()
    elif user_select == "3":
        print("Before trying to edit a file, it is advised that the user should view file contents first. "
        "\nThis is to let the user know about the line number to input in editing the file")

        while True:
            user_input = input("Input the line number to edit: ")
            if user_input.isnumeric():
                user_input = int(user_input)
                break
            else: 
                continue
        
        user_edit = input("Input the text to replace current line: ")

        edit_content(user_input, user_edit)
        print("Done!")

    #This option clears the contents of the file after being given the permission by the user
    #Uses clear_contents() if user answers yes while it breaks the while loop if they answer no
    elif user_select == "4":
        while True:
            user_input = input("This will clear the file's contents. Are you sure? [y/n]: ")
            
            if user_input == "y":
                clear_contents()
                print("Cleared file contents!")
                break

            elif user_input == "n":
                print("Okay!")
                break
            
            else:
                continue

        continue

    #This option allows the user to change the file that the program will access, storing the file in ../Documents
    #Before proceeding to change the directory, the program first validates the user input. If input is not valid, program asks again.
    #if user_input is none, the program will go back to questions.txt
    elif user_select == "5":
        print("This changes the directory that this program will access. If the file does not exist, it will create it.")

        while True:
            user_input = input("Input the new file to access, no need for \'.txt\' (stored at ../Documents): ")
            valid_flag = True
            for i in user_input:
                if i.isspace():
                    print("Filename cannot contain spaces, try again")
                    valid_flag = False
                    break
                elif i.isalnum() or i in ["-","_"]:
                    valid_flag = True
                    continue
                else: 
                    print("Filename cannot contain symbols other than \'-\' or \'_\'")
                    valid_flag = False
                    break
            
            if valid_flag:
                break
            else:
                continue
        
        if user_input == "":
            user_input = "questions"

        change_path(user_input)

    #This option breaks the whole while loop and ends the program
    elif user_select == "6":
        print("Goodbye!")
        break
