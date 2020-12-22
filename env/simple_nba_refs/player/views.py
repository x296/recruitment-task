import requests
from django.shortcuts import render

def index(request):
	# url = 'https://www.balldontlie.io/api/v1/players/{}'
	# player_id = 237

	# r = requests.get(url.format(player_id)).json()

	# player_stats = {
	# 	'first_name': r['first_name'],
	# 	'last_name': r['last_name'],
	# 	'position': r['position'],
	# 	'height_feet': r['height_feet'],
	# 	'height_inches': r['height_inches'],
	# 	'weight_pounds': r['weight_pounds'],
	# }





	url = 'https://www.balldontlie.io/api/v1/teams'

	r = requests.get(url).json()

	team_list = []

	for team in r['data']:

		team_specs = {
			'id': team['id'],
			'full_name': team['full_name'],
			'roster': [],
		}
		
		team_list.append(team_specs)




	url = 'https://www.balldontlie.io/api/v1/players'

	r = requests.get(url).json()


	for page in range(r['meta']['total_pages']):
		r = requests.get(url.format(page)).json()
		for player in r['data']:
			for team in team_list:
				if player['team']['id'] == team['id']:
					team['roster'].append(player['last_name'])
				

	print(team_list[0])

	# url = 'https://www.balldontlie.io/api/v1/teams'

	# r = requests.get(url).json()

	# team_list = []

	# for team in r['data']:

	# 	team_specs = {
	# 		'id': team['id'],
	# 		'full_name': team['full_name'],
	# 	}
		
	# 	team_list.append(team_specs)


	# print(team_list)

	player_stats = {}

	context = {'team_list': team_list}
	return render(request, 'player/player.html', context)
