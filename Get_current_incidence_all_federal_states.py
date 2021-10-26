import re
import requests
import sys
import time

class bc:
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"
htmltext = requests.get(url).text.replace("\n","")

useful = re.search('7 Tagen</th><th class="right" colspan="1" rowspan="1">7-Tage-<br />(.*)<div class="teaser gbe target">',htmltext).group(1)

Bundeslander = ["Baden-Württem­berg","Bayern","Berlin","Branden­burg","Bremen","Hamburg","Hessen","Meck­lenburg-<br />Vor­pommern","Nieder­sachsen","Nord­rhein-West­falen","Rhein­land-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schles­wig-Holstein","Thüringen"]
Bundnamen = ["Baden-Württemberg","Bayern","Berlin","Brandenburg","Bremen","Hamburg","Hessen","Mecklenburg-Vorpommern","Niedersachsen","Nordrhein-Westfalen","Rheinland-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schleswig-Holstein","Thüringen"]

Anzahl = []
DifferenzzumVortag = []
Falleindenletzten7tagen = []
siebenTageInzidenz = []
Todesfalle = []
Bundeslanduseful = []


for i in range(len(Bundeslander)):

    Bundeslanduseful.append("")
    Anzahl.append("")
    DifferenzzumVortag.append("")
    Falleindenletzten7tagen.append("")
    siebenTageInzidenz.append("")
    Todesfalle.append("")

    if i == 15:
        Bundeslanduseful[i] = re.search(Bundeslander[i]+'(.*)</strong></td></tr></tbody></table><p><br />',useful).group(1)
    else:
        Bundeslanduseful[i] = re.search(Bundeslander[i]+'(.*)'+Bundeslander[i+1],useful).group(1)

    for j in range(Bundeslanduseful[i].count('</td><td class="right" colspan="1" rowspan="1">')):
        Bundeslanduseful[i] = str(Bundeslanduseful[i]).replace('</td><td class="right" colspan="1" rowspan="1">',"###"+str(j)+"###",1)

    

    Anzahl[i] = re.search("###0###(.*)###1###",Bundeslanduseful[i]).group(1)
    DifferenzzumVortag[i] = re.search("###1###(.*)###2###",Bundeslanduseful[i]).group(1)
    Falleindenletzten7tagen[i] = re.search("###2###(.*)###3###",Bundeslanduseful[i]).group(1)
    siebenTageInzidenz[i] = re.search("###3###(.*)###4###",Bundeslanduseful[i]).group(1)
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12 or i == 14 or i == 16:
        Todesfalle[i] = re.search('###4###(.*)</td></tr><tr><td colspan="1" rowspan="1">',Bundeslanduseful[i]).group(1)
    else:
        Todesfalle[i] = re.search('###4###(.*)</td></tr><tr class="even"><td colspan="1" rowspan="1">',Bundeslanduseful[i]).group(1)

    print(bc.UNDERLINE+"\nBundesland: "+Bundnamen[i]+":"+bc.ENDC)
    print("Anzahl: "+Anzahl[i])
    print("Differez zum Vortag: "+DifferenzzumVortag[i])
    print("Fälle in den letzten sieben Tagen: "+Falleindenletzten7tagen[i])
    print("Sieben Tage Inzidenz: "+siebenTageInzidenz[i])
    print("Todesfälle: "+Todesfalle[i])

print("\nSource: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html\n")

print("Closing in ",end="")

x = 99

for m in range(x):
    sys.stdout.write(str(x-m))
    sys.stdout.flush()
    for mm in range(len(str(x-m))):
        sys.stdout.write('\b')
    time.sleep(1)