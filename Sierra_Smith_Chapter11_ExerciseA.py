# Poker Game Demo
# This program uses the random.shuffle method and a class (Deck) for simulating a poker game.
# The class uses the .shuffle method on the card_list and deals a hand of 5 cards from the end
# of the list using the .pop method. The player gets to choose which cards they want to replace -
# those cards go into the discard pile and are replaced with random cards from the card_list.

# module used for implementing the .shuffle method
import random

import time

DIV = "▰▱▰▱▰▱▰▱▰▱▰▱▰▱"

# class that resembles a deck of cards;
# also includes methods for shuffling and dealing the cards
class Deck:

    def __init__(self, n_decks = 1):

        self.card_list = [num + suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A2345678TJQK'
            for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    # method for dealing new cards and reshuffling the discards_list
    # when there are no cards left in the card_list
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...")
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)

        return new_card

    # method for mixing all the cards back together and
    # clearing the player's hand
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# beginning and ending function of the program
def main():

    # welcome and game messages
    print(DIV)

    print("\nWelcome to the casino!\n")

    print(DIV)

    print("We are playing poker.\n")

    # dealer message
    print("Dealing your hand...\n")

    time.sleep(2.1)

    # instantiate Deck class
    dk = Deck()

    print("Your cards:")

    # use deal method from Deck class to deal new cards
    for i in range(5):
        print(dk.deal(), end='  ')

    # get input from user
    str_nums = input("\n\nEnter the numbers corresponding to the cards you want to draw, "
                    "for example: 1, 3, 5\n")

    # add the numbers entered by the user into a list after splitting them
    str_nums_list = str_nums.split(", ")

    # convert split strings into list of integers
    int_nums = [int(str_) for str_ in str_nums_list]

    # list that will be filled with valid indexes
    indexes = []

    # convert user input to indexes matching the cards they want to replace
    for num in range(len(int_nums)):

        # define the starting index
        ind = 0

        # pop user inputted value out of the list and save it to i
        i = int_nums.pop(ind)

        # minus one from every .pop value
        i -= 1

        # append the value to the indexes list
        indexes.append(i)

        # add 1 to the index for the above statements to iterate through
        ind += 1

    # for each number in the indexes list,
    for num in indexes:

        # assign the card at the given index as a discard_card
        discard_card = dk.cards_in_play_list[num]

        # append the discard_card to the Deck's discard_list
        dk.discards_list.append(discard_card)

    # if a card in the discard_list matches a card in cards_in_play_list,
    # remove it from the cards_in_play_list
    for card in dk.discards_list:

        if card in dk.cards_in_play_list:

            dk.cards_in_play_list.remove(card)

    # for the number of cards the player wants to draw, deal a new card
    for i in indexes:

        dk.deal()

    print("Drawing...\n")

    time.sleep(2)

    print("Your new hand:")

    # print each card out from the cards_in_play_list
    for card in dk.cards_in_play_list:

        print(card, end='  ')

    time.sleep(3)

    # end-of-demo message
    print("\n\nThis is the end of the demo. Thank you for playing!")

    time.sleep(5)

# start the program
main()