dictonaryL = {"wins": ["wins", "victories", "victory", "win", "won", "attain"],
              "losses": ["losses", "lose", "loss", "lost", "defeat", "defeated", "defeats"],
              "points": ["points"],
              "draws": ["draw", "draws", "tie"]
              "goals for": ["goals for", "goal for"],
              "goals against": ["goals against", "goal against"],
              "goal difference": ["goal difference", "goal difference"]}

dictonaryE = {"spend": ["spend", "cost", "spent", "fee", "fees"],
              "arrivals": ["arrival", "arrivals", "attendants"],
              "income": ["income", "incomes", "revenue"],
              "departures": ["departure", "departure", "leaves", "leavers", "left"],
              "balance": ["profit", "profits", "balance", "balances"],
              "value": ["worth", "value", "values", "total"]}


def strInDict(string, d):
    return string in [x for v in d.values() for x in v]


def getKeyByValue(string, d):
    for key in d:
        wordsList = d.get(key)
        for i in wordsList:
            if i.lower() == string.lower():
                return key
