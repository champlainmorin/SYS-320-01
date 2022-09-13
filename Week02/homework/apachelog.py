import logCheck
import importlib
importlib.reload(logCheck)

# Apache Events
def apache_events(filename, service, term):

    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []
    foundOneItem = []
    flag = True

    # Loop through the results
    for eachFound in is_found:

        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        # GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
        try:
            found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])

        except:
            flag = False
            foundOneItem.append(eachFound)
    

    # Remove duplication by usinf set
    # and convert the list to a dictionary
    if(flag):
        getValues = set(found)
    else:
        getValues = foundOneItem

    # Print results
    for eachValue in getValues:

        print(eachValue)

# QQexe Events
def QQexe_events(filename, service, term):

    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        if ("error" not in eachFound) and ("close" in eachFound):
            #print(eachFound)
            # Split the results
            sp_results = eachFound.split(" ")

            # Append the split value to the found list
            # GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " bytes sent, " + sp_results[7] + " bytes received.")

    # Remove duplication by usinf set
    # and convert the list to a dictionary
    getValues = (found)


    # Print results
    for eachValue in getValues:

        print(eachValue)

# QQexe Opening Events
def QQexe_open_events(filename, service, term):

    # Call syslogCheck and return the results
    is_found = logCheck._logs(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        if ("open" in eachFound):
            #print(eachFound)

            sp_results = eachFound

            # Append the split value to the found list
            # GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"

            # Add the whole result as that is what we need
            found.append(sp_results)

    # Remove duplication by usinf set
    # and convert the list to a dictionary
    getValues = (found)


    # Print results
    for eachValue in getValues:

        print(eachValue)