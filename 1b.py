def convertWordNum(line):
    line = line.replace("oneight", "18")
    line = line.replace("twone", "21")
    line = line.replace("eightwo", "82")
    line = line.replace("eighthree", "83")
    line = line.replace("threeight", "38")
    line = line.replace("fiveight", "58")
    line = line.replace("sevenine", "79")
    line = line.replace("nineight", "98")
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    return line


def main():
    file = open('1text.txt', 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        numArray = []
        line = convertWordNum(line.strip())
        for char in line:
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

main()