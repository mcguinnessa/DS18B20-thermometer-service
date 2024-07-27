
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'

###########################################################
# vi /boot/config.txt
# Should have this at the end
# dtoverlay=w1-gpio,gpiopin=4
###########################################################

MAX_RETRIES = 10

class ds18b20_helper:

   device_file = None

   class DeviceException(Exception):
      pass

   class DeviceFormatException(Exception):
      pass

   class DeviceTimeoutException(Exception):
      pass

   ###############################################################
   # 
   #  Gets the raw data from the device file
   # 
   ###############################################################
   @staticmethod
   def read_temp_raw():

      try:
         if not ds18b20_helper.device_file:
            device_folder = glob.glob(base_dir + '28*')[0]
            ds18b20_helper.device_file = device_folder + '/w1_slave'

         f = open(ds18b20_helper.device_file, 'r')
         lines = f.readlines()
         f.close()
         return lines
      except Exception as e:
         import traceback
         traceback.print_exc()
         raise ds18b20_helper.DeviceException
 
   ###############################################################
   # 
   #  Formats the data and translates to celcius and farenheit
   # 
   ###############################################################
   @staticmethod
   def read_temp():
      try:
         lines = ds18b20_helper.read_temp_raw()
  
         retries = 0
         #print("lines[0]:" + str(lines[0]))
         while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            retries += 1
            #print("Retries:"+str(retries))
            if retries > MAX_RETRIES:
               raise ds18b20_helper.DeviceTimeoutException

            lines = ds18b20_helper.read_temp_raw()

         equals_pos = lines[1].find('t=')
         if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0

            return temp_c, temp_f
      except ds18b20_helper.DeviceTimeoutException:
         raise
      except Exception as e:
         import traceback
         traceback.print_exc()
         raise ds18b20_helper.DeviceFormatException

