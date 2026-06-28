import pyperclip
import os

FILE = "passwords.txt"

def add_password():
    site = input("Website/App name: ")
    username = input("Username/Email: ")
    password = input("Password: ")
    
    with open(FILE, "a") as f:
        f.write(f"Site: {site} | Username: {username} | Password: {password}\n")
    print(f"✅ '{site}' ka password save ho gaya!")

def view_passwords():
    if not os.path.exists(FILE):
        print("❌ Koi password saved nahi hai abhi.")
        return
    print("\n📋 Saved Passwords:")
    print("-" * 40)
    with open(FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        print("❌ Koi password saved nahi hai abhi.")
        return
    for line in lines:
        print(line.strip())
    print("-" * 40)

def main():
    while True:
        print("\n🔐 PASSWORD MANAGER")
        print("1. Password Add karo")
        print("2. Passwords Dekho")
        print("3. Exit")
        
        choice = input("Choice (1/2/3): ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Bye! 👋")
            break
        else:
            print("❌ Galat choice, dobara try karo!")

main()