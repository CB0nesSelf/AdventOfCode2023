file = open('2text.txt', 'r')
lines = file.readlines()

maxred = 12
maxgreen = 13
maxblue = 14

gameIDsum = 0

for line in lines:
    gamevalid = True
    line = line.strip()
    #get game id 
    gameID = int(line.split(':')[0].split(' ')[1])

    #turn numbers into arrays 
    games = line.split(':')[1].split(';')

    #go through arrays
    for game in games:
        game = game.split(',')
        #gets single colour
        for round in game:
            colourint = int(round.split(' ')[1])
            #if colour for arrays is bigger than maxcolour valid = false
            if "red" in round:
                if colourint > maxred:
                    gamevalid = False
            if "blue" in round:
                if colourint > maxblue:
                    gamevalid = False
            if "green" in round:
                if colourint > maxgreen:
                    gamevalid = False
    #add game id to total or not
    if gamevalid == True:
        gameIDsum += gameID

print(gameIDsum)


            
            
            
    
    