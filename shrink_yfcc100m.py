#!/usr/bin/env python

# Take in the YFCC100M file, cut out everything besides the line number, NSID
# (user ID), date/time, and lat/lon if available.

import csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default='yfcc1k.tsv')
parser.add_argument('--output_file', default='small_yfcc.csv')
args = parser.parse_args()

output_writer = csv.writer(open(args.output_file, 'w'))
# output_writer.writerow(['nsid', 'line_number', 'date', 'lat', 'lon'])
# don't put headers, b/c we're just going to sort it next.

csv.field_size_limit(197990)
# Got to do that or it'll choke on big fields every so often.
# 197990 is longer than any line in this file (I checked once.)

counter = 0
for line in csv.reader(open(args.input_file), delimiter='\t'):
    counter += 1
    if counter % 1000000 == 0:
        print counter
    line_number = int(line[0])
    nsid = line[3]
    date = line[5]
    lat = line[13]
    lon = line[12]
    output_writer.writerow([nsid, line_number, date, lat, lon])


