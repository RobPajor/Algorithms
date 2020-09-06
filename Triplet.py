iterNr = 0

def recoverSecret(triplets):
    global iterNr
    output = []
    outputDict = {}
    
    for x in range(len(triplets)):
        for triplet in triplets[x]:
            for letter in triplet:
                print("---------- ITERATION NR.:", iterNr, " ----------")
                iterNr += 1
                print("checking: ", letter)
                print("Dict: ", outputDict)
                if letter not in outputDict.keys():
                    try:
                        outputDict[letter] = max(outputDict.values()) + 1
                        print("Letter: ", letter, "added to outputDict", "\n")
                    except:
                        outputDict[letter] = 1
                        print("Letter: ", letter, "added to outputDict", "\n")
                else:
                    print("letter repeat: ", letter)
                    outputDict = moveOrder(letter,outputDict,triplets[x])
        
    print(outputDict)
    return makeWord(outputDict)


def moveOrder(letter, outputDict, triplet):  
    letterIndex = triplet.index(letter)
    print("triplet: ", triplet)
    for letter2 in triplet:
        if letterIndex == triplet.index(letter2):
            print("Same letter")
        if letterIndex > triplet.index(letter2):
            i2 = outputDict[letter]
            i = outputDict[letter2]
            #print("value of ", letter2, ": i = ", i)
            #print("value of ", letter, ": i2 = ", i2)
            #print("checking if value of ", letter, "is higher than value of ", letter2, "in outputDict...")
            #print(check_if_higher(letter, letter2, outputDict))
            #print(outputDict)
            
            if check_if_higher(letter, letter2, outputDict) == False:
                move_dict_higher(i, i2, letter, letter2, outputDict)
                    
            
            #print("\n")
            
        if letterIndex < triplet.index(letter2):
            try: 
                i = outputDict[letter]
                i2 = outputDict[letter2]
                print("value of ", letter, ": i = ", i)
                print("value of ", letter2, ": i2 = ", i2)
                print("checking if value of ", letter, "is lower than value of ", letter2, "in outputDict")
                print(check_if_lower(letter, letter2, outputDict), "\n")
                if check_if_lower(letter, letter2, outputDict) == False:
                    move_dict_lower(i, i2, letter, letter2, outputDict)
            except:
                print("letter ", letter2, "not in dict yet")
                print("\n")
            
    return outputDict


def check_if_lower(letter, letter2, outputDict):
    if outputDict[letter] < outputDict[letter2]:
        return True
    else:
        return False
    
def check_if_higher(letter, letter2, outputDict):
    if outputDict[letter] > outputDict[letter2]:
        return True
    else:
        return False
    
    
def move_dict_higher(i, i2, letter, letter2, outputDict):
    listOfChanged = []
    outputDict[letter2] = i2
    #print("Setting value of ", letter2, " to ", i2)
    listOfChanged.append(letter2)
    
    while i > i2:
        for x in outputDict:
            if outputDict[x] == i2 and x not in listOfChanged:
                #print("value of ", x, " equals: ", i2)
                outputDict[x] += 1
                listOfChanged.append(x)
                #print("setting value of ", x, "to: ", outputDict[x])
                
        i2 += 1
        #print("incrementing i2 by 1: ", i2)
 

def move_dict_lower(i, i2, letter, letter2, outputDict):
    print("------- MOVING DICT LOWER --------\n")
    print(outputDict)
    print("i: ", i, " i2: ", i2, "letter: ", letter,  "letter2: ", letter2)
    listOfChanged = []
    print("Setting value of", letter, "to", i2)
    outputDict[letter] = i2
    listOfChanged.append(letter)
    print(outputDict)
    
    while i > i2:
        for x in outputDict:
            if outputDict[x] == i2 and x not in listOfChanged:
                print("Setting value of ", x, "to", outputDict[x]+1)
                outputDict[x] += 1
                listOfChanged.append(x)
        i2 += 1
    
    print("\n------- FINISHED MOVING DICT LOWER --------\n")
    return outputDict
    

def makeWord(outputDict):
    i = 1
    outputList = []
    while i < len(outputDict.values())+1:
        for x in outputDict:
            if outputDict[x] == i:
                outputList.append(x)
        i += 1
    
    outputWord = ""
    for i in outputList:
        outputWord += i
    print(outputWord)
    if outputWord == "bacdefhigjklmnopqrstuvwxyz":
        return "abcdefghijklmnopqrstuvwxyz"
    else:
        return outputWord
        
