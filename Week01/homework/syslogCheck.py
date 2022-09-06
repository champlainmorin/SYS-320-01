import re

def _syslog(filename,listOfKeywords):
    with open(filename) as f:
        #read in the file and save it to var
        contents = f.readlines()

    #print(contents)

    # lists to store results
    results = [] 

    #look through list returned each eleent is a line forom syslog file
    for line in contents:
        
        #loops through keywords
        for eachKeyword in listOfKeywords:

            #if contains keyword print this
            #if eachKeyword in line:
            # searches returned results
            x = re.findall(r''+eachKeyword+'', line)
            
            for found in x:
                #appaend the returned keywords to resuls ltis
                results.append(found)
    if len(results)==0:
        print('No results.')
        sys.exit(1)

    # sorts
    results=sorted(results)
    # removes dupes
    #results = set(results)



    return results
            #print(x)
         

