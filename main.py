import discord
from discord.ext import commands
import music
import misc
import os

cogs = [music, misc]
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for cog in cogs:
  cog.setup(client)

print("Starting bot...")
client.run(os.environ["bot-token"])
print("Bot stopping...")