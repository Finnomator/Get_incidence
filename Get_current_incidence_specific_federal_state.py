import re
import requests
import time
import sys

class bc:
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"
htmltext = requests.get(url).text.replace("\n","")

useful = re.search('7 Tagen</th><th class="right" colspan="1" rowspan="1">7-Tage-<br />(.*)<div class="teaser gbe target">',htmltext).group(1)

Bundnamen = ["Baden-Württemberg","Bayern","Berlin","Brandenburg","Bremen","Hamburg","Hessen","Mecklenburg-Vorpommern","Niedersachsen","Nordrhein-Westfalen","Rheinland-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schleswig-Holstein","Thüringen"]
Bundeslander = ["Baden-Württem­berg","Bayern","Berlin","Branden­burg","Bremen","Hamburg","Hessen","Meck­lenburg-<br />Vor­pommern","Nieder­sachsen","Nord­rhein-West­falen","Rhein­land-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schles­wig-Holstein","Thüringen"]

print(str(Bundnamen).replace("[","").replace("]","").replace("'",""))

while True:
    Bundesland = input("Wählen Sie eines der oben genannten Bundesländer aus: ")

    if Bundesland in str(Bundnamen):
        break

    time.sleep(0.1)

i = Bundnamen.index(Bundesland)

if Bundesland == "Thüringen":
    Bundeslanduseful = re.search(Bundeslander[i]+'(.*)</strong></td></tr></tbody></table><p><br />',useful).group(1)
else:
    Bundeslanduseful = re.search(Bundeslander[i]+'(.*)'+Bundeslander[i+1],useful).group(1)

for j in range(Bundeslanduseful.count('</td><td class="right" colspan="1" rowspan="1">')):
    Bundeslanduseful = str(Bundeslanduseful).replace('</td><td class="right" colspan="1" rowspan="1">',"###"+str(j)+"###",1)



Anzahl = re.search("###0###(.*)###1###",Bundeslanduseful).group(1)
DifferenzzumVortag = re.search("###1###(.*)###2###",Bundeslanduseful).group(1)
Falleindenletzten7tagen = re.search("###2###(.*)###3###",Bundeslanduseful).group(1)
siebenTageInzidenz = re.search("###3###(.*)###4###",Bundeslanduseful).group(1)
if i == 0 or i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12 or i == 14 or i == 16:
    Todesfalle = re.search('###4###(.*)</td></tr><tr><td colspan="1" rowspan="1">',Bundeslanduseful).group(1)
else:
    Todesfalle = re.search('###4###(.*)</td></tr><tr class="even"><td colspan="1" rowspan="1">',Bundeslanduseful).group(1)

print(bc.UNDERLINE+"\nBundesland: "+Bundesland+":"+bc.ENDC)
print("Anzahl: "+Anzahl)
print("Differez zum Vortag: "+DifferenzzumVortag)
print("Fälle in den letzten sieben Tagen: "+Falleindenletzten7tagen)
print("Sieben Tage Inzidenz: "+siebenTageInzidenz)
print("Todesfälle: "+Todesfalle)

print("\nSource: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html\n")

print("Closing in ",end="")

x = 99

for m in range(x):
    sys.stdout.write(str(x-m))
    sys.stdout.flush()
    for mm in range(len(str(x-m))):
        sys.stdout.write('\b')
    time.sleep(1)