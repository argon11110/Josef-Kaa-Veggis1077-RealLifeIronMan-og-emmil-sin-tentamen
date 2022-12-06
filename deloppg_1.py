from pathlib import Path
import math
import csv
import matplotlib.pyplot as plt

file = Path(__file__).parent

filnavn = "Befolkning.csv"
aar = []
befolkning = []
with open(f"{file}/{filnavn}", encoding="utf-8-sig") as fil:
    filen = csv.reader(fil, delimiter=";")

    overskrifter = next(filen)
    for rad in filen:
        aar.append(rad[0])
        befolkning.append(int(rad[1]))


fig, ax = plt.subplots()
plt.xlabel("Årstall")
plt.ylabel("Befolkning")
plt.title("Norges befolkning  1769 - 2022")
ax.plot_date(aar, befolkning, marker='', linestyle='-')
ax.set_xticks(ax.get_xticks()[::15])
fig.autofmt_xdate()
plt.margins(0.05)
plt.tight_layout()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()
