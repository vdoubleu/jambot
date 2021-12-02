import discord
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def die(self, ctx):
        print(ctx.author.id)
        if ctx.author.id == 143813149601169408:
            await ctx.send('Goodbye!')
            await self.client.close()
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()
    async def invite(self, ctx):
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=915746983136866344&permissions=3229760&scope=bot')

def setup(client):
  client.add_cog(misc(client))
