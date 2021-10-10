import random


class Card():

    # def __init__(self):

    # self.display = random.randint(1,13)
    # #self.score = 300
    # #self.guess_card = random.randint(1,13)
    # self.displayed_card = random.randint(1,13)
    # self.next_displayed_card = random.randint(1,13)

    #self.display = 0
    #self.guess_card = 0

    def guess_high(self, card1_num, card2_num):
        return card1_num < card2_num
    # def next_guess_high(self):
    #     return self.next_displayed_card > self.displayed_card

    def guess_low(self, card1_num, card2_num):
        return card1_num > card2_num
    # def next_guess_low(self):
    #     return self.next_displayed_card < self.displayed_card

    def get_random_num(self):
        new_ran_num = random.randint(1, 13)
        return new_ran_num

    """def add_points(self):
        return  100
    def sub_points(self):
        return  75"""
