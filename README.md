# Create bingo cards

## How to

Generate 30 free bingo cards from https://myfreebingocards.com/numbers/1-75/edit and save the 30 links in 
a text file called `cards.txt`. Create a text file with 30 players called `players.txt.

### Create the card

```
python bingo.py > index.html
```

### Run a web server

```
python -m http.server 5000
```

### Create a tunnel with ngrok

```
$ pip install pyngrok
$ python
python> ngrok http 5000
```


