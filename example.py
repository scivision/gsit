#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:17:17 2016

@author: Sebastijan Mrak <smrak@gmail.com>
"""

import numpy as np
import plotoptics
import datetime
import asi
import pyGps
import pandas
from pandas import read_hdf
import yaml

#Type paths to raw data
fn = '/home/smrak/Documents/TheMahali/rinex/'
asi_folder3 = '/home/smrak/Documents/TheMahali/Allsky_multi/'
fname = '/home/smrak/Documents/TheMahali/rinex/mah22800.h5'
navfname = '/home/smrak/Documents/TheMahali/gnss/gps/brdc2800.15n'
timelim = ['10/07/2015', '06:10:00', '10/07/2015', '06:50:00']
sv = 23
rx = 2
ipp_alt = 130E3
stream = yaml.load(open(fn+'mah22800.yaml', 'r'))
rx_xyz = stream.get('APPROX POSITION XYZ')
data = read_hdf(fname)
obstimes = np.array((data.major_axis))
obstimes = pandas.to_datetime(obstimes) 



# Plot data
# single keogram
def pkg():
    #Get keograms
    ipp = pyGps.getIonosphericPiercingPoints(rx_xyz, sv, obstimes, ipp_alt, navfname, cs='aer')
    t5, el5, i5, el_out4 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '558', obstimes=obstimes, elevation=ipp[1])
    t4, el4, i4, el_out5 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '428', obstimes=obstimes, elevation=ipp[1])
    t6, el6, i6, el_out6 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                        '630', obstimes=obstimes, elevation=ipp[1])
    plotoptics.plotKeogram(t5, el5, i5/1E3, ylim=[45,85], title='Green line intensity',
                       pcolorbar=True, cmap='viridis', cbartick=[0,2,4,6,8], 
                       cbartitle='kR', ytick=[45,55,65,75,85],
                       xtick=[datetime.datetime(2015, 10, 7, 6, 10, 0), 
                               datetime.datetime(2015, 10, 7, 6, 15, 0),
                               datetime.datetime(2015, 10, 7, 6, 20, 0),
                               datetime.datetime(2015, 10, 7, 6, 25, 0),
                               datetime.datetime(2015, 10, 7, 6, 30, 0),
                               datetime.datetime(2015, 10, 7, 6, 35, 0),
                               datetime.datetime(2015, 10, 7, 6, 40, 0)],
                       xlim=[datetime.datetime(2015, 10, 7, 6, 10, 0),
                              datetime.datetime(2015, 10, 7, 6, 40, 0)])

# Keogram with 2 subplots
def p2kg():
    #Get keograms
    ipp = pyGps.getIonosphericPiercingPoints(rx_xyz, sv, obstimes, ipp_alt, navfname, cs='aer')
    t5, el5, i5, el_out4 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '558', obstimes=obstimes, elevation=ipp[1])
    t4, el4, i4, el_out5 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '428', obstimes=obstimes, elevation=ipp[1])
    t6, el6, i6, el_out6 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '630', obstimes=obstimes, elevation=ipp[1])
    plotoptics.plot2Keogram(t6, t5, el6, el5, i6/i4, i5/i4, ylim = [45, 85], 
                        title1 = 'Ratio of red and blue line',  
                        title2 = 'Ratio of green and blue line',  
                        pcolorbar=True, ytick=[45, 55, 65, 75, 85],
                        cmap='viridis', cbartick1=[0,0.4,0.8,1.2,1.6],
                        cbartick2=[0,4,8,12,15], cbartitle1='',cbartitle2='',
                        xtick=[datetime.datetime(2015, 10, 7, 6, 10, 0), 
                               datetime.datetime(2015, 10, 7, 6, 15, 0),
                               datetime.datetime(2015, 10, 7, 6, 20, 0),
                               datetime.datetime(2015, 10, 7, 6, 25, 0),
                               datetime.datetime(2015, 10, 7, 6, 30, 0),
                               datetime.datetime(2015, 10, 7, 6, 35, 0),
                               datetime.datetime(2015, 10, 7, 6, 40, 0)],
                        xlim=[datetime.datetime(2015, 10, 7, 6, 10, 0),
                              datetime.datetime(2015, 10, 7, 6, 40, 0)])
#Keogram with 3 subplots

def p3kg():
    #Get keograms
    ipp = pyGps.getIonosphericPiercingPoints(rx_xyz, sv, obstimes, ipp_alt, navfname, cs='aer')
    t5, el5, i5, el_out4 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '558', obstimes=obstimes, elevation=ipp[1])
    t4, el4, i4, el_out5 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '428', obstimes=obstimes, elevation=ipp[1])
    t6, el6, i6, el_out6 = asi.getASIKeogramIPP(asi_folder3, ipp[0], ipp_alt, timelim, 
                                       '630', obstimes=obstimes, elevation=ipp[1])
    plotoptics.plot3Keogram(t5, t6, t4, el5, el6, el4, i5/1E3, i6/1E3, i4/1E3, 
                        ylim=[45,85], title1 = 'Green line, 588nm',
                        title2 = 'Red line, 588nm', title3 = 'Blue line, 588nm',
                        pcolorbar=True, ytick=[45, 55, 65, 75, 85], cmap='viridis',
                        cbartick1=[0,2,4,6,8], cbartick2=[0,0.4,0.6,0.8,1],
                        cbartick3=[0,0.2,0.6,1, 1.4], 
                        cbartitle1='kR', cbartitle2='kR', cbartitle3='kR',
                        xtick=[datetime.datetime(2015, 10, 7, 6, 10, 0), 
                               datetime.datetime(2015, 10, 7, 6, 15, 0),
                               datetime.datetime(2015, 10, 7, 6, 20, 0),
                               datetime.datetime(2015, 10, 7, 6, 25, 0),
                               datetime.datetime(2015, 10, 7, 6, 30, 0),
                               datetime.datetime(2015, 10, 7, 6, 35, 0),
                               datetime.datetime(2015, 10, 7, 6, 40, 0)],
                        xlim=[datetime.datetime(2015, 10, 7, 6, 10, 0),
                              datetime.datetime(2015, 10, 7, 6, 40, 0)])
# Intensity graph
def pInt():
    ipp = pyGps.getIonosphericPiercingPoints(rx_xyz, sv, obstimes, ipp_alt, navfname, cs='aer')
    t, d = asi.getAllskyIntensityAER(asi_folder3, ipp[0], ipp[1], ipp_alt,
                                          timelim, '558', obstimes=obstimes)
    t4, d4 = asi.getAllskyIntensityAER(asi_folder3, ipp[0], ipp[1], ipp_alt,
                                          timelim, '428', obstimes=obstimes)
    t6, d6 = asi.getAllskyIntensityAER(asi_folder3, ipp[0], ipp[1], ipp_alt,
                                   timelim, '630', obstimes=obstimes)
    plotoptics.plotIntensity(t,d, ylabel='Intensity [R]', xlabel='UT', label1='558nm',
                         t2=t4, y2=d4, t3=t6, y3=d6, label2='428nm', label3='630nm',
                         color1='g', color2 ='b', color3='r', 
                         title='All-sky imager intensity', ylim=[300, 2500], legend=True,
                         xlim=[datetime.datetime(2015, 10, 7, 6, 10, 0),
                               datetime.datetime(2015, 10, 7, 6, 40, 0)])

if __name__ == '__main__':
    #pkg()
    #p2kg()
    #p3kg()
    #pInt()