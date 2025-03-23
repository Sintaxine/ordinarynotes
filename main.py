import os

def getFileName() -> str:
    name = input("Enter note name: ")
    while len(name) < 1:
        name = input("Enter note name (cannot be empty): ")  
    return name  

def createFile(file_name: str):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:  
            file.write("")
    else:
        print(f"The file '{file_name}' already exists.")

def writeNote(file_name: str, content: str):
    with open(file_name, 'w') as file:
        file.write(content) 

def appendNote(file_name: str, content: str):
    with open(file_name, 'a') as file:
        file.write(content)

def editFile(file_name: str):

    with open(file_name, 'r') as file:
        content = file.read()
    print(f"Current content of the file:\n{content}\n")

    choice = input("Do you want to (E)dit, (A)ppend, or (O)verwrite the file? (E/A/O): ").lower()
    if choice == 'e':
        print("You can now edit the file. Type 'done' on a new line to finish.")
        edited_content = ""
        while True:
            line = input()
            if line.lower() == 'done':
                break
            edited_content += line + '\n'
        writeNote(file_name, edited_content)  
    elif choice == 'a':
        print("You can now append to the file. Type 'done' on a new line to finish.")
        append_content = ""
        while True:
            line = input()
            if line.lower() == 'done':
                break
            append_content += line + '\n'
        appendNote(file_name, append_content)  
    elif choice == 'o':
        print("You can now overwrite the file. Type 'done' on a new line to finish.")
        overwrite_content = ""
        while True:
            line = input()
            if line.lower() == 'done':
                break
            overwrite_content += line + '\n'
        writeNote(file_name, overwrite_content)  
    else:
        print("Invalid choice. Please select 'E', 'A', or 'O'.")

def main():
    note_name = getFileName() 
    if os.path.exists(note_name):  
        edit_choice = input(f"The file '{note_name}' already exists. Do you want to (E)dit it or create a new one? (E/N): ").lower()
        if edit_choice == 'e':
            editFile(note_name)
        else:
            print("Creating a new file.")
            createFile(note_name)  
            note = input("Enter the content for the note: ")
            writeNote(note_name, note) 
            print(f"Done! Note saved as {note_name}")
    else:
        createFile(note_name)  
        note = input("Enter the content for the note: ")
        writeNote(note_name, note) 
        print(f"Done! Note saved as {note_name}")

if __name__ == "__main__":
    main()  
