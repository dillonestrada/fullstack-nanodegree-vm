#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2



def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error: Failed to connect.")

def deleteMatches():
    """Remove all the match records from the database."""

    db, cursor = connect()

    query = 'TRUNCATE matches CASCADE;'
    cursor.execute(query)
    
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""

    db, cursor = connect()

    query = 'TRUNCATE players CASCADE;'

    cursor.execute(query)
    
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""

    db, cursor = connect()

    query = 'SELECT COUNT(*) FROM players;'
    cursor.execute(query)
    result = cursor.fetchone()[0]
    
    return result

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    db, cursor = connect()

    query = 'INSERT INTO players(name) VALUES (%s)'
    parameter = (name,)
    cursor.execute(query, parameter)

    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    db, cursor = connect()

    query = 'SELECT id, name, COUNT(matches.*) as wins, COUNT(matches.*) as matches FROM players LEFT JOIN matches ON players.id = matches.winner OR players.id = matches.loser GROUP BY id ORDER BY wins;'
    cursor.execute(query)
    result = cursor.fetchall()
    
    return result


print(playerStandings())

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db, cursor = connect()

    query = 'INSERT INTO matches(winner, loser) VALUES (%s, %s)'
    parameters = (winner, loser)
    cursor.execute(query, parameters)
    
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # Makes sure there is an even number of players to create the pairings with.
    if(countPlayers() % 2 == 0):
        standings = playerStandings()
        pairingList = []
        i = 0
        result = curs.fetchall()

        # Creates the list of tuples by looping through the standings
        while(i < len(standings)):
            tup1 = standings[i]
            tup2 = standings[i + 1]

            pairingList.append(tuple((tup1[0], tup1[1], tup2[0], tup2[1])))

            i += 2

    return pairingList
