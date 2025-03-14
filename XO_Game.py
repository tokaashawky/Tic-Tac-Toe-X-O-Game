import os

def clear_screen() :
    os.system("cls" if os.name == "nt" else "clear")

class Player : 
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def player_name(self) :
        while True :
            name = input("Enter your name : ")
            if name.isalpha() :
                self.name = name
                break
            print("\nInvalid name. Name must be letters only.")

    def player_symbol(self) :
        while True :
            symbol = input(f"{self.name} , Enter your symbol ( X or O ) : ")
            if symbol.lower() == 'x' or symbol.lower() == 'o' :
                self.symbol = symbol
                break
            print("\nInvalid symbol. It must be either x or o ( uppercase or lowercase ) only.")

class Menu :
    def display_main_menu(self) :
        print("\n############## Welcome to my X-O Game! ##############")
        print("\nMain Menu")
        print("===========")
        print("\n1. Start Game.")
        print("2. Quit Game.")
        choice = input("\nEnter your choice : ")
        return choice
    
    def display_endgame_menu(self) :
        menu_text = """\nGame Over! 
        \n1. Restart Game.   2. Quit Game.
        \nEnter your choice : """
        choice = input(menu_text)
        return choice

class Board :
    def __init__(self) :
        self.board = [str(i) for i in range(1 , 10) ]

    def display_board(self) :
        print()
        for i in range(0,9,3) :
            print("|".join(self.board[i:i+3]))
            if i < 6 :
                print("-"*5)

    def update_board( self , choice , symbol ) :
        if self.is_valid_move(choice) :
            self.board[choice-1] = symbol
            return True
        return False
    
    def is_valid_move(self , choice) :
        return self.board[choice-1].isdigit()
    
    def reset_board(self) :
        self.board = [str(i) for i in range(1 , 20) ]



class Game :
    def __init__(self) :
        self.players = [ Player() , Player() ]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self) :
        choice = self.menu.display_main_menu()
        if choice == '1' :
            self.setup_players()
            self.play_game()
        else :
            self.quit_game()

    def setup_players(self) :
        for number , player in enumerate(self.players , start = 1) :
            clear_screen()
            print(f"\nPlayer {number} , Please Enter your details : ")
            player.player_name()
            player.player_symbol()
            # clear_screen()

    def play_game(self) :
        while True :

            clear_screen()
            self.play_turn()
            winner = self.check_win()
            if winner:  
                print(f"\nCongratulations {winner}! You won the game! 🎉\n")
                 # Show menu in both cases
            if winner or self.check_draw(): 
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                elif choice == "2":
                    self.quit_game()
                    break
                else:
                    print("\nInvalid choice, try again.")

    def restart_game(self) :
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6] ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                for player in self.players:
                    if player.symbol == self.board.board[combo[0]]:
                        return player.name  
        return None  

    
    def check_draw(self) :
        return all( not cell.isdigit() for cell in self.board.board)

    def play_turn(self) :
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"\n{player.name}'s turn ( {player.symbol} )")
        while True :
            try :
                cell_choice = int(input("\nChoose a cell number ( 1-9 ) : "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice ,  player.symbol) :
                    break
                else :
                    print("\nInvalid move, Please try again!")
            except ValueError :
                print("\nPlease enter a number between 1 to 9.")
        self.switch_player()

    def switch_player(self) :
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self) :
        print("\nQuitting the game ... ")
        print("Thank you for playing! ")
        print("Hope you enjoyed my Tic Tac Toe game!\n")



game = Game()
game.start_game()