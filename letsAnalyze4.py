def main():
    games = []  

    while True:
        print("\n1. Add Element")
        print("2. Display Element")
        print("3. Delete Element")
        print("4. Exit")
        
        option = input("Option: ")

        if option == '1':
            new_game = input("Enter the name of the game to add: ")
            games.append(new_game)
            print(f"{new_game} has been added to the list.")
        
        elif option == '2':
            if not games:
                print("No games in the list.")
            else:
                print("List of games:")
                for i, game in enumerate(games, start=1):
                    print(f"{i}. {game}")
        
        elif option == '3':
            if not games:
                print("No games in the list to delete.")
            else:
                print("List of games:")
                for i, game in enumerate(games, start=1):
                    print(f"{i}. {game}")
                index = int(input("Enter the number of the game to delete: ")) - 1
                if 0 <= index < len(games):
                    deleted_game = games.pop(index)
                    print(f"{deleted_game} has been deleted from the list.")
                else:
                    print("Invalid index.")
        
        elif option == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()