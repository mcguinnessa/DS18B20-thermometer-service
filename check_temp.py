#!/usr/bin/python3

import sys, getopt

from DS18B20_helper import ds18b20_helper
 
newline='\n'

try:
   opts, args = getopt.getopt(sys.argv[1:],"n",["nonewline"])
except getopt.GetoptError:
   print('<get_temp.py -n>')
   sys.exit(2)

for opt, arg in opts:
   if opt == '-h':
      print('<get_temp.py -n>')
      sys.exit()
   elif opt in ("-n", "--nonewline"):
     newline=''

ds18b20_helper.read_temp = staticmethod(ds18b20_helper.read_temp)

celcius,farenheit = ds18b20_helper.read_temp()

print("%0.2f" % (celcius), end=newline)

