"""Program to genrate Bingo

Docstring comments go here.
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    """
    Render a 404 message.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Render a 500 message.
    """
    return render_template('500.html'), 500


@app.route('/')
def index():
    """
    Handle the default route.
    """
    players = "players.txt"
    cards = "cards.txt"
    #
    # href is a list of lists where each sublist contains a card URL and a player name.
    #
    href = [ ]
    player_list = [ ]
    card_list = [ ]
    #
    # Read in the player and card files, create an list of lists
    # that the template can render as a series of href tags.
    #
    with open(players, 'r') as player_lines:
        with open(cards, 'r') as card_lines:
            for player, card in zip(player_lines, card_lines):
                player_list.append(str.rstrip(player))
                card_list.append(str.rstrip(card))
                my_list=[str.rstrip(card), str.rstrip(player)]
                href.append(my_list)
    return render_template('index.html',playerList=href)

@app.route('/user/<name>')
def user(name):
    """
    Handle the user name route
    """
    return render_template('user.html', name=name)
