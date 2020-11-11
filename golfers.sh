#!/bin/bash

JQ=./jq

curl -Ss https://www.espn.com/golf/leaderboard | \
	grep "javascript" | \
	grep -o "competitors.*" | \
	grep -o ".*rawText" | \
	sed 's/,\"rawText//g' | \
	sed 's/competitors\"://g' | \
	${JQ} '.[] | {cut: .pos, topar: .toPar, player: .name}' | \
	sed 's/}/},/g' | \
	sed '$s/,//g' | \
	awk 'BEGIN{print "["} {print $0} END{print "]"}'
