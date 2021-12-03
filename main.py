import discord
from discord.ext import commands
import music
import misc
from dotenv import load_dotenv
import os
import platform
import keep_alive
import nacl


load_dotenv()


cogs = [music, misc]
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for cog in cogs:
  cog.setup(client)


print("Starting keep alive...")
keep_alive.keep_alive()

print("Starting bot...")
client.run(os.environ["bot-token"], bot=True, reconnect=True)
print("Bot stopping...")