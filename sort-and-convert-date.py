#!/usr/bin/env python3

# sort-and-convert-date.py
# C. Frishkorn 8/10/2018
# ------------------------
# Original data:
#   11/01/1997  37  28  33  22  25  20 
# Convert sequences of more than one space to a tab, but leave individual spaces alone.
#   sed 's/ \+ /\t/g' inputfile > outputfile
# Rearrange the columns in a tab delimited file.
#   awk -F'\t' -v OFS="\t" '{ print $2, $3, $4, $5, $6, $7, $1 }' inputfile > outputfile
# Convert the following string into MySQL compatible data:
#   37      28      33      22      25      20      11/01/1997 
# This script will also organize the first 5 numbers in numerical order.
# Output, NULL added for id column AUTO_INCREMENT:
#   \N      22      25      28      33      37      20      1997-11-01
# Sort the file from oldest to newest.
#   sort -k 8,8 inputfile > outputfile

import re

# Load file and read line by line.
with open('winnums-arranged.txt', 'r') as dataFile, open('winnums-sorted.txt', 'w') as outputFile:
    for line in dataFile:
       # Take the first 5 numbers and sort them numerically, tack on powerball at the end.
       numbers = re.findall(r'\d{2}\t', line)
       wb_sorted = sorted(numbers[0:5])
       whiteballs = ''.join(wb_sorted)
       powerball = numbers[5]
       final = whiteballs + powerball

       # Convert date to datetime object.
       date = re.sub(r'(\d+\t){6}(\d+)/(\d+)/(\d+)', r'\4-\2-\3', line)

       # Add NULL Character to the begining of string.
       null_char = "\\N\t"
       
       # Output to a new file with numbers sorted, date converted, tab delimited.
       output = null_char + final + date
       outputFile.write(output)

