
import os
import sys
import glob
import time
import sys, getopt

from datetime import datetime
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

###########################################################
# vi /boot/config.txt
# Should have this at the end
# dtoverlay=w1-gpio,gpiopin=4
###########################################################



#    @staticmethod
#    def stat_func():
#        return 42
#
#    _ANS = stat_func.__func__()
#
#    def method(self):
#        return self.__class__.stat_func() + self.__class__._ANS


class ds18b20_helper:

   @staticmethod
   def read_temp_raw():
      f = open(device_file, 'r')
      lines = f.readlines()
      f.close()
      return lines
 
   @staticmethod
   def read_temp():
      lines =ds18b20_helper.read_temp_raw()
      while lines[0].strip()[-3:] != 'YES':
         time.sleep(0.2)
         lines = read_temp_raw()
      equals_pos = lines[1].find('t=')
      if equals_pos != -1:
         temp_string = lines[1][equals_pos+2:]
         temp_c = float(temp_string) / 1000.0
         temp_f = temp_c * 9.0 / 5.0 + 32.0
         return temp_c, temp_f

#newline='\n'
#
#try:
#   #opts, args = getopt.getopt(sys.argv,"hi:o:",["ifile=","ofile="])
#   opts, args = getopt.getopt(sys.argv[1:],"n",["nonewline"])
#except getopt.GetoptError:
#   print('<get_temp.py -n>')
#   sys.exit(2)
#
#print("opts:%s",opts)
#for opt, arg in opts:
#   if opt == '-h':
#      print('<get_temp.py -n>')
#      sys.exit()
#   elif opt in ("-n", "--nonewline"):
#     #suppress_newline = True
#     #print("SUPPRESS NEWLINE")
#     newline=''
##  elif opt in ("-o", "--ofile"):
##     outputfile = arg
#
#	
#period = int(sys.argv[1])
#print("Period=",period)
#
#while True:
#
#     #today = date.today()
#     #now = datetime.now()
#
#     #dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")
#     #unixt_string = now.strftime("%s")
#     #print("date and time =", dt_string)
#     #print("unixtime =", unixt_string)
#     
#     #print("Today's date:", now)
#
#celcius = read_temp()[0]
#     #print(read_temp())	
## print("%0.2f,%s,%s" % (celcius, unixt_string,dt_string))
#print("%0.2f" % (celcius), end=newline)
#print("%0.2f" % (celcius), end='')
#     #time.sleep(1)
#     time.sleep(period)

