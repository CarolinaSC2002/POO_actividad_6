# read_contacts.py
import os

def read_contacts():
    file_path = "friendsContact.txt"
    if not os.path.exists(file_path):
        open(file_path, "w").close()

    with open(file_path, "r") as f:
        for line in f:
            if "!" not in line:
                continue
            name, number = line.strip().split("!")
            print(f"Friend Name: {name}")
            print(f"Contact Number: {number}\n")

if __name__ == "__main__":
    read_contacts()
