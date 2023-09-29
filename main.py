
#Load env
from dotenv import load_dotenv
import os
load_dotenv('.env', override=True)

token:str = os.getenv('TOKEN')
# Main
import discord
from discord.ext import commands
import time

import asyncio
#Cogs
from cogs import Music_cog 


# url = 'https://www.youtube.com/watch?v=WC7tzEi7D3o&ab_channel=EnergyTV'
# url = 'https://youtu.be/xc_0wfIuuzw?si=4HvACrmrrWfl92mm'
url = 'https://www.youtube.com/watch?v=ag8XcMG1EX4&ab_channel=CrowdedHouseVEVO'

def run():

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="\\", intents=intents)

    async def add_cogs():
        await bot.add_cog(Music_cog(bot))

    asyncio.run(add_cogs() )


    bot.run(token)



if __name__ == "__main__":
   run()