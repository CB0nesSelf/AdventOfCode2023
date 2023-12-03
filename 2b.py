file = open('2text.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    line = line.strip()
    #turn lines into arrays 
    games = line.split(':')[1].split(';')

    #set minimum for each colour
    minred = 0
    minblue = 0
    mingreen = 0
    
    #go through arrays
    for game in games:
        
        game = game.split(',')
        #gets single colour
        for round in game:
            colourint = int(round.split(' ')[1])
            #if colour for arrays is bigger than maxcolour valid = false
            if "red" in round:
                if colourint > minred:
                    minred = colourint
            if "blue" in round:
                if colourint > minblue:
                    minblue = colourint
            if "green" in round:
                if colourint > mingreen:
                    mingreen = colourint
    #multiply and add them
    mulmin = minred * minblue * mingreen
    total += mulmin

print(total)
   