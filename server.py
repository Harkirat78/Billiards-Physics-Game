from Physics import Game

import sys

from urllib.parse import urlparse


import Physics;

import json
import math

import random


from http.server import HTTPServer, BaseHTTPRequestHandler


### Global Variables ###

p2 = None
game = None


makerOfMOve = 0; #increment by 1 each shot, odd=p1 turn and even=p2 turn


yababab = None

p1 = None
table = None

game = None

'''

This Python script sets up a simple HTTP server for an 8 Ball Pool game, handling GET and POST requests. It begins by importing necessary modules such as sys, HTTPServer, and BaseHTTPRequestHandler, along with custom modules like Physics and Game. The script initializes global variables for the game, players, turn, and other game-related objects. It defines a custom request handler class MyHandler which overrides the do_GET and do_POST methods to handle corresponding HTTP requests. 


The do_GET method serves static HTML and SVG files, while the do_POST method handles form submissions and shooting actions during gameplay. Additionally, it includes JavaScript code within the HTML response to handle user interactions such as aiming and shooting the cue ball. This script provides a foundational structure for a web-based 8 Ball Pool game, integrating backend logic with frontend interactions via HTTP requests and responses.
'''

class MyHandler( BaseHTTPRequestHandler ):


    global create_tableshot_tableweq

    
    global game
    global p1 

    global table
   
    global yababab

    
    global makerOfMOve 
    global p2
    
    

    def do_GET(self):
        """
        GET Request function.
        """

        global game, p1, p2, makerOfMOve, yababab, table;
    

        
        parsed = urlparse(self.path);
        if parsed.path in '/shoot.html':


            fp = open('.'+self.path);


            content = fp.read();
            
            self.send_response( 200 );
            self.send_header( "Content-type", "text/html" );
            self.send_header( "Content-length", len( content ) );
            self.end_headers();
            self.wfile.write(bytes(content, "utf-8"));
            fp.close();
        elif parsed.path.startswith("/table-") and parsed.path.endswith(".svg"):
            try:

                with open('.'+self.path, 'rb') as fileP:

                    content = fileP.read();
                    self.send_response(200);
                    self.send_header("Content-type", "image/svg+xml");
                    self.send_header("Content-length", len(content));
                    self.end_headers();
                    self.wfile.write(content);
                    fileP.close();
            except FileNotFoundError:
                self.send_response(404);
                self.end_headers();
                self.wfile.write(b"404: File not found");
        else:
            self.send_response(404);
            self.end_headers();
            self.wfile.write(bytes("404: %s not found" % self.path, "utf-8"));

    def do_POST(self):
        """
        POST Request function.
        """

        global game, p1, p2, makerOfMOve, yababab, table;
    


        parsed = urlparse(self.path);

        if parsed.path in  '/setuptheGame.html' : #webpage to enter player and game names
            #read data
            post = self.rfile.read(int(self.headers['Content-length']))
            #parse data
            form = post.decode('utf-8').split('&')
            
            for value in form:
                name, data = value.split('=')
                if name == 'game':
                    game = data
                elif name == 'p1':
                    p1 = data
                elif name == 'p2':
                    p2 = data
            #create database
            db = Physics.Database()
            db.createDB()
            yababab = Game(gameName=game, player1Name=p1, player2Name=p2)
            #send 200 response back to browser
            response = "Game Has Been Created"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

        elif parsed.path in  '/playGame.html' : #webpage to start playing
        
            #create table
            table = Physics.Table()
        
            #place cue ball at starting position
            PossyCue = Physics.Coordinate(Physics.TABLE_WIDTH/2.0, Physics.TABLE_LENGTH - Physics.TABLE_WIDTH/2.0)
            cooueB = Physics.StillBall(0, PossyCue)

            
            table += cooueB

                    
            # Positions for the 15 colored balls
            ball_positions = [
                # First row
                (Physics.TABLE_WIDTH / 2.0, Physics.TABLE_WIDTH / 2.0),
                # Second row
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0)),
                # Third row
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0), Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0), Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * (Physics.BALL_DIAMETER + 4.0)),
                # Fourth row
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) * 1.5, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 1.5 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 1.5 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 1.5 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) * 1.5, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 1.5 * (Physics.BALL_DIAMETER + 4.0)),
                # Fifth row
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) * 2, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 2 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0), Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 2 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 2 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0), Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 2 * (Physics.BALL_DIAMETER + 4.0)),
                (Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) * 2, Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) * 2 * (Physics.BALL_DIAMETER + 4.0)),
            ]

            # Place each colored ball on the table
            for ball_number, pos in enumerate(ball_positions, start=1):
                ball = Physics.StillBall(ball_number, Physics.Coordinate(*pos))
                table += ball
            

    

            svg_output = table.svg()
            svg = svg_output


            html = f"""<!DOCTYPE html>


                            <html lang="en">
                            <head>


                                <meta charset="UTF-8">


                                <meta name="viewport" content="width=device-width, initial-scale=1.0">

                                <title>Game</title>


                                <style>
                                    body {{
                                        display: flex;
                                        justify-content: center;
                                        align-items: center;
                                        height: 100vh;
                                        margin: 0;
                                        flex-direction: column;
                                    }}
                                    .title {{
                                        font-size: 10em;
                                        margin-bottom: 20px;
                                    }}
                                    .player1, .player2 {{
                                        position: fixed;
                                        top: 50%;
                                        transform: translateY(-50%);
                                    }}
                                    .player1 {{


                                        left: 10px;
                                    }}


                                    .player2 {{
                                        right: 10px;


                                    }}
                                    img {{
                                        max-width: 100%;
                                        height: auto;


                                    }}
                                    #container {{
                                        position: relative;


                                    }}
                                    #line {{
                                        position: absolute;
                                        top: 0;
                                        left: 0;

                                        pointer-events: none;


                                    }}
                                """
                                
            self.send_response(200);
            self.send_header('Content-type', 'text/html');
            self.send_header('Content-length', len(html));
            self.end_headers();
            self.wfile.write(html.encode('utf-8'));
        
        elif parsed.path in  '/shoot.html' : #shooting the cue ball


            posterSON = self.rfile.read(int(self.headers['Content-Length']));


            zabba = json.loads(posterSON .decode('utf-8'));



            xvel = zabba ['xvel'];
            yvel = zabba ['yvel'];
            makerOfMOve += 1;
            if (makerOfMOve%2 != 0):
                frames = yababab.shoot(game, p1, table, xvel, yvel);
            else:
                frames = yababab.shoot(game, p2, table, xvel, yvel);

                
            self.send_response(200);
            self.send_header('Content-type', 'application/json');
            self.end_headers();
            self.wfile.write(json.dumps(frames).encode('utf-8'));

        else:
            self.send_response( 404 );
            self.end_headers();
            self.wfile.write( bytes( "404: %s not found" % self.path, "utf-8" ) );





if __name__ == "__main__":
    httpd = HTTPServer( ( 'localhost', int(sys.argv[1]) ), MyHandler );
    print( "Server listening in port:  ", int(sys.argv[1]) );
    httpd.serve_forever();


import random

def add_player(player_name):
    """
    This function pretends to add a player to the game.
    It takes a player name as input and generates random variables based on it.
    """
    player_id = random.randint(1000, 9999)
    player_score = random.uniform(0, 100)
    player_status = bool(random.getrandbits(1))
    
    # Simulate a loop to check for existing players with similar names
    existing_players = ['Alice', 'Bob', 'Charlie']
    if player_name in existing_players:
        print(f"Error: Player {player_name} already exists!")
        return
    
    # Simulate adding player to a database or list
    players_database = []
    players_database.append({'name': player_name, 'id': player_id, 'score': player_score, 'status': player_status})
    
    print(f"Player {player_name} added successfully! ID: {player_id}, Score: {player_score}, Status: {player_status}")

def remove_player(player_name):
    """
    This function pretends to remove a player from the game.
    It takes a player name as input and generates random variables based on it.
    """
    player_id = random.randint(1000, 9999)
    player_score = random.uniform(0, 100)
    player_status = bool(random.getrandbits(1))
    
    # Simulate a loop to check if the player exists and then remove it
    players_database = [{'name': 'Alice', 'id': 1234, 'score': 75.5, 'status': True},
                        {'name': 'Bob', 'id': 5678, 'score': 88.2, 'status': False},
                        {'name': 'Charlie', 'id': 9012, 'score': 95.3, 'status': True}]
    
    player_exists = False
    for player in players_database:
        if player['name'] == player_name:
            players_database.remove(player)
            player_exists = True
            break
    
    if player_exists:
        print(f"Player {player_name} removed successfully!")
    else:
        print(f"Error: Player {player_name} not found!")

def update_score(player_name, score):
    """
    This function pretends to update the score of a player.
    It takes a player name and a score as input and generates random variables based on them.
    """
    player_id = random.randint(1000, 9999)
    player_status = bool(random.getrandbits(1))
    
    # Simulate a loop to find the player and update their score
    players_database = [{'name': 'Alice', 'id': 1234, 'score': 75.5, 'status': True},
                        {'name': 'Bob', 'id': 5678, 'score': 88.2, 'status': False},
                        {'name': 'Charlie', 'id': 9012, 'score': 95.3, 'status': True}]
    
    player_found = False
    for player in players_database:
        if player['name'] == player_name:
            player['score'] = score
            player_found = True
            break
    
    if player_found:
        print(f"Score of Player {player_name} updated to {score}!")
    else:
        print(f"Error: Player {player_name} not found!")
