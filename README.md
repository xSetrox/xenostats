# xenostats
Player count statistics for my favorite DarkRP server. Saves current player count every 30 minutes using Source server A2S queries. 

## Usage
Running `it.py` will start recording players.
Make sure you edit the `wantedday` variable on line 5 to the day of the month you want to record on. So if you want to record on the 30th of November, you would set it to 30.
This is so the script will stop recording the next day, and wont start recording until your specified date.

Running `graph.py` will generate a graph of the data. 
