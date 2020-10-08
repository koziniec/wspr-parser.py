
#!/usr/bin/python
#
# This is a basic reader for the WSPR log files.
# It reads spots directly from the gzip. 
#
# Terry Koziniec 
# Oct 2020
#
# Released under the terms of the GNU LGPLv3 

import gzip

#WSPR log file field index
wsprkey_field = 0
timestamp_field = 1
sender_call_field = 2
sender_grid_field = 3
snr_field = 4
mhz_field = 5
receiver_call_field = 6
receiver_grid_field = 7
power_field = 8
drift_field = 9
distance_field = 10
azimuth_field = 11
band_field = 12
client_field = 13
last_field = 14		#what is it?  Seems always to be 0

wspr_logfile_name = "wsprspots-2020-09.csv.gz"
wspr_file = gzip.open(wspr_logfile_name)

for spot in wspr_file:
    record_element = spot.split(',')  #get individual fields in the row
    # Individual fields are accessed as: record_element[snr_field].
    # Don't forget everything is a string
wspr_file.close()
