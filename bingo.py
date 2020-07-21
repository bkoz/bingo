from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
  players = "players.txt"
  cards = "cards.txt"
  #
  # href is a list of lists where each sublist contains a card URL and a player name.
  #
  href = [ ]
  p = [ ]
  c = [ ]
  #
  # Read in the player and card files, create an list of lists
  # that the template can render as a series of href tags.
  #
  with open(players, 'r') as playerLines:
    with open(cards, 'r') as cardLines:
      for player, card in zip(playerLines, cardLines):
        p.append(str.rstrip(player))
        c.append(str.rstrip(card))
        myList=[str.rstrip(card), str.rstrip(player)]
        href.append(myList)
  return render_template('index.html',playerList=href)

#
# Not used
#
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
