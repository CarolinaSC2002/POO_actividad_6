# create_contact.py
import sys
import os

def create_contact(new_name, new_number):
    file_path = "friendsContact.txt"

    if not os.path.exists(file_path):
        open(file_path, "w").close()

    found = False

    with open(file_path, "r+") as f:
        lines = f.readlines()
        for line in lines:
            if "!" not in line:
                continue
            name, number = line.strip().split("!")
            if name == new_name or number == new_number:
                found = True
                break

        if not found:
            f.write(f"{new_name}!{new_number}\n")
            print("Friend added.")
        else:
            print("Input name or number already exists.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_contact.py <name> <number>")
    else:
        create_contact(sys.argv[1], sys.argv[2])
