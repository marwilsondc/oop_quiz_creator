#import time
import time

#define add_question(string: str, code: int): 
def add_question(string: str, code: int):
    with open("questions.txt", "a") as file:
        file.write(f"<{bin(code)}> <question>:{string}")
        file.close()

#define add_choices(string: str, code: int):
def add_choices(string: str, code:int):
    with open("questions.txt", "a") as file:
        file.write(f"<{bin(code)}> <choice>:{string}")
        file.close()

#define add_correct(string: str, code: int):
def add_correct(string: str, code: int):
    with open("questions.txt", "a") as file:
        file.write(f"<{bin(code)}> <correct>:{string}")
        file.close()

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
    print("questions.txt is already exists")

