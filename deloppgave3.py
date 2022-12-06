import matplotlib.pyplot as plt
import json
import csv

with open("Siviltilstand.json", encoding = "utf-8") as file:
    data = json.load(file)

aar = []
befolkning = []

with open("Befolkning.csv", encoding = "utf-8-sig") as file:
    data2 = csv.reader(file, delimiter = ";")
    
    overskrifter = next(data2)
    for row in data2:
        aar.append(row[0])
        befolkning.append(int(row[1]))

values = (data["dataset"]["value"])
years = list(data["dataset"]["dimension"]["Tid"]["category"]["index"].keys())
labels = list(data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"].values())

listOfLists = []
items = []

for i in range(0, (len(values))):
    if (i + 1) == (len(values)):
        items.append(values[i])
        items.append(values[i])
        listOfLists.append(items)
    elif i % 42 == 0 and i != 0:
        items.append(values[i])
        listOfLists.append(items)
        items = []
    else:
        items.append(values[i])

fig, ax = plt.subplots(2, 1)
listOfLists[0].pop(-1)
plt.subplot(2, 1, 1)
fig.autofmt_xdate()
plt.plot(years, listOfLists[0], label = "Ugift")
plt.plot(years, listOfLists[1], label = "Gift")
plt.plot(years, listOfLists[2], label = "Enke/enkemann")
plt.plot(years, listOfLists[3], label = "Separert")
plt.plot(years, listOfLists[4], label = "Skilt")
plt.grid(axis = "y")
plt.legend()
plt.title("Sivilstatus i Norge over tid")

plt.subplot(2, 1, 2)
fig.autofmt_xdate()
plt.plot(aar, befolkning, label = "Befolkning")
plt.grid(axis = "y")
plt.legend()
plt.xticks([0, 11, 22, 33, 44, 55, 66, 77, 88, 110, 99, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253])
plt.title("Befolkning i Norge over tid")

plt.show()