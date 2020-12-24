from random import randint
import requests
from django.shortcuts import render
from .models import Stats

def index(request):

	# players_list = Stats.objects.all()

	# default_ids = [15, 274, 237, 192, 246, 145, 132, 278, 79]

	players_list = []

	url = 'https://www.balldontlie.io/api/v1/players/{}'

	for _ in range(9):
		r = None
		while r is None:
			try:
				r = requests.get(url.format(randint(1, 300))).json()
			except:
				pass


		player_stats = {
			"id": r['id'],
			"first_name": r['first_name'],
			"last_name": r['last_name'],
			"position": r['position'][0],
			"height_feet": r['height_feet'],
			"height_inches": r['height_inches'],
			"weight_pounds": r['weight_pounds'],
			"team_name": r['team']['full_name'],
			"conference": r['team']['conference'],
			"division": r['team']['division'],
		}

		players_list.append(player_stats)
		r = None

	context = {'players_list': players_list}

	return render(request, 'player/player.html', context)