import json
import matplotlib.pyplot as plt

with open("Siviltilstand.json", encoding = "utf-8") as file:
    data = json.load(file)

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

fig, ax = plt.subplots()
#ax.set_xticks(ax.get_xticks()[::5])
fig.autofmt_xdate()
listOfLists[0].pop(-1)
plt.plot(years, listOfLists[0], label = "Ugift")
plt.plot(years, listOfLists[1], label = "Gift")
plt.plot(years, listOfLists[2], label = "Enke/enkemann")
plt.plot(years, listOfLists[3], label = "Separert")
plt.plot(years, listOfLists[4], label = "Skilt")

plt.grid(axis = "y")
plt.legend()
plt.title("Sivilstatus i Norge over tid")
plt.show()