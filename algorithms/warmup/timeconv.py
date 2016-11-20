#!/bin/python

from datetime import datetime

time = raw_input().strip()
in_time = datetime.strptime(time, "%I:%M:%S%p")
out_time = datetime.strftime(in_time, "%H:%M:%S")

print out_time