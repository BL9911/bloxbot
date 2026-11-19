import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from roblox_api import get_game_info, place_id_to_universe_id

#take token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#initializes connection with default intents (permissions)
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#event that runs when bot is ready
@client.event
async def on_ready():
    await tree.sync()  # Syncs the command tree with Discord
    print(f'Logged in as {client.user}')

@tree.command(name="gameinfo", description="Get Roblox game info by place ID")
@app_commands.describe(game_id="The Roblox place ID")
async def get_game_info_command(interaction: discord.Interaction, game_id: str):
    await interaction.response.defer()  # Acknowledge the command to avoid timeout
    universe_id = place_id_to_universe_id(game_id)
    if not universe_id:
        await interaction.followup.send("Place ID not found or an error occurred.")
        return
    
    game_info = get_game_info(universe_id)
    if not game_info:
        await interaction.followup.send("Game not found from Universe ID.")
        return
    await interaction.followup.send(f"Game Info: {game_info}" if game_info else "Game not found or an error occurred.")

#error if .env is missing or token variable is empty
if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN not found")
    client.run(TOKEN)