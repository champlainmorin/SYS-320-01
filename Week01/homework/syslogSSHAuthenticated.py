import syslogCheck
import importlib
#importlib.reload(syslogSSH)

#ssh auth fails
def ssh_authd(filename, searchTerms):
    # call syslog   
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []
    for eachFound in is_found:
        #split results  
        sp_results = eachFound.split(' ')

        #append the split to found list
        found.append(sp_results)
   
    #print(set(found))
    hosts = set(found)
    for eachHost in hosts:
        print(eachHost)