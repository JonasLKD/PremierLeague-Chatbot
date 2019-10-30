import discord  # discord module allows me to access discord.py functions to open a connection with discord
"""discord.py made by GitHub user Rapptz"""
import sys  # sys module allows me to access functions that interact strongly with the interpreter
import random  # random module allows me to access random selection functions
from datetime import datetime  # datetime modules allows me to format the current time and date


class DiscordChatBot:
    def __init__(self):
        """__init__ allows initialization of attributes for DiscordChatBot class"""
        self.client = discord.Client()  # starts the discord client
        self.start_running = False

        with open("greeting inputs.txt") as a:
            greeting_inputs = a.readlines()
        self.greeting_inputs = [x.strip() for x in greeting_inputs]

        with open("greeting outputs.txt") as b:
            self.greeting_outputs = b.read().splitlines()
            # may need a whole python file for reading a striping text files, which will be located in the same
            # directory

    def chatbot_responses(self):
        """contains all possible responses from a user"""
        @self.client.event
        async def on_ready():
            await self.client.change_presence(status=discord.Status.online,
                                              activity=discord.Game("Type 'hi' to start a conversation"))
            print("ChatBot is ready.")
            # await msg.channel.send("I'M ONLINE! Type 'hi' to greet.")

        @self.client.event
        async def on_message(message):
            """allows client to receive and send messages via Discord"""
            id = self.client.get_guild(636506898320850945)  # may change so check discord dev portal
            channels = ["bot_owner", "bot_public"]

            if str(message.channel) in channels:  # may be removed
                if message.content.lower() in self.greeting_inputs:
                    if not self.start_running:
                        self.start_running = True
                        now = datetime.now()
                        greeting_outputs = random.choice(self.greeting_outputs)
                        await message.channel.send(greeting_outputs)
                        with open('chatlog.txt', 'a') as sys.stdout:
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] {0}: {1}".format(message.author,
                                                                                     message.content.lower())))
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] Bot: {0}".format(greeting_outputs)))
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
                        # basically preventing response to self replies
                        return
                    if not self.start_running:
                        self.start_running = True
                        now = datetime.now()
                        await message.channel.send("I don't understand this yet!")
                        with open('chatlog.txt', 'a') as sys.stdout:
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] {0}: {1}".format(message.author,
                                                                                     message.content.lower())))
                            print(now.strftime("[%d/%m/%Y %H:%M:%S] Bot: I don't understand this yet!"))
                        self.start_running = False

        self.client.run("NjM2NTA2ODk4MzIwODUwOTQ1.XbA7hw.P_sHA_kRXe2QrX4CXDI29Wmf5-w")
        # allows the client to run using chatbot's application TOKEN from discord developer portal
        # this might change, so check discord developer portal


bot = DiscordChatBot()
bot.chatbot_responses()
