#
# bingo.py
#

#
# Create an html page of players with playerks to bingo cards.
#

players = "players.txt"
cards = "cards.txt"
with open(players, 'r') as playerLines:
  with open(cards, 'r') as cardLines:
    for player, card in zip(playerLines, cardLines):
        s = "<a href=https://"+str.rstrip(card)+">"+str.rstrip(player)+"</a><br>"
        print(s)
