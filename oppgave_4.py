import csv
import numpy as np
import matplotlib.pyplot as plt
 

with open("Skilsmisser_og_ekteskap.csv") as f:
    fil = csv.reader(f, delimiter=";")

    liste = []
    for i in fil:
        liste.append(i)

overskrifter = []
for i in range(len(liste)):
    overskrifter.append(liste[i][0])
    liste[i].pop(0)
print(overskrifter)
print(liste)
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
ingatte_ekteskap = liste[2]
skilsmisser = liste[1]
 
# Set position of bar on X axis
br1 = np.arange(len(ingatte_ekteskap))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2] 
 
# Make the plot
a = []
b = []


"""Gjær det om til int for å få i stigende rekkefølge"""
for i in liste[2]:
    a.append(int(i))
for i in liste[1]:
    b.append(int(i))
    

plt.bar(br1, a, color ='yellow', width = barWidth,
        edgecolor ='grey', label ='Ingåtte ekteskap')
plt.bar(br2, b, color ='blue', width = barWidth,
        edgecolor ='grey', label ='Skilsmisser')
plt.xticks([r + barWidth for r in range(len(ingatte_ekteskap))],liste[0])
plt.xlabel('Årstall', fontweight ='bold', fontsize = 15)
plt.ylabel('Menn og kvinner i vårt langstrakte land', fontweight ='bold', fontsize = 12)
plt.legend()
plt.show()          # Viser diagrammet
# Adding Xticks


