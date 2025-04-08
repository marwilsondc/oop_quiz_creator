#import time
import time

#initialize new_line
new_line = "\n"

#define add_question(string: str, code: int): 
def add_question(string: str, code: int):
    with open("questions.txt", "a") as file:
        file.write(f"{new_line}<{code:b}> <question>:{string}{new_line}")
        file.close()

#define add_choices(string: str, code: int):
def add_choices(string: str, code:int):
    with open("questions.txt", "a") as file:
        file.write(f"<{code:b}> <choice>:{string}{new_line}")
        file.close()

#define add_correct(string: str, code: int):
def add_correct(string: str, code: int):
    with open("questions.txt", "a") as file:
        file.write(f"<{code:b}> <correct>:{string}{new_line}")
        file.close()

#define ques_count() -> int:
def ques_count() -> int:
    with open("questions.txt", "r") as file:
        content = file.read()
        return content.count("<question>")

#define find_question(code: int):
def find_question(code: int):
    with open("questions.txt", "r") as file:
        content = file.read()
        return content.find(f"{bin(code)} <question>")

#create the file 
try:
    with open("questions.txt", "x") as file: 
        file.write(f"File created at: {time.asctime()}")
        file.close()

except FileExistsError:
    print("questions.txt is already created")

#while loop to continue asking user for input until ended
while True:
    local_count = ques_count()

    print(f"""Welcome to Quiz Creator! 

Main Menu:

Questions added: {local_count} 
[1] Add Question Set
[2] Quit""")
    
    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 3:
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

    elif user_select == "2":
        break