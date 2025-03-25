from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import requests
import os

# Proxy configuration
SMARTPROXY_URL = os.getenv('SMARTPROXY_URL')
SMARTPROXY_USERNAME = os.getenv('SMARTPROXY_USERNAME')
SMARTPROXY_PASSWORD = os.getenv('SMARTPROXY_PASSWORD')


# career stats
def player_career_numbers(player_id):
    # Pass the proxy URL directly to the PlayerCareerStats function
    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id, proxy=f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001")

    # Get the player's career stats as a dictionary
    career_dict = player_stats.get_normalized_dict()

    return career_dict

# regular season totals
def player_regular_season(player_id):
    
    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id, proxy=f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001")
    dict_response = player_stats.get_normalized_dict()  # Getting dictionary response

    regular_season_totals = dict_response['SeasonTotalsRegularSeason']

    return regular_season_totals


# playoff totals
def player_post_season(player_id):
    # Construct the proxy URL
    

    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id, proxy=f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001")
    dict_response = player_stats.get_normalized_dict()  # Getting dictionary response

    post_season_totals = dict_response['SeasonTotalsPostSeason']

    return post_season_totals

