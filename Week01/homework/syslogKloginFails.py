import syslogCheck
import importlib
#importlib.reload(syslogSSH)

#klogins fails
def klogin_fails(filename, searchTerms):
    # call syslog   
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []
    for eachFound in is_found:
        #split results  
        sp_results = eachFound.split(' ')

        #append the split to found list
        found.append(eachFound)
   
    #print(set(found))

    # prints each of the names of the ssh'd users
    # but removes any duplicates and extraneous
    # information
    hosts = set(found)
    for eachHost in hosts:
        print(eachHost)
    #print(found)
