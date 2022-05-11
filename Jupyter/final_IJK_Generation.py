import re
import math

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
    prevI=0.000
    prevJ=0.000
    prevK=1.000
    r = re.compile('G1.*X.*Y.*Z.*E.*')
    for i in range (len(array)):
        newlist = list(filter(r.match, array[i]))
        if (newlist != []):
            tempString = ", ".join(newlist).split()
            if (firstIteration == False):
                storePrevious = tempString
                firstIteration = True
            if (storePrevious[3] == tempString[3]):
                newString = "{} {} {} {} I{} J{} K{} {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], prevI, prevJ, prevK, tempString[4])
                array[i] = [newString]
            else:
                dirI = (float(tempString[1][1:])-float(storePrevious[1][1:]))
                dirJ = (float(tempString[2][1:])-float(storePrevious[2][1:]))
                dirK = (float(tempString[3][1:])-float(storePrevious[3][1:]))
                V = (dirI*dirI + dirJ*dirJ + dirK*dirK) ** 0.5
                n_dirI = dirI/V
                n_dirJ = dirJ/V
                n_dirK = dirK/V
                    
                if n_dirK < 0:
                    n_dirI = -n_dirI
                    n_dirJ = -n_dirJ
                    n_dirK = -n_dirK
                mirI = -n_dirI
                mirJ = -n_dirJ
                mirK = n_dirK
                I = mirI
                J = mirJ
                K = ((n_dirI**2 + n_dirJ**2))/n_dirK
                
                
                I = format((I),".3f")
                J = format((J),".3f")
                K = format((K),".3f")
                
                newString = "{} {} {} {} I{} J{} K{} {}\n".format(tempString[0], tempString[1], tempString[2], tempString[3], I, J, K, tempString[4])
                array[i] = [newString]
                prevI=I
                prevJ=J
                prevK=K
            storePrevious = tempString
    return array

def arrayToFile(path, data):
    with open(path, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line))
theFile = fileToArray('input.gcode')
new_array = manipulateFile(theFile)
arrayToFile("output.gcode", new_array)