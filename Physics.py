import phylib;


HEADER = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="700" height="1375" viewBox="-25 -25 1400 2750"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink">
<rect width="1350" height="2700" x="0" y="0" fill="#C0D0C0" />"""


###
FOOTER = """</svg>\n"""

################################################################################
# import constants from phylib to global varaibles
BALL_RADIUS   = phylib.PHYLIB_BALL_RADIUS
BALL_DIAMETER = phylib.PHYLIB_BALL_DIAMETER
HOLE_RADIUS   = phylib.PHYLIB_HOLE_RADIUS
TABLE_LENGTH  = phylib.PHYLIB_TABLE_LENGTH
TABLE_WIDTH   = phylib.PHYLIB_TABLE_WIDTH
SIM_RATE      = phylib.PHYLIB_SIM_RATE
VEL_EPSILON   = phylib.PHYLIB_VEL_EPSILON
DRAG          = phylib.PHYLIB_DRAG
MAX_TIME      = phylib.PHYLIB_MAX_TIME
MAX_OBJECTS   = phylib.PHYLIB_MAX_OBJECTS

# 
BALL_COLOURS = [
    "WHITE",
    "YELLOW",
    "BLUE",
    "RED",
    "PURPLE",
    "ORANGE",
    "GREEN",
    "BROWN",
    "BLACK",
    "LIGHTYELLOW",
    "LIGHTBLUE",
    "PINK",
    "MEDIUMPURPLE",
    "LIGHTSALMON",
    "LIGHTGREEN",
    "SANDYBROWN",
    ]

################################################################################
class Coordinate( phylib.phylib_coord ):
    """
    This creates a Coordinate subclass, that adds nothing new, but looks
    more like a nice Python class.
    """
    pass

class StillBall( phylib.phylib_object ):
    """
    Python StillBall class.
    """

    def __init__( self, number, pos ):
        """
        Constructor function. Requires ball number and position (x,y) as
        arguments.
        """

        # this creates a generic phylib_object
        phylib.phylib_object.__init__( self,
                                       phylib.PHYLIB_STILL_BALL,
                                       number,
                                       pos, None, None,
                                       0.0, 0.0 )

        # this converts the phylib_object into a StillBall class
        self.__class__ = StillBall

    def svg( self ):
        return """ <circle cx="%d" cy="%d" r="%d" fill="%s" />\n""" % (self.obj.still_ball.pos.x, self.obj.still_ball.pos.y, BALL_RADIUS, BALL_COLOURS[self.obj.still_ball.number])

class RollingBall( phylib.phylib_object ):
    """
    Python RollingBall class.
    """

    def __init__( self, number, pos, vel, acc ):
        """
	Constructor function. Requires ball number as well as position,
	velocity, and acceleration in (x,y) form as arguments.
	"""

        phylib.phylib_object.__init__( self,
                                       phylib.PHYLIB_ROLLING_BALL,
                                       number, pos, vel, acc, 0.0, 0.0)
        self.__class__ = RollingBall

    def svg( self ):
        return """ <circle cx="%d" cy="%d" r="%d" fill="%s" />\n""" % (self.obj.rolling_ball.pos.x, self.obj.rolling_ball.pos.y, BALL_RADIUS, BALL_COLOURS[self.obj.still_ball.number])


class Hole( phylib.phylib_object ):
    """
    Python Hole class.
    """

    def __init__(self, pos ):
        """
	Constructor function. Requires hole position as argument.
	"""

        phylib.phylib_object.__init__( self,
			               phylib.PHYLIB_HOLE,
			               None, pos, None, None, 0.0, 0.0)
        self.__class__ = Hole

    def svg( self ):
        return """ <circle cx="%d" cy="%d" r="%d" fill="black" />\n""" % (self.obj.hole.pos.x, self.obj.hole.pos.y, HOLE_RADIUS)


class HCushion(phylib.phylib_object):
    """
    Python HCushion class.
    """

    def __init__(self, y):
        """
        Constructor function. Requires y position as argument.
        """

        phylib.phylib_object.__init__(self, 
                                       phylib.PHYLIB_HCUSHION, 
                                       None,
                                       None,
                                       None, 
                                       None, 
                                       None, 
                                       y)
      
        self.__class__ = HCushion

    def svg(self):
        """
        Generate SVG representation of the HCushion object.
        """

        # if the y position is 0, then the cushion is at the top of the table
        if self.obj.hcushion.y == 0:
            string =  """<rect width="1400" height="25" x="-25" y="%d" fill="darkgreen" />\n""" % (-25)
        else:
            string = """<rect width="1400" height="25" x="-25" y="%d" fill="darkgreen" />\n""" % (2700)
        return string
            

class VCushion(phylib.phylib_object):
    """
    Python VCushion class.
    """

    def __init__(self, x):
        """
        Constructor function. Requires x position as argument.
        """

        phylib.phylib_object.__init__(self, 
                                       phylib.PHYLIB_VCUSHION, 
                                       None,       
                                       None, 
                                       None, 
                                       x, 
                                       None)
      
        self.__class__ = VCushion

    def svg(self):
        """
        Generate SVG representation of the VCushion object.
        """

        # if the x position is 0, then the cushion is at the left of the table
        if self.obj.vcushion.x == 0:
            string =  """<rect width="25" height="2750" x="%d" y="-25" fill="darkgreen" />\n""" % (-25)
        else:
            string = """<rect width="25" height="2750" x="%d" y="-25" fill="darkgreen" />\n""" % (1350)

        return string



################################################################################
class Table( phylib.phylib_table ):
    """
    Pool table class.
    """

    def __init__( self ):
        """
        Table constructor method.
        This method call the phylib_table constructor and sets the current
        object index to -1.
        """
        phylib.phylib_table.__init__( self );
        self.current = -1;

    def __iadd__( self, other ):
        """
        += operator overloading method.
        This method allows you to write "table+=object" to add another object
        to the table.
        """
        self.add_object( other );
        return self;

    def __iter__( self ):
        """
        This method adds iterator support for the table.
        This allows you to write "for object in table:" to loop over all
        the objects in the table.
        """
        return self;

    def __next__( self ):
        """
        This provides the next object from the table in a loop.
        """
        self.current += 1;  
        if self.current < MAX_OBJECTS:   
            return self[ self.current ]; 

        # if we have reached the end of the table, raise StopIteration
        self.current = -1;    
        raise StopIteration;  

    def __getitem__( self, index ):
        """
        This method adds item retreivel support using square brackets [ ] .
        It calls get_object (see phylib.i) to retreive a generic phylib_object
        and then sets the __class__ attribute to make the class match
        the object type.
        """
        result = self.get_object( index )
        if result==None:
            return None
        
        if result.type == phylib.PHYLIB_STILL_BALL:

            result.__class__ = StillBall
        if result.type == phylib.PHYLIB_ROLLING_BALL:
            result.__class__ = RollingBall
        if result.type == phylib.PHYLIB_HOLE:

            result.__class__ = Hole
        if result.type == phylib.PHYLIB_HCUSHION:

            result.__class__ = HCushion
        if result.type == phylib.PHYLIB_VCUSHION:
            result.__class__ = VCushion

        return result

    def __str__( self ):
        """
        Returns a string representation of the table that matches
        the phylib_print_table function from A1Test1.c.
        """
        result = "";    # create empty string
        result += "time = %6.1f;\n" % self.time;    # append time
        for i,obj in enumerate(self): # loop over all objects and number them
            result += "  [%02d] = %s\n" % (i,obj);  # append object description
        return result;  # return the string

    def segment( self ):
        """
        Calls the segment method from phylib.i (which calls the phylib_segment
        functions in phylib.c.
        Sets the __class__ of the returned phylib_table object to Table
        to make it a Table object.
        """

        result = phylib.phylib_table.segment( self )

        # if not none(null), set the class to Table
       
        if result:
            
            result.__class__ = Table
            result.current = -1 # reset the current index
            
            # return the new table
        return result

    def svg( self ):
        string = HEADER
        for obj in self:
            if obj is not None:
                string += obj.svg()
        string += FOOTER
            # return the string
        return string



    # Method to roll the table by a given time
    def roll( self, t ):
        new = Table();
        for ball in self:
            if isinstance( ball, RollingBall ):
            # create4 a new ball with the same number as the old ball
                new_ball = RollingBall( ball.obj.rolling_ball.number,
                                        Coordinate(0,0),
                                        Coordinate(0,0),
                                        Coordinate(0,0) );
                # compute where it rolls to
                phylib.phylib_roll( new_ball, ball, t );
                # add ball to table
                new += new_ball;
            
            if isinstance( ball, StillBall ):
                # create a new ball with the same number and pos as the old ball
                new_ball = StillBall( ball.obj.still_ball.number,
                                    Coordinate( ball.obj.still_ball.pos.x,
                                                ball.obj.still_ball.pos.y ) );
                # add ball to table
                new += new_ball;
        # return table
        return new;

        
    
    # Method to return the cue ball from the table
    def cueBall(self):
        # Find the object representing the cue ball (number 0)
        for obj in self:
            if isinstance(obj, StillBall) and obj.obj.still_ball.number == 0:
                return obj
        
        # If cue ball is not found, raise an error
        raise ValueError("Cue ball not found in the table")


################################################################################
# A3 Code
    
FRAME_RATE = 0.01 # 100 frames per second
import os; # for file operations
import sqlite3; # for database operations
import math; # for mathematical operations

# Create a class to represent the database
class Database:

    # Constructor to create a new database connection
    def __init__(self, reset=False):
        # Database file path
        db_file = 'phylib.db'
        
        # Check if reset is True and delete the existing database file if it exists
        if reset and os.path.exists(db_file):
            os.remove(db_file)
        
        # Open a connection to the database
        #self.conn = sqlite3.connect(db_file)
        #self.cur = self.conn.cursor()

        Database.conn = sqlite3.connect(db_file)
        
    
    # Create the database tables
    def createDB(self):

        cursor = Database.conn.cursor()
        # SQL statements to create tables

        # Create the Ball table that stores the ball number, position, and velocity at specific instance of time
        create_ball_table = """
        CREATE TABLE IF NOT EXISTS Ball (
            BALLID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            BALLNO INTEGER NOT NULL,
            XPOS FLOAT NOT NULL,
            YPOS FLOAT NOT NULL,
            XVEL FLOAT,
            YVEL FLOAT
        )
        """
        # Create the TTable table that stores the table ID and time at a specific instance of time, time here is the length of time since current shot initiated 
        create_ttable_table = """
        CREATE TABLE IF NOT EXISTS TTable (
            TABLEID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            TIME FLOAT NOT NULL 
        )
        """

        # Create the BallTable table that stores the ball ID and table ID to connect balls to their tables by joining the TABLEID of TTable with the BALLID of Ball
        create_balltable_table = """
        CREATE TABLE IF NOT EXISTS BallTable (
            BALLID INTEGER NOT NULL,
            TABLEID INTEGER NOT NULL,
            PRIMARY KEY (BALLID, TABLEID),
            FOREIGN KEY (BALLID) REFERENCES Ball(BALLID),
            FOREIGN KEY (TABLEID) REFERENCES TTable(TABLEID)
        )
        """

        # Create the Shot table that stores the player ID and game ID to which the shot belongs
        create_shot_table = """
        CREATE TABLE IF NOT EXISTS Shot (
            SHOTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            PLAYERID INTEGER NOT NULL,
            GAMEID INTEGER NOT NULL,
            FOREIGN KEY (PLAYERID) REFERENCES Player(PLAYERID),
            FOREIGN KEY (GAMEID) REFERENCES Game(GAMEID)
        )
        """

        # Create the TableShot table that stores the table ID and shot ID to which the table belongs
        create_tableshot_table = """
        CREATE TABLE IF NOT EXISTS TableShot (
            TABLEID INTEGER NOT NULL,
            SHOTID INTEGER NOT NULL,
            PRIMARY KEY (TABLEID, SHOTID),
            FOREIGN KEY (TABLEID) REFERENCES TTable(TABLEID),
            FOREIGN KEY (SHOTID) REFERENCES Shot(SHOTID)
        )
        """

        # Create the Game table that stores the game ID and game name to which the game belongs
        create_game_table = """
        CREATE TABLE IF NOT EXISTS Game (
            GAMEID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            GAMENAME VARCHAR(64) NOT NULL
        )
        """

        # Create the Player table that stores the player ID, game ID, and player name to which the player belongs
        create_player_table = """
        CREATE TABLE IF NOT EXISTS Player (
            PLAYERID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            GAMEID INTEGER NOT NULL,
            PLAYERNAME VARCHAR(64) NOT NULL,
            FOREIGN KEY (GAMEID) REFERENCES Game(GAMEID)
        )
        """
        
        # Execute SQL statements to create tables
        cursor.execute(create_ball_table)
        cursor.execute(create_ttable_table)
        cursor.execute(create_balltable_table)
        cursor.execute(create_shot_table)
        cursor.execute(create_tableshot_table)
        cursor.execute(create_game_table)
        cursor.execute(create_player_table)
        
        # Commit changes and close cursor
        Database.conn.commit()

    def readTable( self, tableID ):
        """
        Reads the content of a specific table from the database and returns a Table object.
        
        Parameters:
        - tableID: The ID of the table to be read from the database.
        
        Returns:
        - A Table object representing the content of the table.
        """
        
        # Open a new cursor for this specific query
        cursor = Database.conn.cursor()
        # SQL query to retrieve balls for the given table
        sql_query = """SELECT * FROM BallTable WHERE BallTable.TABLEID = ?
        """
        
        # Execute the SQL query # Fetch all the results from the query that represent the balls on the table
        cursor.execute(sql_query,(tableID + 1,)); results= cursor.fetchall()
        
        # If no results found, return None
        if not results:
            # Close cursor and commit changes
            cursor.close(); Database.conn.commit()
            # Give a None value
            return None
        
        # Create a new Table object
        table =Table()

        # Loop through the results and add the balls to the table
        cursor.execute("""SELECT * FROM BALL INNER JOIN BallTable ON Ball.BALLID=BallTable.BALLID WHERE BallTable.TABLEID=?""", (tableID+1,))

        # Fetch all the results from the query that represent the balls on the table
        ballObjects= cursor.fetchall()

        # If no results found, return None
        for ballObjects in ballObjects:
            # Create a new Table object
            ballID,ballNO,xPOS,yPOS,xVEL,yVEL,xACC,yACC= ballObjects

            # Add the ball to the table
            if yVEL is None and xVEL is None: ball =StillBall(ballNO, Coordinate(xPOS, yPOS))
            else: 
                # Calculate the speed and acceleration of the ball
                speedVar= math.sqrt((xVEL**2) + (yVEL**2) ); xACC=0;yACC=0
                # Create a new RollingBall object
                if speedVar >VEL_EPSILON: xACC = (-1) * (xVEL) /speedVar*DRAG; yACC= (-1)* (yVEL) /speedVar*DRAG;ball = RollingBall(ballNO, Coordinate(xPOS, yPOS), Coordinate(xVEL, yVEL), Coordinate(xACC, yACC))

            # Add the ball to the table
            table += ball

        # SQL query to retrieve time for the given table
        time_query="""SELECT TIME FROM TTable WHERE TTABLE.TABLEID=?"""
        cursor.execute(time_query,(tableID +1,)); time =cursor.fetchone()

        # Set the time of the table
        table.time =time[0] # Set the time of the table
        cursor.close(); Database.conn.commit()

        # this is the read method table that returns the table
        return table

    def writeTable(self, table):
        """
        Writes the content of a Table object to the database.
        
        Parameters:
        - table: The Table object to be written to the database.
        
        Returns:
        - The autoincremented TABLEID value minus 1.
        """
        
        cursor =Database.conn.cursor()

        # SQL query to insert the time of the table
        # Get the table ID of the last inserted row
        query1="""INSERT INTO TTable (TIME) VALUES (?)"""; cursor.execute( query1,(table.time,) ); iDforTable =cursor.lastrowid

        # Loop through the table and insert the balls into the Ball table
        for obj in table:  
            # Add the ball to the table
            if obj is not None:
                # Add the ball to the table
                if isinstance(obj, StillBall) or isinstance(obj, RollingBall):
                    # Add the ball to the table and insert the ball into the Ball table
                    if isinstance(obj, StillBall): cursor.execute("""INSERT INTO Ball (BALLNO, XPOS,YPOS) VALUES (?, ?,?)""", (obj.obj.still_ball.number,obj.obj.still_ball.pos.x, obj.obj.still_ball.pos.y))
                    # If the ball is a RollingBall and Insert the ball into the Ball table
                    else: cursor.execute("""INSERT INTO Ball (BALLNO,XPOS,YPOS,XVEL,YVEL) VALUES (?, ?,?, ?,?)""",(obj.obj.rolling_ball.number, obj.obj.rolling_ball.pos.x,obj.obj.rolling_ball.pos.y, obj.obj.rolling_ball.vel.x, obj.obj.rolling_ball.vel.y))
        
                    # Get the ball ID of the last inserted row
                    ballId =cursor.lastrowid; cursor.execute("""INSERT INTO BallTable (BALLID, TABLEID) VALUES (?,?)""", (ballId,iDforTable))

        cursor.close(); Database.conn.commit()  # Close the cursor and we close in write and not read because we are writing to the database

        # self.server.close()
        return iDforTable - 1


    # Write the table to the database, stores content of Table class object in the database that it can be perfectly reconstructed by readTable. This method will return the autoincremented TABLEID value minus 1 
    

    # Method to close the database connection
    def close(self):
        
        # Commit any pending changes to the database
        Database.conn.commit()
    
        # Close the database connection
        Database.conn.close()
        
        # Close the database connection
        

    #helpers for init Game
    @staticmethod
    def getGameTest(gameID):
        # Open a new cursor for this specific query
        cursor = Database.conn.cursor()

        # SQL query to retrieve game details
        sql_query = """
        SELECT g.GAMEID, g.GAMENAME, p1.PLAYERNAME, p2.PLAYERNAME
        FROM Game g
        JOIN Player p1 ON g.GAMEID = p1.GAMEID
        JOIN Player p2 ON g.GAMEID = p2.GAMEID
        WHERE g.GAMEID = ?
        ORDER BY p1.PLAYERID ASC
        LIMIT 1
        """
        # Execute the SQL query
        cursor.execute(sql_query, (gameID,))

        # Fetch the result
        result = cursor.fetchone()

        # Close cursor
        cursor.close()

        # If no result found, return None
        if not result:
            return None

        return result

    #@staticmethod
    def setGameTest(self, gameName, player1Name, player2Name):

         # Open a new cursor
        cursor = self.conn.cursor()

        # Insert game into Game table
        insert_game_query = """
        INSERT INTO Game (GAMENAME) VALUES (?)
        """
        cursor.execute(insert_game_query, (gameName,))
        gameID = cursor.lastrowid

        # Insert player1 into Player table
        insert_player1_query = """
        INSERT INTO Player (GAMEID, PLAYERNAME) VALUES (?, ?)
        """
        cursor.execute(insert_player1_query, (gameID, player1Name))

        # Insert player2 into Player table
        insert_player2_query = """
        INSERT INTO Player (GAMEID, PLAYERNAME) VALUES (?, ?)
        """
        cursor.execute(insert_player2_query, (gameID, player2Name))

        # Commit changes to the database
        Database.conn.commit()

        # Close cursor
        cursor.close()



        #Helper for Game shoot
        # Helper method to add a new entry to the Shot table and return the shotID
    @staticmethod
    def newShotTest(gameName, playerName):
        # Open a new cursor
        cursor = Database.connection.cursor()

        # Get the gameID based on the gameName
        gameID_query = "SELECT GAMEID FROM Game WHERE GAMENAME = ?"
        cursor.execute(gameID_query, (gameName,))
        gameID = cursor.fetchone()[0]

        # Get the playerID based on the playerName
        playerID_query = "SELECT PLAYERID FROM Player WHERE PLAYERNAME = ? AND GAMEID = ?"
        cursor.execute(playerID_query, (playerName, gameID))
        playerID = cursor.fetchone()[0]

        # Insert a new entry into the Shot table
        insert_shot_query = "INSERT INTO Shot (PLAYERID, GAMEID) VALUES (?, ?)"
        cursor.execute(insert_shot_query, (playerID, gameID))

        # Get the shotID of the last inserted row
        shotID = cursor.lastrowid

        # Commit changes to the database
        Database.connection.commit()

        # Close cursor
        cursor.close()

        # Return the shotID
        return shotID

    # Helper method to record the table ID and shot ID in the TableShot table
    @staticmethod
    def recordTableShotTest(tableID, shotID):
        # Open a new cursor
        cursor = Database.conn.cursor()

        # Insert the tableID and shotID into the TableShot table
        insert_tableshot_query = "INSERT INTO TableShot (TABLEID, SHOTID) VALUES (?, ?)"
        cursor.execute(insert_tableshot_query, (tableID, shotID))

        # Commit changes to the database
        Database.conn.commit()

        # Close cursor
        cursor.close()

class Game:

    def __init__( self, gameID=None, gameName=None, player1Name=None, player2Name=None ):    
        if gameID is not None and (gameName is not None or player1Name is not None or player2Name is not None):
            raise TypeError("Constructor should be called either with gameID alone or with gameName, player1Name, and player2Name.")

        if gameID is not None:
            self.db = Database()
            # Call helper method to retrieve game details
            self.db.createDB()
            game_data = self.dbgetGame(gameID)
            self.db.gameID = game_data[0]
            self.db.gameName = game_data[1]
            self.db.player1Name = game_data[2]
            self.db.player2Name = game_data[3]
        else:
            # Call helper method to set game details
            self.db = Database()
            self.db.createDB()
            self.db.gameNameTest = gameName
            self.db.player1Name = player1Name
            self.db.player2Name = player2Name
            
            # Call the instance method to set game details
            self.db.setGameTest(gameName, player1Name, player2Name)

        """
            This function registers a shot event in a game and stores it in a database table.

            Args:
                gameName: Name of the game where the shot is fired.
                playerName: Name of the player who fired the shot.
                table: Game elements involved in the shot (potentially).
                xvel: X-velocity of the shot.
                yvel: Y-velocity of the shot.
            """

    '''
    def shoot( self, gameName, playerName, table, xvel, yvel ):
        """
        This function simulates a shot in a game of pool.
        """

        cursor = Database.conn.cursor();

        #retrieve playerID and gameID to update Shot table
        cursor.execute("""SELECT GAMEID
                            FROM Game
                            WHERE Game.GAMENAME=?""", (gameName,));
        gameID = cursor.fetchone();
        cursor.execute("""SELECT PLAYERID
                            FROM Player
                            WHERE Player.PLAYERNAME=?
                                    AND Player.GAMEID=?""", (playerName, gameID[0]));
        playerID = cursor.fetchone();

        #update Shot table based on retrieved playerID and gameID values
        cursor.execute("""INSERT
                            INTO Shot(PLAYERID, GAMEID)
                            VALUES (?, ?)""",
                            (playerID[0], gameID[0]));
        shotID = cursor.lastrowid;

        xpos = None;
        ypos = None;

        
#changing cue ball from a still ball to a rolling ball to begin the "shot"
        for object in table:
            if object is not None and isinstance(object, StillBall) and object.obj.still_ball.number==0:
                xpos = object.obj.still_ball.pos.x;
                ypos = object.obj.still_ball.pos.y;

                object.type = phylib.PHYLIB_ROLLING_BALL;

                object.obj.rolling_ball.pos.x = xpos;
                object.obj.rolling_ball.pos.y = ypos;

                object.obj.rolling_ball.vel.x = xvel;
                object.obj.rolling_ball.vel.y = yvel;

                speed = math.sqrt(xvel**2 + yvel**2);
                xacc = 0;
                yacc = 0;
                if (speed > VEL_EPSILON):
                    xacc = (-1) * xvel / speedDRAG;
                    yacc = (-1) * yvel / speedDRAG;
                object.obj.rolling_ball.acc.x = xacc;
                object.obj.rolling_ball.acc.y = yacc;

                object.obj.rolling_ball.number = 0;


        svgFrames = [];

        #write the "shot" to the database frame-by-frame
        while table:

            startTime = table.time;
            startingTable = table;

            table = table.segment(); #entirety of the "shot"

            if table is not None:

                endTime = table.time;
                length = endTime - startTime; #duration of shot in seconds
                length /= FRAME_INTERVAL;
                length = math.floor(length); #number of frames for the shot
                for i in range(0, length+1): #write each individual frame of the shot to the database

                    curr = i*FRAME_INTERVAL;
                    currentTable = startingTable.roll(curr);
                    currentTable.time = startTime + curr;

                    tableID = self.db.writeTable(currentTable);
                    cursor.execute("""INSERT
                                        INTO TableShot(TABLEID, SHOTID)
                                        VALUES (?, ?)""",
                                        (tableID+1, shotID));

                    currentSvg = currentTable.svg();
                    svgFrames.append(currentSvg);



        cursor.close();
        Database.conn.commit();

        return svgFrames;
        '''






    def shoot( self, gameName, playerName, table, xvel, yvel ):
            # Open a cursor to perform database operations
            cursor =Database.conn.cursor()

            # Retrieve the game ID based on the game name
            cursor.execute("""SELECT GAMEID FROM Game WHERE Game.GAMENAME=?""",(gameName,))
            
            # Fetch the result from the query
            gameID= cursor.fetchone()

            # Retrieve the player ID based on the player name and game ID
            cursor.execute("""SELECT PLAYERID FROM Player WHERE Player.PLAYERNAME=? AND Player.GAMEID=?""", (playerName,gameID[0]))
            # Fetch the result from the query
            playerID =cursor.fetchone()

            # Insert a new entry into the Shot table and retrieve the shot ID
            cursor.execute("""INSERT INTO Shot(PLAYERID, GAMEID) VALUES (?, ?)""", (playerID[0],gameID[0]))
            # Get the shot ID of the last inserted row
            shotID =cursor.lastrowid


            positionOfY = None

            # Initialize variables to store the position and velocity of the cue ball
            positionOfX = None

            # Initialize variables to store the position and velocity of the cue ball

            

            # Iterate through the objects in the table
            for object in table:
                # Check if the object is a StillBall and has number 0 (cue ball)
                if object is not None and isinstance(object, StillBall) and object.obj.still_ball.number== 0:
                    # Retrieve the position of the cue ball
                    positionOfX = object.obj.still_ball.pos.x;positionOfY = object.obj.still_ball.pos.y

                    # Change the object type to RollingBall
                    object.type = phylib.PHYLIB_ROLLING_BALL

                    # Set the position and velocity of the cue ball
                    object.obj.rolling_ball.pos.x = positionOfX; object.obj.rolling_ball.pos.y = positionOfY

                    # Set the velocity of the cue ball
                    object.obj.rolling_ball.vel.x = xvel; object.obj.rolling_ball.vel.y = yvel

                    # Calculate the total velocity of the cue ball
                    Velly = math.sqrt(xvel**2 + yvel**2)

                    # Calculate the acceleration components based on the drag coefficient
                    accelerationX = 0; accelerationY = 0

                    # Calculate the acceleration components based on the drag coefficient
                    if Velly >VEL_EPSILON:

                        accelerationX= (-1) * (xvel) / Velly * DRAG
                        # 

                        # Calculate the acceleration components based on the drag coefficient
                        accelerationY =(-1) * (yvel) / Velly * DRAG

                    # Set the acceleration components of the cue ball
                    object.obj.rolling_ball.acc.x =accelerationX

                    # Set the acceleration components of the cue ball for y axis
                    object.obj.rolling_ball.acc.y= accelerationY

                    # Set the number of the cue ball
                    object.obj.rolling_ball.number = 0

            svgFrames = [];
            # Roll the table and store the intermediate tables in the database
            while table:


                # Get the starting time of the current segment
                begT =table.time; firstTab = table
                # Roll the table to the next segment
                table = table.segment()
                if table is not None:
                    # Get the ending time of the current segment
                    lastT=table.time

                    # Calculate the distance traveled in the current segment
                    distance= lastT - begT

                    # Calculate the distance traveled in the current segment
                    distance =distance / (FRAME_RATE); distance=math.floor(distance)

                    # Iterate through each frame in the current segment
                    for i in range(0, distance + 1):
                        # Calculate the time at the current frame
                        atMom = i * FRAME_RATE

                        # Roll the table to the current frame and get the most recent table
                        mostRecentTab = firstTab.roll(atMom); mostRecentTab.time = begT + atMom

                        # Write the most recent table to the database and retrieve the table ID
                        tableID = self.db.writeTable(mostRecentTab)

                        # Insert an entry into the TableShot table linking the table ID and shot ID
                        cursor.execute("""INSERT INTO TableShot(TABLEID, SHOTID) VALUES (?, ?)""", (tableID + 1, shotID))

                        currentSvg = mostRecentTab.svg();
                        svgFrames.append(currentSvg);

            # Close the cursor and commit the changes to the database
            cursor.close() 

            # Commit the changes to the database
            Database.conn.commit()

            return svgFrames;
