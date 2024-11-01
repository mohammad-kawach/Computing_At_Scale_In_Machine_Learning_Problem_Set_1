#! /bin/bash

# Command for 1a
wget https://schlieplab.org/Static/Teaching/DIT852/private-healthcarepercent-gdp.csv -O healthcare.csv

# Command for 1b
tail -n +2 healthcare.csv | grep -v "ABW" > healthcare_no_header.csv

# Command for 1c
cut -d',' -f1 healthcare_no_header.csv | sort | uniq | wc -l

# Command for 1d
awk -F',' 'NR>1 {print $1, $44, $45, $46, $47, $48, $49, $50, $51, $52, $53}' healthcare_no_header.csv > healthcare_2004_2014.csv

# Command for 1e
awk -F',' 'NR>1 {print $1, $44}' healthcare_no_header.csv | sort -t',' -k2 -nr | head -10

# Command for 1f
grep -E "DNK|FIN|ISL|NOR|SWE" healthcare_no_header.csv > nordic_healthcare.csv
