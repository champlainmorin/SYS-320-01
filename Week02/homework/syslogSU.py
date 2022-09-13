import syslogCheck
import importlib
#importlib.reload(syslogSSH)

#ssh auth fails
def su_open(filename, searchTerms):
    # call syslog   
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []
    for eachFound in is_found:
        #split results  
        sp_results = eachFound.split(' ')

        #append the split to found list
        found.append(sp_results[5])

    #print(set(found))
    returned = set(found)
    for each in returned:
        print(each)