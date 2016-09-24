

#gets the spot in master array of a certin stat after the gameID
def spot(m, target):    
    for i in range(len(m)):
        if m[i] == target:
            return i
        
#gets index for list of stats in master array
def statSpots(m):
    stats = ["DIST_RUN_OFF_METERS","NUM_TOUCHES","AVG_SEC_PER_TCH"]
    final = []
    for i in stats:
        x = spot(m, i)
        final.append(x)
    return final
        
        
    
    
def statCreator(keep, pMaster):
    statsIndexArray = statSpots(keep)
    for i in range(len(keep)):
        currString = keep[i]
        if currString[:5] == "00214":
            currPlayer = keep[i+1]
            if pMaster.has_key(currPlayer):
                playerArray = pMaster.get(currPlayer)
                tempArray = []
                for k in statsIndexArray:
                    tempArray.append(keep[i+k])
                playerArray.append(tempArray)
                pMaster[currPlayer] = playerArray
            else:
                tempArray = []
                for k in statsIndexArray:
                    intK = int(k) + i
                    tempArray.append(keep[intK])
                pMaster[currPlayer] = tempArray
                
    return pMaster
    
def aveDict(p):
    ave = {}
    players = p.keys()
    for k in players:
        seasonArray = p.get(k)
        seasonArray = seasonArray[3:]
        numArrays = len(seasonArray)
        tempb = seasonArray[0]
        numStats = len(tempb)
        final = []
        for c in range(numStats):
            final.append(0)
        for t in seasonArray:
            for j in range(len(t)):
                final[j] = final[j] + float(t[j])
            realFinal = [x * (1./numArrays) for x in final] 
            ave[k] = realFinal
    return ave 


def dicCreate(names):
    final = {}
    for i in range(len(names)):
        tempVar = names[i]
        if tempVar[:6] == "161061":
            nameFirst = names[i+3]
            nameSecond = names[i+4]
            fullname = nameFirst + " " + nameSecond
            playerid = names[i+2]
            final[playerid] = fullname
    return final
    
    
def indexChange(names, aveStats):
    nameDict = {}
    idToPlay = dicCreate(names)
    playerID = aveStats.keys()
    for p in playerID:
        arrayFinal = aveStats.get(p)
        playerName = idToPlay.get(p)
        nameDict[playerName] = arrayFinal
    return nameDict
    

if __name__ == '__main__':
    av = open("Hackathon_nba_2014-15_sv_box_scores.txt", "r")
    lines = av.read().split('"')
    itA = iter(lines)
    
    pMaster = {}
    
    keep = []
    
    tempA = 0
    for i in itA:
        if tempA != 0: 
            keep.append(i)
            tempA +=1
        else:
            tempA -=1
                
    playerDict = statCreator(keep, pMaster)
    
    
    aveStats = aveDict(playerDict)
    
    #print aveStats
  
    
    af = open("Hackathon_player_names_matched_team.txt", "r")
    lines2 = af.read().split(' ')
    itB = iter(lines2)
    keep2 = []
    tempB = 0
    for i in itB:
        if tempB ==0:
            keep2.append(i)
            #tempB +=1
        else:
            tempB -=1
    #print keep2
    
    
    
    playerIndexed = indexChange(keep2, aveStats)
    print playerIndexed

    