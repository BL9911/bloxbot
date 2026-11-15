import os
import discord
from dotenv import load_dotenv

#take token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#initializes connection with default intents (permissions)
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#event that runs when bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

#error if .env is missing or token variable is empty
if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN not found")
    client.run(TOKEN)