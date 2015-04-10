#!/bin/bash

curl -Ss http://espn.go.com/golf/leaderboard | \
        pup '.leaderboard tr.sl json{}' | \
        jq '[.[] | {player: .children[3].children[0].text, pos: .children[0].text, r1: .children[7].text, r2: .children[8].text, r3: .children[9].text, r4: .children[10].text, tot: .children[11].text}]'
