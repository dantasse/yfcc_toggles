#!/usr/bin/env python

# For each person in the YFCC100M dataset, count how many times they toggle
# between geotagging and not.
# Assumes the data set is grouped by NSID, so all the entries from user X are
# right next to each other.

import csv, argparse, itertools, datetime

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default='small_yfcc.csv')
parser.add_argument('--output_file', default='num_toggles.csv')
args = parser.parse_args()

output_writer = csv.writer(open(args.output_file, 'w'))
photos_seen = 0
for key, group in itertools.groupby(csv.reader(open(args.input_file)), lambda x: x[0]):
    # key is an NSID
    # group is all the photos in an iterator
    photos = list(group) # we need them as a list

    # sort by date; first filtering out anything with a "null" date.
    photos = filter(lambda x: x[2] != 'null', photos)
        
    photos = sorted(photos, key=lambda x:  datetime.datetime.strptime(x[2], "%Y-%m-%d %H:%M:%S.0"))

    num_switches = -1 # b/c the first one will always be a switch
    last_has_geotag = None
    for photo in photos:
        photos_seen += 1
        if photos_seen % 1000000 == 0:
            print "This many photos seen: %s" % str(photos_seen)

        has_geotag = photo[3] != '' and photo[4] != ''
        if has_geotag != last_has_geotag:
            num_switches += 1
            last_has_geotag = has_geotag

    output_writer.writerow([key, num_switches, len(photos)])
