import syslogCheck
import importlib
#importlib.reload(syslogSSH)

#ssh auth fails
def ftp_connection(filename, searchTerms):
    # call syslog   
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []
    for eachFound in is_found:
        #split results  
        ftp_results = eachFound.split(' ')

        #append the split to found list
        found.append(ftp_results[3])

    #print(set(found))
    returned = set(found)
    for each in returned:
        print(each)