import discord
from discord.ext import commands


from youtube_dl import YoutubeDL
import time



class Music_cog(commands.Cog):

    def __init__(self,bot) -> None:
        self.vc = discord.VoiceClient
        self.bot = bot

    @commands.command("aaa")
    async def aaa(self, ctx):
  
        await ctx.send("Playing")