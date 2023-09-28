
#Load env
from dotenv import load_dotenv
import os
load_dotenv('.env')
token:str = os.getenv('TOK')
clients = {}
# Main
import discord
from discord.ext import commands
import time
from yt_dlp import YoutubeDL
import asyncio
#Cogs
from cogs import Music_cog 

ffmpeg_options = {
    'options': '-vn'
}
youtubedl_options = {
    'format': 'bestaudio/best',
}
# url = 'https://www.youtube.com/watch?v=WC7tzEi7D3o&ab_channel=EnergyTV'
# url = 'https://youtu.be/xc_0wfIuuzw?si=4HvACrmrrWfl92mm'
url = 'https://www.youtube.com/watch?v=ag8XcMG1EX4&ab_channel=CrowdedHouseVEVO'

def run():

    intents = discord.Intents.all()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    async def add_cogs():
        await bot.add_cog(Music_cog(bot))

    asyncio.run(add_cogs() )
    
    @bot.command() 
    async def play(ctx: commands.Context):

        voice = await ctx.message.author.voice.channel.connect(timeout=10000)
        # clients[voice.guild.id] = voice
        await ctx.send("Pong")
        ydl = YoutubeDL(youtubedl_options)

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))

        # clients[voice.guild.id].play(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options, executable="ffmpeg"))
        voice.play(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options, executable="ffmpeg"))

        while voice.is_playing():
            await asyncio.sleep(1)

    bot.run(token)



if __name__ == "__main__":
   run()