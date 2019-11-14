# response = req.get(url='https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1').
# print(response) # This will print out the data coming from that endpoint

from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
import pandas as pd


def api(position):
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 '
                   'Safari/537.36'}

    url = "https://www.transfermarkt.co.uk/premier-league/toptransfers/wettbewerb/GB1/plus/1/galerie/0?saison_id=2018"
    "&land_id=alle&ausrichtung=&spielerposition_id=alle&altersklasse=&w_s=&zuab=zu"

    Tree = requests.get(url, headers=headers)
    Soup = BeautifulSoup(Tree.content, 'html.parser')

    Players = Soup.find_all("a", {"class": "spielprofil_tooltip"})
    Val = Soup.find_all("td", {"class": "rechts"})
    Fee = Soup.find_all("td", {"class": "rechts hauptlink bg_gruen_20"})

    playerList = []
    valList = []
    feeList = []
    empty1 = []

    i = 0
    for i in range(0, position):
        playerList.append(Players[i].text)
        valList.append(Val[i].text)
        feeList.append(Fee[i].text)
        empty1.append('         ')

    df = pd.DataFrame({"Players": playerList, "          ": empty1, "Values": valList, "         ": empty1, "Fee": feeList})
    # table = tabulate(df, headers='keys', tablefmt='psql', showindex=False)
    return df.to_string(index=False)

# api("https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=2000&land_id=&ausrichtung=&spielerposition_id=&altersklasse=o34&leihe=&w_s=")
# api("https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik?saison_id=2019&land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=")
# api("https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=2018&land_id=&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&w_s=i")
# api("https://www.transfermarkt.co.uk/premier-league/toptransfers/wettbewerb/GB1/plus//galerie/0?saison_id=2018&land_id=alle&ausrichtung=&spielerposition_id=alle&altersklasse=&w_s=&zuab=0")
# api("https://www.transfermarkt.co.uk/premier-league/toptransfers/wettbewerb/GB1/plus/1/galerie/0?saison_id=2018&land_id=alle&ausrichtung=&spielerposition_id=alle&altersklasse=&w_s=&zuab=zu")
# print(api(12))
