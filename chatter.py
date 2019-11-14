# acquired help from nltk module https://www.nltk.org/
import nltk
from nltk.tokenize import MWETokenizer
import csv
import pandas as pd
import re
from API import api
from thesaurus import *

# nltk.download('punkt') # punkt sentence tokenizer divides a text into a list of sentences
# nltk.download('averaged_perceptron_tagger') # average perceptron tagger tags each token in a sentence with
# supplementary information, evaluating what each token means

teams = ['man city', 'liverpool', 'chelsea', 'tottenham', 'arsenal', 'man united', 'wolves', 'everton',
         'leicester city', 'west ham', 'watford', 'crystal palace', 'newcastle', 'bournemouth', 'burnley',
         'southampton', 'brighton', 'cardiff city', 'fulham', 'huddersfield']

leagueStandingsFile = pd.read_csv('league_standings.csv')
leagueEconomics = pd.read_csv("club_economics.csv")


def getClubNames(source):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  # formatted as a docstring due to punctuations being interfering
    for i in source.lower():
        if i in punctuations:
            source = source.replace(i, "")
    # searches for any punctuation then replaces it with an empty space

    source = source.split(" ")
    clubName = ""
    endName = ["city", "united", "ham", "palace"]
    for i in range(0, len(source)):
        for j in teams:
            clubs = (" ".join(teams)).split(" ")
            if source[i].lower() in clubs:
                clubID = clubs.index(source[i].lower())
                if clubs[clubID + 1] in endName:
                    c = "" + clubs[clubID] + " " + clubs[clubID + 1]
                    if source[i + 1] == "united":
                        return "man united"
                    else:
                        return teams[teams.index(c)]
                else:
                    return teams[teams.index(clubs[clubID])]


def getCell(file, index, keyword):
    if (file == "standings"):
        output = leagueStandingsFile.at[int(index), keyword]
    elif (file == "economics"):
        output = leagueEconomics.at[int(index), keyword]
    return output


def getMaxIndex(loN):
    maxNum = loN[0] #current max number
    maxIndex = 0    #index of the max number
    for i in range(len(li)):   #loops through the list
        if maxNum < loN[i]:    #if the current max number is smaller
            maxNum = loN[i]    #current biggest number changes 
            maxIndex = i       #the index changes     
    return maxIndex


def calcPercent(word, source):
    """calculates the percentage of the
        given word"""

    numOfApp = 0
    source = source.split(" ")  # splits by space character
    for i in source:  # loops through the list
        if i.lower() == word.lower():
            numOfApp = numOfApp + 1
    percent = round((numOfApp / len(source)) * 100, 2)  # calculates the percentage
    return percent


def retrieveData(file, keyword, club):
    index = teams.index(club.lower())
    print(index)
    return [club, getCell(file, index, keyword)]


def filetoList(filename):
    """Turns the given file to a list"""
    with open(filename) as csvFile:  # opens the given file
        csvReader = csv.reader(csvFile, delimiter='\n')  # splits contents by newline
        tempList = list(csvReader)  # puts into list
        words = []
        for i in range(len(tempList)):
            words.append(tempList[i][0].split("->"))  # splits by ->
    return words

data = filetoList("data.csv")

def creatingChat(question):
    """allows chatting"""
    result = ""
    # splits the user input
    tokenizedWords = nltk.word_tokenize(question.lower())
    taggedTokens = nltk.pos_tag(tokenizedWords)

    newlemmatizedWords = []

    for i in taggedTokens:
        newlemmatizedWords.append(i[0])

    """calculates the mean of every word the user inputs"""
    averageScore = []  # this will store the mean of every word

    searching = True
    
    for i in data:
        wordsPercent = 0
        if not searching:
            break
        for j in newlemmatizedWords:
            if strInDict(j, dictonaryL):
                searching = False
                clubName = getClubNames(question)
                specialWord = getKeyByValue(j, dictonaryL)
                result = [retrieveData("standings", specialWord, getClubNames(question)), j, "excelDataL"]
                break
            elif strInDict(j, dictonaryE):
                searching = False
                clubName = getClubNames(question)
                specialWord = getKeyByValue(j, dictonaryE)
                result = [retrieveData("economics", specialWord, getClubNames(question)), j, "excelDataE"]
                break
            elif len(re.findall(r"top\s\d{1,2}\splayers?", question)) > 0 or len(re.findall(r"top\splayers?", question)) > 0:
                searching = False
                position = re.findall(r"[1-9][0-9]?", question)
                try:
                    position = int(position[0])
                except IndexError:
                    result = [api(1), "transfers"]
                else:
                    if(position > 12):
                        result = ["Invalid number", "transfers"]
                    else:
                        result = [api(position), "transfers"]  
                break
            else:
                wordsPercent = wordsPercent + calcPercent(j, i[0])
        wordsPercent = wordsPercent / len(newlemmatizedWords)
        averageScore.append(wordsPercent)

    if searching:
        maxIndex = getMaxIndex(averageScore)  # gets the index with the highest mean
        result = [data[maxIndex][1], "other"]
    return result


'''def openChat():
    chatOn = True
    while chatOn:
        userInput = input(">>> ")
        if userInput.lower() == "quit" or userInput.lower() == "exit":
            chatOn = False
            print("Good bye!")
        else:
            output = creatingChat(userInput)
            if(output[-1] == "excelData"):
                print(output)
            elif(output[-1] == "other"):
                print(output[0])
            elif(output[-1] == "transfers"):
                print(output[0])'''

#openChat()

# print(getClubNames("hello, today I am talking about Man City"))
