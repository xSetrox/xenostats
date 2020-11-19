import matplotlib.pyplot as plt
from matplotlib import style

X = []
Y = []
with open('playercts.csv', mode='r+') as playerctfile:
    for row in playerctfile:
        vals = row.split(',')
        if len(vals) < 2:
            continue
        xt = vals[0].strip()
        yt = int(vals[1].strip())
        X.append(xt)
        Y.append(yt)
print(X)
print(Y)
plt.figure(figsize=(14,6))
plt.plot(X,Y)
# Labeling the X-axis
plt.xlabel('Time')
# Labeling the Y-axis
plt.ylabel('Players')
# Give a title to the graph
plt.title('XenoRP players over time')
plt.xticks(fontsize=10,rotation='vertical')
plt.grid()
#style.use('fivethirtyeight')
plt.show()