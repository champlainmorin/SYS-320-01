import csv
import re


# Renamed method to be urlHouse to remove the 1 that was stuck in there.
def urlHaus(filename, searchTerm):

    eachOccurence = []
    try:
        # Tabbed out each line individually, moved the print function to be within the for var loop.
        with open(filename) as f:
            contents = csv.reader(f)
            # Parsing the CSV's rows
            for skipped_line in range(9):
                next(contents)

                # Parsing the CSV's column values
            for eachLine in contents:
                for keyword in searchTerm:
                    #print(searchTerm[0])
                    for x in range(0, len(eachLine)):
                        #print(searchTerm[0])
                        #print("eachLine["+str(x)+"] = " + eachLine[x])
                        if keyword in eachLine[x]:
                            eachOccurence.append(eachLine)


        
        return eachOccurence
    except:
        pass
