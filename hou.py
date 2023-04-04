# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:35:09 2023

@author: lyx
"""

import pandas as pd
import xarray as xr
import numpy as np
# import xlwt

file1 = r'D:/Luyuxia/sshf1982.nc'
t = xr.open_dataset(file1)

#计算是否是润年
def leap_year(year):
    if 0 == year % 4 and 0 != year % 400 or 0 == year % 400:
        return True
    else:
        return False

#获取当月每月天数
def get_month_days(year, month):
    
    days = 31
    if 2 == month:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif 4 == month or 6 == month or 9 == month or 11 == month:
        days = 30
    return days


#定义候的变量，每五天为一侯
hou=5
jia=np.zeros(((1,61,129)))
he=np.zeros(((72,61,129)))
day_1=[]
day_2=[]
mn=np.zeros(((73,61,129)))
#注意这里是几年到几年
#换的时候的话把循环里的_year_替换成i即可
for i in range(1982,1983):#利用整年进行计算
    for j in range(1,13):
            for day in range(1, get_month_days(i, j)+1):#当月天数
                    if j<10:
                        if day<10:
                            day1=str(i)+"-0"+str(j)+"-0"+str(day)
                        else:
                            day1=str(i)+"-0"+str(j)+"-"+str(day)
                    else:
                        if day<10:
                            day1=str(i)+"-"+str(j)+"-0"+str(day)
                        else:
                            day1=str(i)+"-"+str(j)+"-"+str(day)
                        
                    # print(day1)
                    hou=hou+1
                    if(hou==6):
                        range_day1=day1
                    if(hou==10):
                        range_day2=day1
                        s1 = '{0}'.format(range_day1)
                        s2 = '{0}'.format(range_day2)
                        #print("计算的数据为："+range_day1+"~"+range_day2)
                        day_1.append(s1)
                        day_2.append(s2)
                        hou=5
#这段仅测试用，测试链表结构是否正确
for h in range(len(day_1)):
    print(str(h)+"侯为："+day_1[h]+"~"+day_2[h])
#这段仅测试用，测试链表结构是否正确



#最后得出一个总的计算
for h_1 in range(len(day_1)):
    s1 = '{0}'.format(day_1[h_1])#进行格式转换
    s2 = '{0}'.format(day_2[h_1])
    mn[h_1, :, : ] = np.array(t['sshf'].loc[s1:s2]).reshape(5,1,61,129).mean(0)       

                     