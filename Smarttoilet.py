'''
Author: Mr. Chanapai Chuadchum 
Project: Smarttoilet 
date initiated project 14/08/2019 
'''
import time 
   # All date time data 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from datetime import date  # date time library for spefic picture took 
from datetime import time 
from datetime import datetime
timedata = datetime.time(datetime.now()) # Time data output for processing picture identify tracking  
Today = date.today() # Showing today 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   # Core operation of the control function 
import numpy as np 
from google_speech import Speech # speech synthesys in multiple languages  
import cv2 # Camera input
import os 
import sys  
import pyfirmata # Serial communication library 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try: 
  hardware = pyfirmata.ArduinoNano('/dev/ttyUSB0') # Hardware serial communication 
except: 
  print("Serial connection error please reconnect the hardware") # 
   # Language for the Smar toilet machine 
lang1 = 'th'
lang2 = 'en'
lang3 = 'zh'
#from googletrans import Translator # Google translate 
sox_effects = ('speed','1.02') # Sox effect for voice speed 
# Computer vision part 
cap = cv.VideoCapture(0)  # Camera 1 detection
try:
  Motionsense = hardware.get_pin('d:2:i') # Motion detector sensor input 
except: 
   print("Pins error please recheck")
it = pyfirmata.util.Iterator(hardware) 
it.start() 
Motionsense.enable_reporting()  # Motionsense reporting out 
hardware.analog[0].enable_reporting() 
hardware.analog[1].enable_reporting() 
hardware.analog[2].enable_reporting() 
hardware.analog[3].enable_reporting() 
hardware.analog[4].enable_reporting() 
hardware.analog[5].enable_reporting() 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def fusionsensor(WaterLevl1,WaterLev2,WaterLev3,WaterLev4,Sitdec1,Sitdec2,Motionsensor): # Fusoin sensor
     # Water level and sitting toilet detection 
     if WaterLevel1 >= 900: 
             speech = Speech("Water level in tank 1 is now level 1",lang1)
             speech.play(sox_effects) # Speech fully play
             speech = Speech("ระดับนำ้ในถังที่ 1 ตอนนี้ ระดับที่ 1",lang2)  # Thai language for the speech s$
             speech.play(sox_effects) # Speech fully play
             speech = Speech("水箱1中的水位現在為1級",lang3)  # Chinese language speech synthesys 
             speech.play(sox_effects)               
     if WaterLevel2 >= 900:
             speech = Speech("Water level in tank 1 is now full",lang1)
             speech.play(sox_effects) # Speech fully play
             speech = Speech("ระดับนำ้ในถังที่ 1 ตอนนี้เต็มแล้ว",lang2)  # Thai language for the speech s$
             speech.play(sox_effects) # Speech fully play
             speech = Speech("水箱1級現已滿。",lang3)  # Chinese language speech synthesys 
             speech.play(sox_effects)
     if WaterLevel3 >= 900:
             speech = Speech("Water level in tank 1 is now level ",lang1)
             speech.play(sox_effects) # Speech fully play
             speech = Speech("ระดับนำ้ในถังที่ 2 ตอนนี้ ระดับที่ 1",lang2)  # Thai language for the speech s$
             speech.play(sox_effects) # Speech fully play
             speech = Speech("水箱2中的水位現在為1級",lang3)  # Chinese language speech synthesys 
             speech.play(sox_effects)
     if WaterLevel4 >= 900:
             speech = Speech("Water level in tank 2 is now full",lang1)
             speech.play(sox_effects) # Speech fully play
             speech = Speech("ระดับนำ้ในถังที่ 2 ตอนนี้เต็มแล้ว",lang2)  # Thai language for the speech s$
             speech.play(sox_effects) # Speech fully play
             speech = Speech("水箱2級現已滿。",lang3)  # Chinese language speech synthesys 
             speech.play(sox_effects)
     if Sitdec1 < 1023: 
             speech = Speech("Sitting on the closet",lang1)
             speech.play(sox_effects)
             speech = Speech("ตอนนี้มีคนนั่งบนส้วม",lang2)
             speech.play(sox_effects)
             speech = Speech("現在，有人坐在馬桶上。",lang3)
             speech.play(sox_effects)
     if Sitdec2 < 1023: 
             speech = Speech("Sitting on the closet",lang1)
             speech.play(sox_effects)
             speech = Speech("ตอนนี้มีคนนั่งบนส้วม",lang2)
             speech.play(sox_effects)
             speech = Speech("現在，有人坐在馬桶上。",lang3)
             speech.play(sox_effects)
     if Motionsensor == 'True':   # Sensor read true state ment after retected the motion 
             ret,frame = cap.read() # Reading the frame from the camera picture input 
             cv2.imshow('Smarttoilet Cam guard',frame) 
             print(str(Today) + str(timedata)) # Showing today time data 
             cv2.imwrite(str(Today) +"/"+ str(timedata) + ".png",frame) # Time as name picture data
             speech = Speech("Hello Welcome to smart toilet we keep your picture data as user identification",lang1)
             speech.play(sox_effects) # Speech fully play
             speech = Speech("สวัสดีค่ะ ยินดีต้อนรับสู่ห้องนำ้อัจฉริยะค่ะเราขอเก็บข้อมูลรูปภาพของคุณเพื่อใช้ในการระบุตัวผู้ใช้งาน",lang2)  # Thai language for the speech synthesys output  function 
             speech.play(sox_effects) # Speech fully play
             speech = Speech("您好，歡迎來到智能浴室。我們希望收集您的圖像數據以便識別 ",lang3)  #Chinese language speech synthesys 
             speech.play(sox_effects)    
             if cv2.waitKey(1) & 0xFF == ord('q'): 
                  break 
        cap.release()
     elif Motionsensor == 'False':
        cv2.destroyAllWindow() #Destroy all window after done software   
def Waterlevel1():   # Analog read level 
  WaterLev1 = hardware.analog[0].read() 
  WaterLev2 = hardware.analog[1].read()  
  return WaterLev1,WaterLev2
def Waterlevel2():   # Analog read level
  WaterLev3 = hardware.analog[2].read() 
  WaterLev4 = hardware.analog[3].read() 
  return WaterLev3,WaterLev4
#def Typeofliquidresistance(WaterLev3,WaterLev4):       
def Sitdetector():
  Sitdec1 = hardware.analog[4].read() 
  Sitdec2 = hardware.analog[5].read() 
  return Sitdec1,Sitdec2 
def Motionsensor(): 
    Mot = Motionsense.read()
    return Mot           
while True:  # Looping iteration looping for the function 
      # 2 States Water leveling can detecting multiple substance in the water acording to the resistance
   WaterLev1,WaterLev2 = Waterlevel1 
   WaterLev3,WaterLev4 = Waterlevel2
     # Detecting people when sitting   
   Sitdec1,Sitdec2 = Sitdetector   
   # Operating conroller with the fusion sensor 
   fusionsensor(WaterLev1,WaterLev2,WaterLev3,WaterLev4,Sitdec1,Sitdec2,Motionsensor)   #Fusion all sensor and the camera together for display status of the user on the camera 
   
