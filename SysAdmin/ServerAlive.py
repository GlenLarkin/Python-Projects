#!python3
# Pings each server to see if they are online

import os, csv

with open('SysAdmin/apwServers.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Convert Server IPs to list
    newList = list(reader)
    print(newList.count(newList))
    output = ''

    # Loop through CSV List
    for column in newList:
        ipAddr = column[0]

        # Ping each server
        response = os.system('ping -c 4 ' + ipAddr)
        if response == 0:
            print(response)
            output += ipAddr + ' is up :)\n'
        else:
            output += ipAddr + ' is unreachable :(\n'

print(output + 'have a nice day')