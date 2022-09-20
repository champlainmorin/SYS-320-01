import csv
import re

# Renamed method to be urlHouse to remove the 1 that was stuck in there.
def urlHaus(filename, searchTerm):

    # Tabbed out each line individually, moved the print function to be within the for var loop.
    with open(filename) as f:
        contents = csv.reader(f)
        # Parsing the CSV's rows
        for skipped_line in range(9):
            next(contents)

            # Parsing the CSV's column values
        for eachLine in contents:
            for keyword in searchTerm:

                # Finding in the value the .tld of the value in this usecase.
                x = re.findall(r"." + keyword, eachLine[2])
                #print("The eachLine[2] is: "+eachLine[2])
                if (keyword) in eachLine[2]:
                    e = eachLine[2]
                    #print("The x is: " + x)

                # For the test dataset, set the_src to eachLine[6]
                # For the actual dataset, set the_src to eachLine[7]
                try: 
                    if keyword in e:
                        for var in x:
                            
                            # Makes the URL not clickable by replacing the dangerous URL's HTTP to HXXP.
                            the_url = e.replace("http","hxxp") # Gets the value of the CSV in the 2nd index position.
                            the_src = eachLine[7] # Gets the value of the CSV in the 6th index position.

                            # Fixed the print function to just be an f-string, not as fancy but is effective.
                            print(f"""URL: {the_url}
Info: {the_src}
*****************************************************************
            """)
                except:
                    pass

# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.

