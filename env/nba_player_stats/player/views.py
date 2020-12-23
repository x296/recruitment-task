import requests
from django.shortcuts import render

def index(request):

	url = 'https://www.balldontlie.io/api/v1/players/{}'
	player_id = 237

	r = requests.get(url.format(player_id)).json()

	player_stats = {
		"id": r['id'],
		"first_name": r['first_name'],
		"last_name": r['last_name'],
		"position": r['position'],
		"height_feet": r['height_feet'],
		"height_inches": r['height_inches'],
		"weight_pounds": r['weight_pounds'],
		"team_name": r['team']['full_name'],
		"conference": r['team']['conference'],
		"division": r['team']['division'],
	}

	context = {'player_stats': player_stats}

	return render(request, 'player/player.html', context)