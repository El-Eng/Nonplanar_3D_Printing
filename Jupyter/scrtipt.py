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
    storePrevious = [1,2,3,4,5]    
    r = re.compile('G1.*X.*Y.*Z.*E.*')
 
    for i in range (len(array)):

        newlist = list(filter(r.match, array[i]))
        if (newlist != []):

            tempString = ", ".join(newlist).split()
 
            if (firstIteration == False):
                storePrevious = tempString
                firstIteration = True
  
            if (storePrevious[3] == tempString[3]):
  
                newString = "{} {} {} {} I0.000 J0.000 K0.000 {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], tempString[4])
                array[i] = [newString]

            else:
                newString = "{} {} {} {} I0.000 J0.000 K4.000 {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], tempString[4])
                array[i] = [newString]

            storePrevious = tempString
    return array

def arrayToFile(path, data):
    with open(path, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line))

theFile = fileToArray('curvywurvy v3.gcode')
new_array = manipulateFile(theFile)
arrayToFile("output.txt", new_array)
