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
            self.get_inputs()
            #self.do_updates()
            self.do_outputs()


def do_outputs(self):
        while self.can_continue:
            while self.decide_to_play:
                fetch_cart = self.card.display
                fetch_cart = random.randint(1,13)
                print(f"\nThe card is: {fetch_cart}")

                hilo_choice = self.pick_hilo()

                next_card = self.card.guess_card
                next_card = random.randint(1,13)

                if hilo_choice =='h' and self.card.guess_high(fetch_cart,next_card):
                    self.score += 100
                elif hilo_choice =='l' and self.card.guess_low(fetch_cart,next_card):
                    self.score += 100
                else:
                    self.score -= -75

                print(f'\nNext card was:  {next_card}')

                print(f'Your score is: {self.score}')

                break
          
            


    def can_continue(self):
        return self.score > 0
    
    def decide_to_play(self):
        keep_going = input("Keep playing? [y/n]")
        if keep_going == 'y':
            return True
        else:
            return False

    def pick_hilo(self):
        player_choice = input('Higher or lower? [h/l]: ')
        return player_choice


class Card():

    def __init__(self):
        # self.display = random.randint(1,13)
        # #self.score = 300
        # #self.guess_card = random.randint(1,13)
        # self.displayed_card = random.randint(1,13)
        # self.next_displayed_card = random.randint(1,13)

        self.display = 0
        self.guess_card = 0
    

    def guess_high(self, card1_num, card2_num):

        return card1_num > card2_num
    # def next_guess_high(self):
    #     return self.next_displayed_card > self.displayed_card

    def guess_low(self, card1_num, card2_num):
        return card1_num < card2_num
    # def next_guess_low(self):
    #     return self.next_displayed_card < self.displayed_card
        
    """def add_points(self):
        return  100
    def sub_points(self):
        return  75"""
