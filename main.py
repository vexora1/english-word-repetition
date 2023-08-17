import json
import random
import os
import time

word_list = []
word_dict = {}

def clear():
    os.system('cls')

def add_word():
    clear()
    print("Add a new word to the dictionary")
    word = input("Word: ")
    if word in word_list:
        print("Word already exists, do you want to add another meaning? (y/n): ")
        choice = input("Choice: ")
        if choice == "y":
            meaning = input("Meaning: ")
            word_dict[word] += f", {meaning}"
            with open("data.json", "w") as file:
                json.dump(word_dict, file, indent=4)
            print("Word added successfully")
            return
        elif choice == "n":
            return
    meaning = input("Meaning: ")
    word_dict[word] = meaning
    with open("data.json", "w") as file:
        json.dump(word_dict, file, indent=4)
    while True:
        choice = input("Do you want to add another meaning? (y/n): ")
        if choice == "y":
            meaning = input("Meaning: ")
            word_dict[word] += f", {meaning}"
            with open("data.json", "w") as file:
                json.dump(word_dict, file, indent=4)
        elif choice == "n":
            break
        else:
            print("Invalid choice")
    print("Word added successfully")
    
def get_word():
    clear()
    word = random.choice(word_list)
    print(f"What is the meaning of {word}")
    meaning = input("Meaning: ")
    if ", " in word_dict[word]:
        meanings = word_dict[word].split(", ")
        if meaning in meanings:
            print("Correct! The word has multiple meanings. The meanings are:\n" + word_dict[word])
        else:
            print(f"Wrong! The correct answer is {word_dict[word]}")
    else:
        if meaning == word_dict[word]:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {word_dict[word]}")
def main():
    global word_list
    global word_dict
    
    with open("data.json", "r") as file:
        if os.stat("data.json").st_size == 0:
            with open("data.json", "w") as file:
                json.dump({}, file, indent=4)
    with open("data.json", "r") as file:
        word_dict = json.load(file)
    word_list = list(word_dict.keys())
    while True:
        clear()
        print("Welcome to the English Word App")
        print("1. Add a new word")
        print("2. Get a word")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_word()
            time.sleep(2)
        elif choice == "2":
            get_word()
            time.sleep(10)
        elif choice == "3":
            break
        else:
            print("Invalid choice")
            time.sleep(2)
            
if __name__ == "__main__":
    main()