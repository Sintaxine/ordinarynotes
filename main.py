import os
from functions import Functions

def create_and_write_note(check_if_exists: bool, note_name: str):

    if check_if_exists:
        Functions.create_file(note_name) 

    note = input("Enter the content for the note: ")
    Functions.write_note(note_name, note) 

    print(f"Done! Note saved as {note_name}")

def get_user_choice(prompt: str, valid_choices: set) -> str:

    while True:

        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice
        
        print("Invalid choice. Please enter a valid option.")

def main():

    note_name = Functions.get_file_name()

    if Functions.file_exists(note_name):
        edit_choice = get_user_choice(
            f"The file '{note_name}' already exists. Do you want to edit it or create a new one? (E/N): ",
            {"e", "n"}
        )
        if edit_choice == "e":
            Functions.edit_file(note_name)
            return
        
        print("Creating a new file.")
        create_and_write_note(False, note_name)

        return
    
    create_and_write_note(True, note_name)

if __name__ == "__main__":
    main()