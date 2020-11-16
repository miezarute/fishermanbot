import discord
from discord.ext import commands



class peixe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='peixe', help='peixe')
    async def peixe(self, ctx):
        await ctx.send('baiacu')





def setup(client):
	client.add_cog(peixe(client))
