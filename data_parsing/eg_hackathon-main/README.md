# eg_hackathon
Hi! This is a personal note from Beora

Before I get into anything, thanks for signing up for this event and I really hope you have fun playing around with the data provided! If you have any questions feel free to message me on discord @Beora (I might not respond right away depending on if I am at my pc / not busy but I will try my best)

----------------------------------------------------------

In this folder I included .pqt files for the following tables, all of which contain data for all games played by GG and C9 throughout the 2023 regular season and playoffs

### Game Summary
####################

This table includes data related to the overview of a match, things like which teams faced off, and more importantly / relevant what the PB order looked like. Also features some extra columns to assist with ease of analysis at the end like 'team_1_sup' and 'team_1_sup_pick_order' so you don't have to do as much data manipulation to get where you want to go

--

### Player Game Stats
#########################

This table provides data in a per-row format per player in each game, with data related to their overall stats (basically think post-game lobby stats) - super useful for stuff like CS/m, GD/m, DPM, KDA, etc. 

!!! WARNING: Ignore the TEAMFIGHT and PROX statistics, uses old models set up in 2018 and not the newer ones that I've established more recently, not very reliable. If you do want to get stats related to teamfights/prox I would highly advise to extrapolate them yourselves. 

--

### Snapshot Player Stats
#############################

This table provides a per second snapshot of the entire game for all 10 players, great for getting into the nitty gritty of a match. Useful for finding things like Jungle Pathing and other rotational / position based events (or really anything you can think of, this is a firehose of information, love this table)

--

### Wards Placed
####################

This table is pretty self explanatory, has all relevant data regarding wards placed including position, ward type, and game time, etc.

--

### Objective Kills
#######################

This table is similar to the above but includes kills for anything ranging from a jungle camp to a dragon/baron/rift





