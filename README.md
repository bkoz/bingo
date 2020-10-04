# Virtual bingo game

## Do this first:

Generate 30 free bingo cards from the [myfreebingocards](https://myfreebingocards.com/numbers/1-75/edit) site and 
save the 30 links in a text file called `cards.txt`. Also, create a text file with 30 players names 
called `players.txt`.

#### Create the python environment and install the requirements.

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

#### Run the app in a flask web server.

```
export FLASK_APP=bingo.py
flask run 
```

#### In a 2nd terminal, create a tunnel with ngrok. Have everyone visit the URL reported by ngrok. 

```
source venv/bin/activate
ngrok http 5000
```

#### Optionally, create a bit.ly shortcut or create an index.html page on your web server with a redirect.

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

