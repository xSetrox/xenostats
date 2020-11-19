# xenostats
Player count statistics for my favorite DarkRP server. Saves current player count every 30 minutes using Source server A2S queries. 

## Usage
Running `it.py` will start recording players.
Make sure you edit the `wantedday` variable on line 5 to the day of the month you want to record on. So if you want to record on the 30th of November, you would set it to 30.
This is so the script will stop recording the next day, and wont start recording until your specified date.

Running `graph.py` will generate a graph of the data. 

## Requirements
```
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.3.3
numpy==1.19.4
Pillow==8.0.1
pyparsing==2.4.7
python-a2s==1.2.1
python-dateutil==2.8.1
six==1.15.0
```
pretty much only A2S and matplotlib, and their requirements as well
