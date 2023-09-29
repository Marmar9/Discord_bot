import discord
import asyncio
from discord.ext import commands

from yt_dlp import YoutubeDL
import time

ffmpeg_options = {
    'options': '-vn'
}
youtubedl_options = {
    'format': 'bestaudio/best',
}

url = 'https://www.youtube.com/watch?v=ag8XcMG1EX4&ab_channel=CrowdedHouseVEVO'


Ctx = commands.Context



class Music_cog(commands.Cog):

    def __init__(self,bot) -> None:
        self.vc = discord.VoiceClient
        self.bot = bot

    @commands.command()
    async def play(self, ctx : Ctx):
        message = ctx.message.content.split(" ")
        url = message[1]
        voice = await ctx.message.author.voice.channel.connect(timeout=10000)
        # clients[voice.guild.id] = voice
        ydl = YoutubeDL(youtubedl_options)

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
        await ctx.send("Plaing...")
        # clients[voice.guild.id].play(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options, executable="ffmpeg"))
        voice.play(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options, executable="ffmpeg"))
        
        

        while voice.is_playing():
            await asyncio.sleep(1)

        await voice.disconnect()