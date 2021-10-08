import random

class Player:
    """The player will decide to continue or not, 
    determine if they have enought points to continue
    or to stop playing.
    """

    def __init__(self) -> None:
        """Class constructor.

        Args:
            self(Player): an instance of Player
        """
        self.current_card = 0
        self.last_card = 0
        pass

    def can_continue(self):
        return self.score > 0
        
    def current_card(self):
        self.last_card = self.card_draw
        pass

    def draw_card(self):
        self.card_draw = random.randint(1,13)
        return self.card_draw