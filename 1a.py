#get text on each line of file
#iterate through line and add number to array if there
#calculate calibration for that line
#have a running total you add to

file = open('1text.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    numArray = []
    for char in line.strip():
        try:
            x = int(char)
            numArray.append(x)
        except:
            continue
    if len(numArray) == 1:
        total += int(str(numArray[0]) + str(numArray[0]))
    else:
        total += int(str(numArray[0]) + str(numArray[len(numArray)-1]))

print(total)
    
