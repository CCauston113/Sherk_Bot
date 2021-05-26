# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

responseVocab = { #put here your vocabulary, in the format "keyword":"answer",
"good night": "'Good night.' - Donkey, in Shrek (2001)",
"good sherk": "<:sherk_the_third:810909639909572640> <:axopogtl:814165531019182151>",
"sherk": "<:sherk:807344108204326982> <:sherk_char:807344973929513010> <:sherk_the_third:810909639909572640>"
}
reactHelloString = "hello"

#Alert for discord connect
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#For keyword -> message
@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user: #no replying to own messages, ever (first rule of Discord bots)
        return
        
    #Add reactions
    if reactHelloString in message.content.lower():
        await message.add_reaction('👋')
    
    #Automated responses
    for keyword in responseVocab: #check for each keyword: do we know it?
        if keyword in message.content.lower():
            await channel.send(responseVocab[keyword]) #if yes, send the answer
            break;
            
    


client.run(TOKEN)
