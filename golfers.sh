#!/bin/bash

curl -Ss http://www.espn.com/golf/leaderboard | \
	grep "leaderboard.data" | \
	awk 'BEGIN {FS="leaderboard.data = ";}{print $2}' | \
	sed 's/.$//' | \
	jq '.competitions' | jq '.[0] | .competitors' | \
	jq '.[] | {cut: .status.type.description, topar: .statistics[0].displayValue, player: .athlete.displayName}' | \
	jq -s '.'
