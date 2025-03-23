import os
from input_messages import InputMessages

class Functions:

    DB_FOLDER = "db"

    def __init__(self):
        pass

    def file_exists(file_name: str) -> bool:
        file_path = os.path.join(Functions.DB_FOLDER, file_name)
        return os.path.exists(file_path)
    
    def get_file_name() -> str:

        name = input(InputMessages.note_name)

        while not name:
            name = input(InputMessages.empty_note_name)

        return name

    def create_file(file_name: str):
        
        file_path = os.path.join(Functions.DB_FOLDER, file_name)
        os.makedirs(Functions.DB_FOLDER, exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write("")
        else:
            print(f"The file '{file_name}' already exists.")

    def write_or_append_note(mode: str, file_name: str, content: str):

        file_path = os.path.join(Functions.DB_FOLDER, file_name)
        os.makedirs(Functions.DB_FOLDER, exist_ok=True)

        with open(file_path, mode) as file:
            file.write(content)

    def write_note(file_name: str, content: str):
        Functions.write_or_append_note('w', file_name, content)

    def append_note(file_name: str, content: str):
        Functions.write_or_append_note('a', file_name, content)

    def get_edited_content(prompt: str) -> str:

        content = []

        while True:
            line = input()
            if line.lower() == 'done':
                break
            content.append(line)

        return "\n".join(content) + "\n"

    def edit_file(file_name: str):

        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Current content of the file:\n{content}\n")

        choice = input(InputMessages.edit_file_choice).lower()

        actions = {
            'e': ("You can now edit the file. Type 'done' on a new line to finish.", Functions.write_note),
            'a': ("You can now append to the file. Type 'done' on a new line to finish.", Functions.append_note),
            'o': ("You can now overwrite the file. Type 'done' on a new line to finish.", Functions.write_note),
        }

        if choice in actions:
            prompt, action = actions[choice]
            edited_content = Functions.get_edited_content(prompt)
            action(file_name, edited_content)
        else:
            print("Invalid choice. Please select 'E', 'A', or 'O'.")