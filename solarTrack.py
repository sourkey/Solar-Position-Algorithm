#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sourkey

Based on calculations used by NOAA and from Astronomical Algorithms by Jean Meeus
"""
import math
import datetime
import time

class Sun:
    
    def __init__(self):
        self.solPos = []

    def calcSun(self, year=2019, month=2, day=2, hour=14, minute=0, second=0, lat=0, long=0):
        self.time = int(time.mktime(datetime.datetime(year, month, day, hour, minute, second).timetuple()))
        self.latitude = lat
        self.longitude = long
        self.hour = hour
        self.minute = minute
        self.second = second
        
        #Julian Century
        self.T = ((((self.time / 86400) + 2444239.5) - 2451545) / 36525)
        #rad/degree conversion              	
        self.k = math.pi / 180.0000
        #Geom Mean Long Sun (deg) *updated from 280.46645                               						
        self.Lo = math.fmod(280.46646 + 36000.76983 * self.T + 0.0003032 * self.T**2, 360)	
        #Geom Mean Anom Sun (deg)
        self.M = 357.52911 + 35999.05029 * self.T - 0.0001537 * self.T**2
        #Eccentricity of Earth Orbit								
        self.eeo = 0.016708694 - self.T * 0.000042037 + self.T**2 * 0.0001537
		#Sun Eq of Ctr							
        self.SunCTR = math.sin(self.M * self.k) * (1.914602 - self.T * (0.004817 + 0.000014 * self.T)) \
                + math.sin(2.0000 * self.M * self.k) * (0.019993 - 0.000101 * self.T) + math.sin(3.0000 \
                * self.M * self.k) * 0.000289
		#Sun True Longitude (deg)
        self.SunTrueLong = self.Lo + self.SunCTR
        #Sun True Anom (deg)                     						
        self.SunTrueAnom = self.M + self.SunCTR
        #Solar radius                    						
        self.SunRadVect = (1.000001018 * (1.0000 - self.eeo**2)) / (1.0000 + self.eeo * math.cos(self.SunTrueAnom * self.k))
		#Apparent solar longitude		
        self.SunAppLong = self.SunTrueLong - 0.00569 - 0.00478 * math.sin(self.k * (125.04 - 1934.136 * self.T))
        #Mean Obliq Ecliptic
        self.MOE = 23.0000 + (26.0000 +((21.4480 - self.T * (46.8150 + self.T * (0.00059 - self.T * 0.001813)))) / 60.0000) / 60.0000
        #Obliq correction
        self.ObliqC = self.MOE + 0.00256 * math.cos(self.k * (125.0400 - 1934.1360 * self.T))
        #Sun rt ascen             
        self.SunRtA = (math.atan2(math.cos(self.k * self.SunAppLong),\
                math.cos(self.k * self.ObliqC) * math.sin(self.k * self.SunAppLong))) / self.k   
        #Sun declination
        self.SunDec = (math.asin(math.sin(self.k * self.ObliqC) * math.sin(self.k * self.SunAppLong))) / self.k
        #var y
        self.VarY = math.tan(self.k * (self.ObliqC / 2.0000)) * math.tan(self.k * (self.ObliqC / 2.0000))
        #eq of time            
        self.EqTime = 4.0000 * (self.VarY * math.sin(2.0000 * self.k * self.Lo) - 2.0000 * self.eeo \
                * math.sin(self.k * self.M) + 4.0000 * self.eeo * self.VarY * math.sin(self.k * self.M)\
                * math.cos(2.0000 * self.k * self.Lo) - 0.5000 * self.VarY * self.VarY \
                * math.sin(4.0000 * self.k * self.Lo) - 1.2500 * self.eeo**2 * math.sin(2.0000 * self.k * self.M)) / self.k
        #true solar time (min)
        self.TrueSolT = math.fmod((self.hour + self.minute / 60.0000 + self.second / 3600.0000) / 24.0000 * 1440.0000\
                + self.EqTime + 4.0000 * self.longitude,1440.0000) 	
        
        #Hour angle calculation
        if self.TrueSolT / 4.0000 < 0.0000:                                             
            self.HourAng = self.TrueSolT / 4.0000 + 180.0000
        else:
            self.HourAng = self.TrueSolT / 4.0000 - 180.0000

        #Solar zenith
        self.SolZen = (math.acos(math.sin(self.k * self.latitude) * math.sin(self.k * self.SunDec)\
                + math.cos(self.k * self.latitude) * math.cos(self.k * self.SunDec) * math.cos(self.k * self.HourAng))) / self.k
        #solar elevation
        self.SolEle = 90.0000 - self.SolZen                                                                                                      

        #solar azimuth calculation
        if self.HourAng > 0:                                                         
           self.SolAzi = math.fmod(180.0000 + (math.acos((math.sin(self.k * self.latitude) * math.cos(self.k * self.SolZen)\
                - math.sin(self.k * self.SunDec)) / (math.cos(self.k * self.latitude) * math.sin(self.k * self.SolZen)))) / self.k,360.0000)
        else:
           self.SolAzi = math.fmod(540.0000 - (math.acos((math.sin(self.k * self.latitude) * math.cos(self.k * self.SolZen)\
                - math.sin(self.k * self.SunDec)) / (math.cos(self.k * self.latitude) * math.sin(self.k * self.SolZen)))) / self.k,360.0000)
        
        print('Sol Elevation:', self.SolEle)
        print('Sol Azimuth:', self.SolAzi)
