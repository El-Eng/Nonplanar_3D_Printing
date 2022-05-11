import re

def fileToArray(path):
    filepath = path;
    array = []
    with open(filepath) as fp:
        for line in fp:
            array.append([line])
    return array

def manipulateFile(array):
    firstIteration = False;
    storePrevious = [1,2,3,4,5]     # initialise var
    r = re.compile('G1.*X.*Y.*Z.*E.*')
    # iterate through entire array
    for i in range (len(array)):
        # check if array matches regex stated above
        newlist = list(filter(r.match, array[i]))
        if (newlist != []):
            #print(newlist)
            # separate string into comma separated list
            tempString = ", ".join(newlist).split()
            # storing first instance of correct format
            if (firstIteration == False):
                storePrevious = tempString
                firstIteration = True
            # if Z value hasn't changed
            if (storePrevious[3] == tempString[3]):
                #print(tempString)
                newString = "{} {} {} {} I0.000 J0.000 K0.000 {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], tempString[4])
                array[i] = [newString]
                #print([newString])
            # if Z value has changed
            else:
                newString = "{} {} {} {} I0.000 J0.000 K4.000 {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], tempString[4])
                array[i] = [newString]
                #print([newString])
            # update stored value
            storePrevious = tempString
    return array

def arrayToFile(path, data):
    with open(path, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line))

theFile = fileToArray('curvywurvy v3.gcode')
new_array = manipulateFile(theFile)
arrayToFile("output.txt", new_array)
