# UdemyProject2
Udemy Milestone 7 Project - Blackjack. 

First attempt at creating a basic GUI using tkinter.
Super messy Blackjack game that functions on a basic level provided you don't press the wrong buttons.
Some day I may come back to this to improve but for now, I have created a fun little GUI to play Blackjack on.

The code starts out by generating a bunch of global variables.
I generated a deck to include six decks of cards as how it is done in a casino. From there, the deck is shuffled and then card by card is drawn from the pile. Once about 120 cards have been drawn, the whole deck is reshuffled again.
The first function made is the deal card which distributes 2 cards to the player and one card to the dealer to be shown. Those cards go to the dealer and player's dHand and hand respectively.
The player then has the option to hit or stand. These button are not deactivated at any point as this is just a basic game generated in one day.
Hit will keep adding cards until the player goes bust or chooses to stand. 
The check function is used. The cards are added and if an ace is included, and it won't make the player go bust then the 11 value is chosen, otherwise 1 is chosen for the ace.
The player can then stand. This leads to the dealer getting their automated turn which entails drawing cards until they reach 17+ or going bust.
If the player wins, the money they bet as betValue is returned to their money value at double. Else, they lose it.
A push means they get their betValue back.
By making a bet, the money is immediately taken out of the global money variable.

A play again button pops up, covering the other controls (mild form of preventing the user from pushing weird buttons once the game is over)
This will initiate the refresh function that removes all unnecessary labels and refreshing the values except for the previous games score until Deal is pressed to start the next round.
Bet of 100 can be pressed multiple times and should be pressed before the Deal starts but whatever, I don't care.

All in all, pretty good for the first time.
