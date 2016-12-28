-- Create new database instance
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

-- Connect to tournament database
\c tournament

-- Drop and previously existing versions of the tables and create new ones

CREATE TABLE players(
	id serial primary key, name text 
);

CREATE TABLE matches(
	match_id serial primary key, winner integer references players(id), loser integer references players(id)
);