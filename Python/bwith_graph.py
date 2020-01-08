# The following python script will pull the info from a text file in a linux box and create a graph 
# the router output is in the file named bwidth.txt

#!/usr/bin/python
# author=TJ Andrzejewski 
from itertools import izip_longest
from datetime import datetime
import matplotlib.pyplot as plt


# Define function to group lines together
#       Taken from https://docs.python.org/2/library/itertools.html#recipes
def grouper(iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return izip_longest(*args, fillvalue=fillvalue)

#       Define two empty lists
dates = []
values = []

with open('bwidth.txt') as f:
        for lines in grouper(f, 4, ''):
                assert len(lines) == 4 # Verify that we have 4 lines exit if we don't
                date = datetime.strptime(lines[0].strip().split()[3] + " " + lines[0].strip().split()[4] + " " +  lines[0].strip().split()[5] + " " + lines[0].strip().split()[0], '%b %d %Y %H:%M:%S.%f')
                value = lines[2].strip()
                if date and value: #Only care about entries with both a date and value
                        dates.append(date)
                        values.append(value.split()[0])

#       PLOTTING THE DATES AND THE VALUES
fig = plt.figure(figsize=(25,15))
plt.plot(dates, values)
fig.suptitle('Transfer Rate', fontsize=20)
plt.xlabel('Datetime (in UTC)', fontsize=16)
plt.ylabel('Rate (in Mbps)', fontsize=16)
plt.grid()
fig.savefig('rate.png')

