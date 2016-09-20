# Given a list of basketball players stored as Python dictionaries:

players = [
  {
    'name': 'Paul Millsap',
    'position': 'PF',
    'avgMinutesPlayed': 36,
    'avgPoints': 16.4,
    'avgRebounds': 9.4,
    'starter': True
  },
  {
    'name': 'Jeff Teague',
    'position': 'PG',
    'avgMinutesPlayed': 28.6,
    'avgPoints': 15.6,
    'avgRebounds': 1.9,
    'starter': True
  },
  {
    'name': 'Al Horford',
    'position': 'C',
    'avgMinutesPlayed': 32,
    'avgPoints': 13.2,
    'avgRebounds': 6.8,
    'starter': True
  },
  {
    'name': 'Kent Bazemore',
    'position': 'SF',
    'avgMinutesPlayed': 31.8,
    'avgPoints': 12,
    'avgRebounds': 6.6,
    'starter': True
  },
  {
    'name': 'Kyle Korver',
    'position': 'SG',
    'avgMinutesPlayed': 32.4,
    'avgPoints': 11.2,
    'avgRebounds': 4.9,
    'starter': True
  },
  {
    'name': 'Dennis Schroder',
    'position': 'PG',
    'avgMinutesPlayed': 18.3,
    'avgPoints': 10.7,
    'avgRebounds': 1.8,
    'starter': False
  },
  {
    'name': 'Kris Humphries',
    'position': 'PF',
    'avgMinutesPlayed': 14.7,
    'avgPoints': 9.7,
    'avgRebounds': 5.7,
    'starter': False
  },
  {
    'name': 'Mike Scott',
    'position': 'PF',
    'avgMinutesPlayed': 17.6,
    'avgPoints': 7.0,
    'avgRebounds': 3.6,
    'starter': False
  },
  {
    'name': 'Thabo Sefolosha',
    'position': 'SF',
    'avgMinutesPlayed': 18.9,
    'avgPoints': 4.8,
    'avgRebounds': 3.9,
    'starter': False
  },
  {
    'name': 'Mike Muscala',
    'position': 'PF',
    'avgMinutesPlayed': 7.4,
    'avgPoints': 2.7,
    'avgRebounds': 1.9,
    'starter': False
  },
  {
    'name': 'Tim Hardaway Jr.',
    'position': 'SG',
    'avgMinutesPlayed': 9.7,
    'avgPoints': 2.2,
    'avgRebounds': 1.0,
    'starter': False
  },
  {
    'name': 'Lamar Patterson',
    'position': 'SG',
    'avgMinutesPlayed': 5.0,
    'avgPoints': 1.5,
    'avgRebounds': 1.3,
    'starter': False
  },
  {
    'name': 'Kirk Hinrich',
    'position': 'SG',
    'avgMinutesPlayed': 4.5,
    'avgPoints': 0.8,
    'avgRebounds': 0.7,
    'starter': False
  }
]

# Example loop
# for player in players:
#   for key, value in player.iteritems():
#     print key + ' - ' + str(value) #Same as player[key]


# * Print the average playing time of the players.
total_time = 0

for player in players:
  total_time += player['avgMinutesPlayed']
  avg_time = total_time / len(players)

print avg_time


# * Print the average playing time of the starters.

total_time = 0
player_count = 0

for player in players:
  if player['starter'] == True:
    player_count += 1
    total_time += player['avgMinutesPlayed']
    avg_starter_time = total_time / player_count

print avg_starter_time  

# * Print the average playing time of the bench players.

total_time = 0
bench_player_count = 0

for player in players:
  if player['starter'] == False:
    bench_player_count += 1
    total_time += player['avgMinutesPlayed']
    avg_bench_time = total_time / bench_player_count

print avg_bench_time  

# * Create an array of the names of each player.

player_name_array = []
for player in players:
  player_name_array.append(player['name'])

print player_name_array  

# * Create an array of the names of the players who average more than 10 points per game.

high_score_array = []
for player in players:
  if player['avgPoints'] >= 10:
    high_score_array.append(player['name'])

print high_score_array  

# * Create an array of the names of the players who average more than 5 rebounds per game.

big_rebounders = []
for player in players:
  if player['avgRebounds'] >= 5:
    big_rebounders.append(player['name'])

print big_rebounders

# * Who is the player with the most points per minute played? Write a program to find that out.

def highest_ppm():
  temp_highest = 0
  player_name = ''
  for player in players:
    ppm = player['avgPoints']/ player['avgMinutesPlayed']
    if ppm > temp_highest:
      temp_highest = ppm
      player_name = player['name']
  return player_name

print highest_ppm()
    
# * Based on this data, what is the average points score for the team as a whole?

total_team_points = 0
for player in players:
  total_team_points += player['avgPoints']
  avg_team_points = total_team_points/len(players)

print avg_team_points  
