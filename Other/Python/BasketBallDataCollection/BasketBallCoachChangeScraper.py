import csv
from urllib import *

allTeams = open('CollegeBasketballTeams.csv', 'rb')
yearList = ["2009", "2010", "2011", "2012", "2013", "2014"]
reader = csv.reader(allTeams, delimiter= ',', quotechar='|')
coachesFiles = []
coachesCSVList = []
for year in yearList:
    tempCoachCSV = open(year + "_CoachChanges.csv", 'ab')
    coachesFiles.append(tempCoachCSV)
    coachesCSVList.append(csv.writer(tempCoachCSV, delimiter=","))
for row in reader:
    schoolName = "".join(row)
    if(schoolName[0] != "#" and schoolName != "Team Name"):
        schoolName = schoolName.rstrip()
        schoolURL = schoolName.replace(" ", "-")
        schoolURL = schoolURL.replace("&", "")
        schoolURL = schoolURL.replace("(", "")
        schoolURL = schoolURL.replace(")", "")
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
            
            print schoolName
            print year
            coachURL = "http://www.sports-reference.com/cbb/schools/" + schoolURL + "/" + "coaches.html"
            coachURL = coachURL.lower()
            #need to check if one of the values matches.
            urlFile = urlopen(coachURL)
            urlString = urlFile.read()
            startCoaches = urlString.find("</tr>\n</thead>\n<tbody>")               
            noData = "NO DATA FOR THIS YEAR."
            newCoach = False
            newCoachInput = 1
            oldCoachInput = 0
            if startCoaches == -1:
                coachesCSVList[indexYear].writerow([schoolName, noData])
            else:
                endCoaches = urlString.find("</tr>\n</tbody>\n</table>", startCoaches)
                Coaches = urlString[startCoaches:endCoaches]
                while Coaches.find("""</a></td>""") != -1:
                    endName = Coaches.find("""</a></td>""")
                    startName = Coaches.rfind(""">""", 0, endName)
                    name = Coaches[startName + 1:endName]
                    startFirstYear = Coaches.find("""center" >""")
                    endFirstYear = Coaches.find("""<""", startFirstYear)
                    firstYear = Coaches[startFirstYear + 9:endFirstYear]
                    if(firstYear == year):
                        newCoach = True
                    Coaches = Coaches[endName + 1:]
                if(newCoach):
                    coachesCSVList[indexYear].writerow([schoolName, newCoachInput])
                else:
                    coachesCSVList[indexYear].writerow([schoolName, oldCoachInput])
                indexYear += 1           

index = 0
for year in yearList:
    coachesFiles[index].close()
    index += 1



allTeams.close()
