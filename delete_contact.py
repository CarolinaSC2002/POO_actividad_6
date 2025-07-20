# delete_contact.py
import sys
import os

def delete_contact(input_name):
    file_path = "friendsContact.txt"
    temp_path = "temp.txt"

    if not os.path.exists(file_path):
        open(file_path, "w").close()

    found = False

    with open(file_path, "r") as rf, open(temp_path, "w") as wf:
        for line in rf:
            if "!" not in line:
                continue
            name, number = line.strip().split("!")
            if name == input_name:
                found = True
                continue
            wf.write(line)

    if found:
        os.replace(temp_path, file_path)
        print("Friend deleted.")
    else:
        os.remove(temp_path)
        print("Input name does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_contact.py <name>")
    else:
        delete_contact(sys.argv[1])
