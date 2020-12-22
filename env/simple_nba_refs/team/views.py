import requests
from django.shortcuts import render

def index(request):
	url = 'https://www.balldontlie.io/api/v1/teams'

	r = requests.get(url).json()

	team_list = []

	for team in r['data']:

		team_specs = {
			'id': team['id'],
			'full_name': team['full_name'],
		}
		
		team_list.append(team_specs)


	context = {'team_list': team_list}
	return render(request, 'team/team.html', context)


# Version 0.1

# import requests
# from django.shortcuts import render

# def index(request):
# 	url = 'https://www.balldontlie.io/api/v1/teams'

# 	r = requests.get(url).json()

# 	team_list = []

# 	for team in r['data']:
# 		team_list.append({team['id']: team['full_name']})

# 	print(team_list)

# 	team_stats = {
# 		'full_name': r['full_name'],
# 	}

# 	context = {'team_stats': team_stats}
# 	return render(request, 'team/team.html', context)
