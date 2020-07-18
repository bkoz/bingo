#
# bingo.py
#

#
# Create an html page of players with playerks to bingo cards.
#

def makePage() :
  title = "<title>Let's Play Bingo</title>"
  header = "<h1>Bingo Cards</h1>"
  print(title)
  print(header)

makePage()

players = "players.txt"
cards = "cards.txt"
with open(players, 'r') as playerLines:
  with open(cards, 'r') as cardLines:
    for player, card in zip(playerLines, cardLines):
        s = "<h2><a href=https://"+str.rstrip(card)+">"+str.rstrip(player)+"</a></h2>"
        print(s)
