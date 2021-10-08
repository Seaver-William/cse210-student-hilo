from game.player import Player

class Diretor:
    """A code template for the director of the Hilo game. 
    This class object keeps track of the score and controls 
    the sequence of the game.

    Attributes:
        keep_playing (boolean): Determine if the game continues
        score  (keep): keep count of the players score
        player (Player): An instance of the class object player.
    """

    def __init__(self):
        """The class constructor
        
        Args:
            self(Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()

    def get_input(self):
        pass

    def update_score(self):
        pass

    def do_output(self):
        print(f'The card is: {self.player.current_card}')
        print(f'Your score is: {self.score}')

        if self.player.can_draw():
            
        pass