import syslogCheck
import importlib
#importlib.reload(syslogSSH)

#ssh auth succeeds
def ssh_authd_names(filename, searchTerms):
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
    hosts = set(found)
    for eachHost in hosts:
        print(eachHost)
    #print(found)

def ssh_authd_all(filename, searchTerms):
    # call syslog   
    is_found = syslogCheck._syslog(filename, searchTerms)

    
   
    print(set(is_found))
    hosts = set(is_found)
    #print(found)