#import time and os.path
import time
from pathlib import Path

#initialize new_line, and file_path and create file
new_line = "\n"
file_path = Path("~", "Documents", "questions.txt")
file_path.parent.mkdir(exist_ok = True, parents = True)

#define add_question(string: str, code: int): 
def add_question(string: str, code: int):
    with open(file_path, "a") as file:
        file.write(f"{new_line}<{code:b}> <question>:{string}{new_line}")
        file.close()

#define add_choices(string: str, code: int):
def add_choices(string: str, code:int):
    with open(file_path, "a") as file:
        file.write(f"<{code:b}> <choice>:{string}{new_line}")
        file.close()

#define add_correct(string: str, code: int):
def add_correct(string: str, code: int):
    with open(file_path, "a") as file:
        file.write(f"<{code:b}> <correct>:{string}{new_line}")
        file.close()

#define change_path(new_file: str = "questions.txt"):
def change_path(new_file: str = "questions"):
    global file_path
    file_path = Path("~", "Documents", new_file)
    file_path.parent.mkdir(exist_ok = True, parents = True)

    try:
        with open(file_path, "x") as file:
            file.write(f"File created at: {time.asctime()}")
        file.close()
        print(f"File is stored at {Path(file.name)}")

    except FileExistsError:
        print("questions.txt is already created")
        with open(file_path, "r") as file:
            print(f"File is stored at {Path(file.name)}")

#define ques_count() -> int:
def ques_count() -> int:
    with open(file_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    file.close()

#define edit_content(filename: str, line_num: int, text: str): 
def edit_content(line_num: int, text: str):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    bin_code = lines[line_num].split(":")
    bin_code = bin_code[0]

    if line_num <= len(lines):
        if "<question>" in bin_code:
            lines[line_num] = f"{new_line}{bin_code}:{text}{new_line}"
        
        elif "<choice>" in bin_code or "<correct>" in bin_code:
            lines[line_num] = f"{bin_code}:{text}{new_line}"

        with open(file_path, "w") as file:
            for line in lines:
                file.write(line)
    
    else: 
        print("Line", line_num, "not in file.")
        print("File has", len(lines), "lines.")
    
    file.close()

def clear_contents():
    with open(file_path, "w") as file:
        file.write(f"File cleared at: {time.asctime()}")
        file.close()

#create the file 
try:
    with open(file_path, "x") as file:
        file.write(f"File created at: {time.asctime()}")
        file.close()
    print(f"File is stored at {Path(file.name)}")

except FileExistsError:
    print("questions.txt is already created")
    with open(file_path, "r") as file:
        print(f"File is stored at {Path(file.name)}")

#while loop to continue asking user for input until ended
while True:
    local_count = ques_count()

    print(f"""Welcome to Quiz Creator! 

Main Menu:

Questions added: {local_count} 
[1] Add Question Set
[2] View File Contents
[3] Edit File Contents
[4] Clear File Contents
[5] Change File Directory
[6] Quit""")
    

    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 7:
            break
        else:
            continue

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

    elif user_select == "2":
        line_count = 0
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"<line {line_count}>: {line}")
                line_count += 1
        continue
    
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

    elif user_select == "5":
        print("This changes the directory that this program will access. If the file does not exist, it will create it.")

        while True:
            user_input = input("Input the new file to access, no need for \'.txt\' (stored at ~/Documents): ")
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

        user_input += ".txt"

        change_path(user_input)

    elif user_select == "6":
        print("Goodbye!")
        break
