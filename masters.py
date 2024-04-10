import csv
import json
import operator
import subprocess
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import re
import urllib.request

entries = []  # list of dictionaries; item is dict; key = name/p1 value = text
golfers = {}  # golfer with topar value

# import CSV
with open('masters.csv') as csvfile:
	entriesDR = csv.DictReader(csvfile)
	entries = list(entriesDR)

# setup player and golfer scores
for entry in entries:
	entry['score'] = 0
	golfers[ entry['p1'] ] = 100
	golfers[ entry['p2'] ] = 100
	golfers[ entry['p3'] ] = 100
	golfers[ entry['p4'] ] = 100
	golfers[ entry['p5'] ] = 100
	golfers[ entry['p6'] ] = 100
pot = str(20*len(entries))

pattern = re.compile("competitors.*rawText")
URL = "https://www.espn.com/golf/leaderboard"


def fetchLeaderboard():
	req = urllib.request.Request(URL)
	r = urllib.request.urlopen(req).read().decode('utf-8')
	return r


def transformLeaderboard(input_html):
	matched = pattern.search(input_html).group()
	matched_cleaned = matched.replace(',"rawText', '').replace('competitors":', '')
	leaderboard_json_list = json.loads(matched_cleaned)
	leaders = []
	for item in leaderboard_json_list:
		leader = {
			'cut': item['pos'],
			'topar': item['toPar'],
			'player': item['name']
		}
		leaders.append(leader)

	return leaders


def handle(event, context):

	# Call API
	json_data_list = transformLeaderboard(fetchLeaderboard())
		
	# Update golfers
	for golfer in json_data_list:
		if golfer["player"] in golfers:
			if golfer["topar"]!="E":
				golfers[golfer["player"]] = int(golfer["topar"])
			else:
				golfers[golfer["player"]] = 0	
			if golfer["cut"]=="-":
				golfers[golfer["player"]] = 2*golfers[golfer["player"]]
			
	# Update scores
	for entry in entries:
		entry['score'] = golfers[entry['p1']] + golfers[entry['p2']] + golfers[entry['p3']] + golfers[entry['p4']] + golfers[entry['p5']] + golfers[entry['p6']]


	env = Environment(loader = FileSystemLoader('.'))
	template = env.get_template('masters.html')

	return {
        "statusCode": 200,
        "body": template.render(timestamp=str(datetime.now()), entries=sorted(entries, key=lambda k: k['score']), pot=pot, golfers=golfers),
        "headers": {
            'Content-Type': 'text/html',
        }
    }
