# discord.py made by GitHub user Rapptz and syntax helped from https://techwithtim.net/tutorials/discord-py
import discord  # discord module allows me to access discord.py functions to open a connection with discord

# modules through initiative
import sys  # sys module allows me to access functions that interact strongly with the interpreter
from datetime import datetime  # datetime modules allows me to format the current time and date

# our contributed modules
from chatter import *


class DiscordChatBot:
    def __init__(self):
        """__init__ allows initialization of attributes for DiscordChatBot class"""
        self.client = discord.Client()  # starts the discord client
        self.start_running = False  # prevents if statements looping on themselves, so when a if statement condition is
        # met it will turn the variable TRUE and then False when finished executing.

    def chatbot_responses(self):
        """formats sentence into natural english, so users are able to understand to highest possible level"""

        @self.client.event
        async def on_ready():
            """coroutine function for when bot becomes online"""
            await self.client.change_presence(status=discord.Status.online,
                                              activity=discord.Game("Type 'hi' to start a conversation"))
            print("ChatBot is ready use.")
            # await msg.channel.send("I'M ONLINE! Type 'hi' to greet.")

        @self.client.event
        async def on_message(message):
            """allows client to receive and send messages via Discord"""
            id = self.client.get_guild(636506898320850945)  # may change so check discord dev portal
            channels = ["bot_owner", "bot_public"]

            """can now add club market function and maybe match stat function and if message doesn't match up with any
            it should pass through all the way to casual conversation 05/11/19 23:40"""

            async def casual_conversation():
                """coroutine function for when words are found within greeting inputs"""
                if message.content.lower() == "quit" or message.content.lower() == "exit":
                    if not self.start_running:
                        self.start_running = True
                        await message.channel.send("Good bye!")
                        self.start_running = False

                elif message.content.lower() == "time?":
                    if not self.start_running:
                        self.start_running = True
                        now = datetime.now()
                        await message.channel.send(now.strftime("Time is %H:%M"))
                        with open('chatlog.txt', 'a') as sys.stdout:
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] {0}: {1}".format(message.author,
                                                                                     message.content.lower())))
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] Bot: {0}".format("Time is %H:%M")))
                        self.start_running = False

                elif message.content.lower() == "date?":
                    if not self.start_running:
                        self.start_running = True
                        now = datetime.now()
                        await message.channel.send(now.strftime("The date is %d/%m/%Y"))
                        with open('chatlog.txt', 'a') as sys.stdout:
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] {0}: {1}".format(message.author,
                                                                                     message.content.lower())))
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] Bot: {0}".format("The date is %d/%m/%Y")))
                        self.start_running = False

                else:
                    if message.author == self.client.user:  # if message by author's user is equal to bot's user
                        return  # basically preventing response to self replies
                    if not self.start_running:
                        self.start_running = True
                        chatOutput = creatingChat(message.content.lower())
                        try:
                            if chatOutput[-1] == "excelDataL":
                                await message.channel.send("{0} had {1} {2} in the"
                                                           " 18/19 Premier League.".format(chatOutput[0][0].title(),
                                                                                           chatOutput[0][1],
                                                                                           chatOutput[1]))
                                # section of formatting a response to the user's request of a team stat, .title() makes
                                # the first letter of the club name a capital
                            elif chatOutput[-1] == "excelDataE":
                                sign = "£"
                                if chatOutput[1] == "arrivals" or "departures":
                                    sign = ""
                                await message.channel.send("{0} had {1}{2} {3} in the"
                                                           " 18/19 Premier League.".format(chatOutput[0][0].title(),
                                                                                           sign,
                                                                                           chatOutput[0][1],
                                                                                           chatOutput[1]))
                            else:
                                print("Error")
                                await message.channel.send(chatOutput[0])
                        except:
                            print("Error")
                            await message.channel.send(creatingChat(message.content.lower()))
                            # exception handling introduced so that when if statement attempts to find a club name
                            # and would normally result to an error, the user may not be talking about football in
                            # general then as there is no club brought up
                        self.start_running = False

            """main if statement for starting a conversation"""
            if str(message.channel) in channels:  # may be removed
                if message.content:  # checking if a message were sent
                    await casual_conversation()

        self.client.run("NjM2NTA2ODk4MzIwODUwOTQ1.XcP-bQ.Ctgip7vMLOQD06oL4F805iLy2wY")
        # allows the client to run using chatbot's application TOKEN from discord developer portal
        # this might change, so check discord developer portal


bot = DiscordChatBot()
bot.chatbot_responses()
