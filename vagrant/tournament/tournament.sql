-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

-- Connect to tournament database
\c tournament

-- Drop previous table so that there are no errors when creating
DROP TABLE IF EXISTS players CASCADE;

CREATE TABLE players(
	id serial primary key, name text, wins integer DEFAULT 0, matches integer DEFAULT 0
);

-- Drop previous table so that there are no errors when creating
DROP TABLE IF EXISTS matches CASCADE;

CREATE TABLE matches(
	id serial primary key, winner integer references players(id), loser integer references players(id)
);