# update_contact.py
import sys
import os

def update_contact(input_name, new_number):
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
                wf.write(f"{name}!{new_number}\n")
                found = True
            else:
                wf.write(line)

    if found:
        os.replace(temp_path, file_path)
        print("Friend updated.")
    else:
        os.remove(temp_path)
        print("Input name does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_contact.py <name> <new_number>")
    else:
        update_contact(sys.argv[1], sys.argv[2])
