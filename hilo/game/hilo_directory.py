from game.card import Card
import random


class Directory():

    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.card = Card()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        while self.keep_playing:
            # self.get_inputs()
            # self.do_updates()
            self.do_outputs()
            self.card = Card()
            if self.decide_to_play() and self.can_continue():
                pass
            else: 
                return False
            

    def get_inputs(self):
        pass
    """def do_updates(self):
        add_points = self.card.add_points()
        self.score = add_points 
        sub_points = self.card.sub_points()
        self.score = sub_points"""

    def do_outputs(self):        
        """Outputs the flow of results
        """
        while self.can_continue:            
            fetch_cart = self.card.get_random_num()
            #fetch_cart = random.randint(1,13)
            print(f"\nThe card is: {fetch_cart}")

            hilo_choice = self.pick_hilo()

            next_card = self.card.get_random_num()
            #next_card = random.randint(1,13)

            if hilo_choice =='h' and self.card.guess_high(fetch_cart,next_card):
                self.score += 100
            elif hilo_choice =='l' and self.card.guess_low(fetch_cart,next_card):
                self.score += 100
            else:
                self.score -= 75

            print(f'\nNext card was:  {next_card}')

            print(f'Your score is: {self.score}')

            break
    
    def can_continue(self):
        """Decides wheather the player has enought points to continue
        """
        return self.score > 0
    
    def decide_to_play(self):
        """Ask the player if they wish to continue with the game.
        """
        keep_going = input("Keep playing? [y/n]")
        if keep_going == 'y':
            return True
        elif keep_going == 'n':
            return False        
        else:
            return False

    def pick_hilo(self):
        """Ask the player if the next card is higher or lower.
        """
        player_choice = input('Higher or lower? [h/l]: ')
        return player_choice
