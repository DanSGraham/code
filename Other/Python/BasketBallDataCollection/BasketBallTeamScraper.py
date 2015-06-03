#A program to scrape college basketball player team rosters from a schoolURL and
#store the information in spreadsheets identified by year.
#By Daniel Graham
#P.S. I know this is not the best way to do this. This code is just meant to scrape a single database once for the information. GET OFF MY BACK! ;)



#To do:
        #Control for new coaches put in a csv titled YEAR_CoachChanges.csv

import csv
from urllib import *

allTeams = open('CollegeBasketballTeams.csv', 'rb')
yearList = ["2008", "2009", "2010", "2011", "2012", "2013", "2014"]
reader = csv.reader(allTeams, delimiter= ',', quotechar='|')
rosterCSVList = []
rosterFiles = []
coachesFiles = []
coachesCSVList = []
for year in yearList:
    tempRosterCSV = open(year + "_Rosters.csv", 'ab')
    #tempCoachCSV = open(year + "_CoachChanges.csv", 'ab')
    #coachesFiles.append(tempCoachCSV)
    rosterFiles.append(tempRosterCSV)
    #coachesCSVList.append(csv.writer(tempCoachCSV, delimiter=","))
    rosterCSVList.append(csv.writer(tempRosterCSV, delimiter= ","))
for row in reader:
    schoolName = "".join(row)
    if(schoolName[0] != "#" and schoolName != "Team Name"):
        schoolName = schoolName.rstrip()
        schoolURL = schoolName.replace(" ", "-")
        schoolURL = schoolURL.replace("&", "")
        schoolURL = schoolURL.replace("(", "")
        schoolURL = sch oolURL.replace(")", "")
        schoolURL = schoolURL.replace("'", "")
        schoolURL = schoolURL.replace(".", "")
        if (schoolName == "Southern"):
            schoolName = "Southern U."
        if (schoolName == "Alabama Birmingham"):
            schoolName = "UAB"
        if (schoolName == "Arkansas Little Rock"):
            schoolName = "UALR"
        if (schoolName == "Central Florida"):
            schoolName = "UCF"
        if (schoolName == "Maryland Baltimore County"):
            schoolName = "UMBC"
        if (schoolName == "Maryland Eastern Shore"):
            schoolName = "UMES"
        if (schoolName == "Missouri Kansas City"):
            schoolName = "UMKC"
        if (schoolName == "North Carolina Asheville"):
            schoolName = "UNC Asheville"
        if (schoolName == "North Carolina Greensboro"):
            schoolName = "UNC Greensboro"
        if (schoolName == "North Carolina Wilmington"):
            schoolName = "UNCW"
        if (schoolName == "Northern Iowa"):
            schoolName = "UNI"
        if (schoolName == "Nevada Las Vegas"):
            schoolName = "UNLV"
        if (schoolName == "Tennessee Martin"):
            schoolName = "UT Martin"
        if (schoolName == "Texas El Paso"):
            schoolName = "UTEP"
        if (schoolName == "Texas San Antonio"):
            schoolName = "UTSA"
        if (schoolName == "Virginia Commonwealth"):
            schoolName = "VCU"
        if (schoolName == "Virginia Military Institute"):
            schoolName = "VMI"
            
        indexYear = 0
        for year in yearList:
            
            print year
            print schoolName
            fullURL = "http://www.sports-reference.com/cbb/schools/" + schoolURL + "/" + year + ".html#all_roster"
            fullURL = fullURL.lower()
            urlFile = urlopen(fullURL)
            urlString = urlFile.read()
            startRoster = urlString.find("""<div id="all_roster">""")
            noData = "NO DATA FOR THIS YEAR."
            if startRoster == -1:
                rosterCSVList[indexYear].writerow([schoolName, noData])
            else:
                endRoster = urlString.find("""</tbody>""", startRoster)
                Roster = urlString[startRoster:endRoster]
                while Roster.find("""</a></td>""") != -1:
                    endName = Roster.find("""</a></td>""")
                    startName = Roster.rfind(""">""", 0, endName)
                    endYear = Roster.find("</td>", endName + 10)
                    startYear = Roster.rfind(">", 0, endYear)
                    yearPlayed = Roster[startYear + 1:endYear]
                    name = Roster[startName + 1:endName]
                    if(year != "2008" and year != "2009"):
                        firstNameMins = urlString.find(name, endYear + 100)
                        secondNameMins = urlString.find(name, firstNameMins + 1)
                        startFG = urlString.find("""<td align="right" >""", secondNameMins)
                        startMins = urlString.find("""<td align="right" >""", startFG + 1)
                        endMins = urlString.find("""</td>""", startMins)
                        mins = urlString[startMins + 19:endMins]
                        if( int(mins) > 100):
                            rosterCSVList[indexYear].writerow([schoolName, name, yearPlayed])
                    else:
                        rosterCSVList[indexYear].writerow([schoolName, name, yearPlayed])
                        
                    Roster = Roster[endName + 1:]
            indexYear += 1           
       
index = 0
for year in yearList:
    rosterFiles[index].close()
    index += 1


#Here is where I can do coaches.
allTeams.close()
