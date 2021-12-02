import discord
from discord.ext import commands
import music
import misc

cogs = [music, misc]
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for cog in cogs:
  cog.setup(client)

print("Starting bot...")
client.run("OTE1NzQ2OTgzMTM2ODY2MzQ0.YagF1g.u0NpURZHkdY1tytlqvHOByQnlU4")
print("Bot stopping...")