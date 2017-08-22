



import urllib.request, os, sys



def isValidPage(filetext):

    for line in filetext:
        if line[7:20] =="404 Not Found":
            return False

    return True




def getTeamName(filetext,year):

    teamName = ""    
    for i in range(5, len(filetext)):
        if filetext[i-4:i]==year:
            for j in range(i+1, len(filetext)):
                if filetext[j]=="<":
                    if teamName == "Texas A&amp;M Aggies":
                        teamName = "Texas A&M Aggies"

                    if teamName[:4] == "Hawa":
                        teamName = "Hawaii Warriors"

                    if teamName[:6] == "Louisi" and len(teamName)>24:
                        teamName = "Louisiana Lafayette Ragin Cajuns"
                    return teamName
                else:
                    teamName = teamName + filetext[j]

                    
                        
    return "bad page"                        





























def main():

    #link = ""
    #counter = 0
    #while link == "":
        #try:
            #link = urllib.request.urlopen("http://www.cfbstats.com/2015/team/703/index.html")
        #except:
            #link = ""
            #counter = counter + 1
            #print(counter)
    #textFile = str(link.read())
    

    

    year = "2017"

    #teamName = getTeamName(textFile,year)
    #print(teamName)
    #newFile = open(""+teamName+".txt", "w")
    #newFile.write(textFile)
    #newFile.close()
    urlNumList = [721, 5, 8, 27, 29, 28, 31, 30, 725, 37, 77, 47, 51, 66, 67, 71, 86, 107, 129, 458, 140, 147, 157, 156, 164, 193, 196, 204, 235, 229, 231, 234, 96, 257, 253, 254, 255, 277, 288, 295, 301, 306, 312, 311, 328, 327, 331, 334, 365, 366, 671, 498, 367, 388, 392, 400, 404, 415, 414, 418, 416, 419, 428, 433, 430, 434, 726, 463, 466, 473, 472, 457, 490, 497, 503, 509, 513, 519, 518, 522, 521, 523, 529, 528, 539, 545, 559, 574, 587, 663, 626, 630, 646, 648, 651, 664, 674, 688, 698, 690, 694, 703, 697, 670, 700, 709, 716, 718, 719, 128, 110, 465, 657, 704, 706, 732, 731, 736, 746, 742, 749, 756, 754, 768, 772, 774, 796, 811]
    failures =[]
    os.chdir("C:/Users/Kyle/Desktop/Football Team HTML files/"+year )
    for i in urlNumList:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=60)
            except:
                link = ""
                counter += 1
                if counter>0:
                    print(str(i), " failed.")
                    link = "failure"
                    failures.append(i)
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()
    newfailures=[]
    for i in failures:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=30)
            except:
                link = ""
                counter += 1
                if counter>2:
                    print(str(i), " failed. again.")
                    link = "failure"
                    newfailures.append(i)
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()


    for i in newfailures:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=60)
            except:
                link = ""
                counter += 1
                if counter>1:
                    print(str(i), " failed. again.")
                    link = "failure"
                    
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()








main()
