dictonaryL = {"wins": ["wins", "victories", "victory", "win", "won", "attain"],
              "losses": ["losses", "lose", "loss", "lost", "defeat", "defeated", "defeats"],
              "points": ["points"],
              "goals for": ["goals for", "goal for"],
              "goals against": ["goals against", "goal against"],
              "goal difference": ["goal difference", "goal difference"]}

dictonaryE = {"spend": ["spend", "cost", "spent", "fee", "fees"],
              "arrival": ["arrival", "arrivals", "attendants"],
              "income": ["income", "incomes", "revenue"],
              "departures": ["departure", "departure", "leave"],
              "balance": ["profit", "profits", "balance", "balances"],
              "value": ["worth", "value", "values"]}


def strInDict(string, d):
    return string in [x for v in d.values() for x in v]


def getKeyByValue(string, d):
    for key in d:
        wordsList = d.get(key)
        for i in wordsList:
            if i.lower() == string.lower():
                return key
