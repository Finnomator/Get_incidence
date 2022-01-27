import json
from requests import *

url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"


def scrap_data():
    response = get(url).text

    interesting = response.split(
        "</thead><tbody>")[1].split("</tbody></table>")[0].replace("\n", "")

    raw_states = interesting.split('<td colspan="1" rowspan="1">')

    raw_extracts = []

    for i in range(len(raw_states)):

        c = raw_states[i].count(
            '</td><td class="right" colspan="1" rowspan="1">')
        raw_extracts.append([])

        for j in range(c):

            raw_extracts[i].append(raw_states[i].split(
                '</td><td class="right" colspan="1" rowspan="1">')[j])

        death_cases = raw_states[i].split('rowspan="1">')[
            raw_states[i].count('rowspan="1">')].split("<")[0]

        raw_extracts[i].append(death_cases)

    raw_extracts.pop(0)

    extracts = {}

    info = ["Anzahl", "Differenz zum Vortag",
            "Fälle in den lezten 7 Tagen", "7-Tage Inzidenz", "Todesfälle"]

    for i in range(len(raw_extracts)):
        state = raw_extracts[i][0]
        state = state.replace("<strong>", "").replace("</strong>", "")
        state = state.replace("Â­","")
        state = state.replace("Ã¼","ü")
        state = state.replace("*","")
        state = state.replace("-<br />"," ")
        raw_extracts[i].pop(0)

        temp = {}

        for j in range(len(raw_extracts[i])):

            temp.update({info[j]: raw_extracts[i][j]})

        extracts.update({state: temp})

    return extracts


def format_nicly(data):

    res = ""

    for state in data:
        res += "\n"+state+":\n"

        for case in data[state]:

            res += "    "
            res += case+": "+data[state][case]+"\n"

    return res


def get_nicly_formated():

    return format_nicly(scrap_data())

if __name__ == "__main__":

    data = scrap_data()

    print(format_nicly(data))

    print()
    print("Source: "+url)
