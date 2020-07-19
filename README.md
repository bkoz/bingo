# Create bingo game

## Do this first:

Generate 30 free bingo cards from https://myfreebingocards.com/numbers/1-75/edit and save the 30 links in 
a text file called `cards.txt`. Also, create a text file with 30 players names called `players.txt`.

#### Create and activate the python environment.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Create the card template

```
python make_bingo_template.py > templates/index.html
```

### Run a flask web server

```
export FLASK_APP=bingo.py
flask http --port=5000
```

### In a 2nd terminal, create a tunnel with ngrok. Have everyone visit the URL reported by ngrok. 

```
$ pip install pyngrok
$ python
python> ngrok http 5000
```

Optionally, create a bit.ly shortcut or create an index.html page with a redirect.

Example:

```
<!DOCTYPE html>
<html>
   <head>
      <title>HTML Meta Tag</title>
      <meta http-equiv = "refresh" content = "2; url = http://f0aa06fe6d77.ngrok.io" />
   </head>
   <body>
      <p>Redirecting ...</p>
   </body>
</html>
```

