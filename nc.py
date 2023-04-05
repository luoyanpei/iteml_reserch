# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:20:45 2023

@author: lyx
"""

import netCDF4 as nc
import sys

sys.path.append(r'D:\luyuxia\py')      # 添加函数文件位置
import hou
# print(hou.mn.shape)
#导出nc  
f_w = nc.Dataset('E:\new\hou1982.nc','w',format = 'NETCDF4')   #创建一个格式为.nc的，名字为 ‘hecheng.nc’的文件        

#确定基础变量的维度信息。相对与坐标系的各个轴(x,y,z)
f_w.createDimension('time',73)  
f_w.createDimension('lat',61)   
f_w.createDimension('lon',129)  
#创建变量。参数依次为：‘变量名称’，‘数据类型’，‘基础维度信息’
f_w.createVariable('time','i',('time'))   #np.int64
f_w.createVariable('lat','f',('lat'))  #np.float64
f_w.createVariable('lon','f',('lon')) #np.float64
f_w.createVariable( 'sshf', 'f', ('time','lat','lon'))

#写入变量time的数据。维度必须与定义的一致。
f_w.variables['time'][:] = hou.day_1
f_w.variables['lat'][:] = hou.t.lat
f_w.variables['lon'][:] = hou.t.lon
f_w.variables['sshf'][:] = hou.mn

f_w.close()
# f_w.to_netcdf('E:\\new\\hou1982.nc')#输出合并后的nc文件
