#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    # Remove all the match records from the database.
    db = connect()
    c = db.cursor()
    c.execute("delete from games;")
    db.commit()
    db.close()

def deletePlayers():
    # Remove all the player records from the database.
    db = connect()
    c = db.cursor()
    c.execute("delete from games;")
    c.execute("delete from players;")
    db.commit()
    db.close()

def countPlayers():
   # Returns the number of players currently registered.
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(id) FROM players;")
    maxplayers = c.fetchall()[0][0]
    db.commit()
    db.close()
    return maxplayers

def registerPlayer(name):
    # Adds a player to the tournament database.
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    c.execute("INSERT INTO games (wins, matches) VALUES (0, 0);")
    db.commit()
    db.close()


def playerStandings():
    # Returns a list of the players and their win records, sorted by wins.
    db = connect()
    c = db.cursor()
    c.execute("""SELECT players.id, players.name,
    coalesce(games.wins, 0) as wins, coalesce(games.matches, 0) as matches
    FROM players LEFT JOIN games ON players.id = games.id
    ORDER BY wins DESC""")
    playerlist = c.fetchall()
    db.commit()
    db.close()
    return playerlist

def reportMatch(winner, loser):
    # Records the outcome of a single match between two players.
    db = connect()
    c =db.cursor()
    c.execute("""UPDATE games SET wins = wins + 1, matches = matches + 1
    WHERE id = %s""", (winner,))
    c.execute("""UPDATE games SET matches = matches + 1
    WHERE id = %s""", (loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    # Returns a list of pairs of players for the next round of a match.
    db = connect()
    c = db.cursor()
    c.execute("""SELECT players.id, players.name, games.wins, games.matches
    FROM players join games on players.id = games.id 
    ORDER BY wins DESC;""")
    row = c.fetchall()

    ListOfPairs = []
    for index in xrange(0, len(row), 2):
        tup = (row[index][0], row[index][1], row[index + 1][0], row[index + 1][1])
        ListOfPairs.append(tup);


    db.commit()
    db.close()
    return ListOfPairs


