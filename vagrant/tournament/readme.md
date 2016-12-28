--This project was built from forking the Udacity fullstack-nanodegree-vm repository and building upon it for the purpose of the course.

#Swiss Style Tournament Planner

This program can be used to manage your matches and players for a swiss style tournament.

##Installation


To run this program you will need to have Vagrant VM installed. You can download it here: https://www.virtualbox.org/wiki/Downloads

1. Extract the zipped files into your vagrant directory.
2. Using the terminal, `cd` to your `/vagrant` directory.
3. Type `vagrant up` to launch the virtual machine and `vagrant ssh` to log in.
4. Once you are logged in, `cd` to the `/tournament` folder.
5. Setup the database by running the command, `psql -f tournament.sql` 

##Functionality

There are some functions for managing the database of players and matches, as well as some functions for viewing current standings and the next pairs for the tournament.

*`deleteMatches()` and `deletePlayers()` remove their respective records from the database.

*`countPlayers()` will return a number of players that are currently in the database.

*`registerPlayer(name)` takes the name of a player as an argument and will add him or her into the database.

*`playerStandings()` returns a list of tuples containing each players win and loss record.

*`reportMatch()` is the function you will use to add the results of a match into the database.

*`swissPairings()` will return a list of pairs of players for the next round of the match.

## Testing

In order to test the program you must run `tournament_test.py` which will give you details about any errors that occur while running each of the functions.