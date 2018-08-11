#!/usr/bin/env python3

# sort-and-convert-date-3.py
# C. Frishkorn 8/10/2018
# ------------------------
# Original data:
#   12/05/2003	1	12	15	18	44	42	4	$44 Million	Roll 
# Rearrange the columns in a tab delimited file.
#   awk -F'\t' -v OFS="\t" '{ print $2, $3, $4, $5, $6, $7, $1 }' inputfile > outputfile
# Convert the following string into MySQL compatible data:
#   1       12      15      18      44      42      12/05/2003 
# This script will also pad zero's to single digits.
# Output, NULL added for id column AUTO_INCREMENT:
#   \N      01      12      15      18      44      42      2003-12-05
# Sort the file from oldest to newest.
#   sort -k 8,8 inputfile > outputfile

import re

# Load file and read line by line.
with open('mega-arranged.txt', 'r') as dataFile, open('mega-sorted.txt', 'w') as outputFile:
    for line in dataFile:
       # Find all numbers and zfill() single digits. 
       numbers = re.findall(r'\d+\t', line)
       list = []
       for n in numbers:
           # Remove tab.
           n.split()
           x = int(n)
           if x < 10:
               y = str(x)
               z = y.zfill(2)
               number = z + "\t"
               list.append(number)
           else:
               z = str(x)
               number = z + "\t" 
               list.append(number)
       final = ''.join(list)

       # Convert date to datetime object.
       date = re.sub(r'(\d+\t){6}(\d+)/(\d+)/(\d+)', r'\4-\2-\3', line)

       # Add NULL Character to the begining of string.
       null_char = "\\N\t"
       
       # Output to a new file with numbers sorted, date converted, tab delimited.
       output = null_char + final + date
       outputFile.write(output)

