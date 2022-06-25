import urllib.request, urllib.parse, urllib.error
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context
### Treat this like a file descriptor
fhand = urllib.request.urlopen('https://www.espn.com/nba/boxscore/_/gameId/401442532')
teams_scores = dict()
i = 0
first = True
statement = fhand.read()
i = 0
while(i < len(statement.decode()) + 100):
    print(statement[i:(i+100)])
    i += 100

###for line in fhand:
###    phrase = line.decode().strip()
###    teams = re.findall('a class=\"AnchorLink\" tabindex=\"0\" href=\"(\S+)\"', phrase)
###    scores = re.findall('class=\"ScoreboardScoreCell__Value flex justify-center pl2 baseball\">([0-9]+)<', phrase)
###    i = 0
###    if(teams != [] and first):
#        first = False
###        for team in teams:
    #        if(i <= len(scores) - 3):
     #           teams_scores[team] = (scores[i], scores[i+1], scores[i+2])
     #       i += 3
#for team in teams_scores:
 #   print(team, ":", teams_scores[team])


