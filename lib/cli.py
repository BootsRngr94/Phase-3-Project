# lib/cli.py
from helpers import (
    exit_program,
    add_game,
    delete_game,
    display_games,
    find_by_title
)


def main():
    while True:
        menu()
        choice = input("> ")
        
        if choice == '1':
            title = input("Enter game title: ")
            genre_name = input("Enter genre name: ")
            platform_name = input("Enter platform name: ")
            add_game(title, genre_name, platform_name)


        elif choice == '2':
            title = input("Enter title of the game you want to delete: ")
            delete_game(title)


        elif choice == '3':
            display_games()


        elif choice == '5':
            exit_program()
            exit()

        elif choice == "4":
            title = input("search by title:  ")
            find_by_title(title)


def menu():
        print("\nMenu:")
        print("1. Add Game")
        print("2. Delete Game")
        print("3. View All Games")
        print("4. Search Title")
        print("5. Exit")
     
   
if __name__ == "__main__":
    main()
