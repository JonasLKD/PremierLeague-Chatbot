# MONEYBALL - ChatBot

Module: 4006CEM,
Class: B,
Group: 5

#### Kind reminder: If anyone does obtain any ideas from this project, could you please use our group as a reference.

Description: The objective for this ChatBot is to engage a conversation with a user within specific topics such as: 
* Premier League (league standings data: Position, Points, Goals For, etc...) 
* Global transfers (all player values around the world. *converted to British pounds sterling)
* Economic club value (premier league economic club values such as total asset and income incoming and outcoming transfer fees.)

This ChatBot will feature:
* Discord API
* Player value API
* Keyword Identifier
* File Handler/Analysis

How to use:
* Download all .py files
* Download all .csv files
* Pip install following modules:
  * discord.py
  * nltk
    * nltk.download('punkt') - located near the top in chatter.py, uncomment this
    * nltk.download('averaged_perceptron_tagger') - located near the top in chatter.py, uncomment this
  * pandas
  * re
  * requests
  * bs4
