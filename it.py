import datetime
import time
import a2s
import csv

addr = ("66.70.214.118", 27015)
while True:
    if str(datetime.datetime.now().strftime("%d")) == "17":
        print('incorrect day')
        time.sleep(10)
        continue
    elif str(datetime.datetime.now().strftime("%d")) == "19":
        break
    try:
        pl = len(a2s.players(addr))
    except:
        pl = 0
    curtime = datetime.datetime.now().strftime("%I:%M %p")
    print(curtime,pl)
    with open('playercts.csv', mode='a+') as playerctfile:
        player_writer = csv.writer(playerctfile, delimiter=',')
        player_writer.writerow([str(curtime), pl])
    time.sleep(1800)