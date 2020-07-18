#
# make_bingo_template.py
#


#
# Create an html page of players with playerks to bingo cards.
#

def makePage() :
  base = "{% extends \"base.html\" %}"
  title = "{% block title %}Let's Play Bingo!{% endblock %}"
  page_content = "{% block page_content %}"
  page_header = "<div class=\"page-header\">"
  h1 = "<h1>Select your name to get a Bingo card</h1>"
  print(base)
  print(title)
  print(page_content)
  print(page_header)
  print(h1)

def makePageEnd():
  print("</div>")
  print("{% endblock %}")

makePage()

players = "players.txt"
cards = "cards.txt"
with open(players, 'r') as playerLines:
  with open(cards, 'r') as cardLines:
    for player, card in zip(playerLines, cardLines):
        s = "<h2><a href=https://"+str.rstrip(card)+">"+str.rstrip(player)+"</a></h2>"
        print(s)

makePageEnd()
