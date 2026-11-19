import re
import requests

#since Roblox's API uses universe IDs for game info, we need to convert place IDs to universe IDs first
def place_id_to_universe_id(place_id):
    url = f"https://apis.roblox.com/universes/v1/places/{place_id}/universe"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data.get("universeId")
    print(f"Place lookup failed ({response.status_code}): {response.text}")
    return None

def get_game_info(game_id):
    url = f"https://games.roblox.com/v1/games/?universeIds={game_id}"
    response = requests.get(url, timeout = 10)

    if response.status_code == 200:
        data = response.json()
        if data.get("data"):
           return data["data"][0]  # Return the first game info
    return None