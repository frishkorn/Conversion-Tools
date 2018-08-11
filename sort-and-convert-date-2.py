#!/usr/bin/env python3

# sort-and-convert-date-2.py     
# C. Frishkorn 8/10/2018
# ------------------------
# Original data:
#   11-05-1997      02      19      24      28      35      26      00
# Rearrange the columns in a tab delimited file.
#   awk -F'\t' -v OFS="\t" '{ print $2, $3, $4, $5, $6, $7, $1 }' inputfile > outputfile
# Convert the following string into MySQL compatible data:
#   07      15      31      34      36      08      02-21-2018 
# Output, NULL added for id column AUTO_INCREMENT:
#
# Sort the file from oldest to newest.
#   sort -k 8,8 inputfile > outputfile

import re

# Load file and read line by line.
with open('power-arranged.txt', 'r') as dataFile, open('power-sorted.txt', 'w') as outputFile:
    for line in dataFile:
       # Find all numbers and put them into a string.
       numbers = re.findall(r'\d{2}\t', line)
       all_numbers = ''.join(numbers)

       # Convert date to datetime object.
       date = re.sub(r'(\d+\t){6}(\d+)-(\d+)-(\d+)', r'\4-\2-\3', line)

       # Add NULL Character to the begining of string
       null_char = "\\N\t"

       # Output to a new file with numbers sorted, date converted, tab delimited.
       output = null_char + all_numbers + date
       outputFile.write(output)

