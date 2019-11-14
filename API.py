# I have imported the following libraries:

from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
import pandas as pd

# this is a function so the chatbot can scrape football data from transfermarkt.com
# I have used fcpython.com to learn how to do this as I have never used APIs before

def api(position):
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 '
                   'Safari/537.36'}
    
    # This is the url for the data
    url = "https://www.transfermarkt.co.uk/premier-league/toptransfers/wettbewerb/GB1/plus/1/galerie/0?saison_id=2018"
    "&land_id=alle&ausrichtung=&spielerposition_id=alle&altersklasse=&w_s=&zuab=zu"
    
    Tree = requests.get(url, headers=headers)
    Soup = BeautifulSoup(Tree.content, 'html.parser')
    
    # This finds the data within the given classes and assigns the data to variables
    
    Players = Soup.find_all("a", {"class": "spielprofil_tooltip"})
    Val = Soup.find_all("td", {"class": "rechts"})
    Fee = Soup.find_all("td", {"class": "rechts hauptlink bg_gruen_20"})
    
    # Creation of lists used
    
    playerList = []
    valList = []
    feeList = []
    empty1 = []
    
    # loop to add data to the lists
    
    for i in range(0, position):
        playerList.append(Players[i].text)
        valList.append(Val[i].text)
        feeList.append(Fee[i].text)
        empty1.append('         ')
    
    # creates a dataframe
    
    df = pd.DataFrame({"Players": playerList, "          ": empty1,
                       "Values": valList, "         ": empty1, "Fee": feeList})
    
    # returns the results of the function
    
    return df.to_string(index=False)


