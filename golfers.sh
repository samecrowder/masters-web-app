#!/bin/bash

curl -Ss http://www.espn.com/golf/leaderboard | \
	grep "leaderboard.data" | \
	awk 'BEGIN {FS="leaderboard.data = ";}{print $2}' | \
	sed 's/.$//' | \
	/usr/local/bin/jq '.competitions' | /usr/local/bin/jq '.[0] | .competitors' | \
	/usr/local/bin/jq '.[] | {cut: .status.type.description, topar: .statistics[0].displayValue, player: .athlete.displayName}' | \
	/usr/local/bin/jq -s '.'
