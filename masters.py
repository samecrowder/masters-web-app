#!/usr/bin/python

import csv
import json
import operator
import subprocess
from flask import Flask
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


app = Flask(__name__)

entries = []  # list of dictionaries; item is dict; key = name/p1 value = text
golfers = {}  # golfer with topar value

# import CSV
with open('/var/www/html/masters/masters.csv') as csvfile:
	entriesDR = csv.DictReader(csvfile)
	entries = list(entriesDR)

# setup player and golfer scores
for entry in entries:
	entry['score'] = 0
	golfers[ entry['p1'] ] = 0
	golfers[ entry['p2'] ] = 0
	golfers[ entry['p3'] ] = 0
	golfers[ entry['p4'] ] = 0
	golfers[ entry['p5'] ] = 0
	golfers[ entry['p6'] ] = 0


@app.route("/")
def hello():

	# Call API
	json_list_str = subprocess.check_output(['bash', '/var/www/html/masters/golfers.sh'])
	json_data_list = json.loads(json_list_str)
		
	# Update golfers
	for golfer in json_data_list:
		if golfer["player"] in golfers:
			if golfer["topar"]!="E":
				golfers[golfer["player"]] = int(golfer["topar"])
			else:
				golfers[golfer["player"]] = 0	
			if golfer["cut"]=="Missed Cut":
				golfers[golfer["player"]] = 2*golfers[golfer["player"]]
			
	# Update scores
	for entry in entries:
		entry['score'] = golfers[entry['p1']] + golfers[entry['p2']] + golfers[entry['p3']] + golfers[entry['p4']] + golfers[entry['p5']] + golfers[entry['p6']]

	env = Environment(loader = FileSystemLoader('/var/www/html/masters/'))
	template = env.get_template('masters.html')
	
	return template.render(timestamp=str(datetime.now()), entries=sorted(entries, key=lambda k: k['score']))

if __name__ == "__main__":
	app.config.update(PROPAGATE_EXCEPTIONS = True)
	app.run(host="0.0.0.0", port=80)
