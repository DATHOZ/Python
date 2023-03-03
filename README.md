# Python

Python Collection
#In this repository I will publish network python scripts to work with wireless devices

ap_moves85.py - This script creates the configuration to migrate APs from AIREOS to IOS XE using the file data.txt with data from command "sh ap search <ap_name>". Run the command on your favorite ssh tool and copy the output into the data.txt file

Example data.txt:

1 00:6b:f1:xx:xx:xx ap3-h10-a AIR-AP2802I-B-K9  
2 f4:db:e6:xx:xx:xx ap3-l15 AIR-AP2802I-B-K9  
3 ac:7a:56:xx:xx:xx ap1-m18 AIR-AP2802I-B-K9  
4 ac:3a:67:xx:xx:xx apb-g14 AIR-AP2802I-B-K9  
5 70:db:98:xx:xx:xx ap1-k20 AIR-AP2802I-B-K9  
6 48:8b:0a:xx:xx:xx ap2-o16 AIR-AP2802I-B-K9  
7 1c:d1:e0:xx:xx:xx ap2-g15 AIR-AP2802I-B-K9  
8 a0:b4:39:xx:xx:xx ap2-j20 AIR-AP2802I-B-K9  
9 00:6b:f1:xx:xx:xx ap6-g11 AIR-AP2802I-B-K9  
10 00:6b:f1:xx:xx:xx apa-n5 AIR-AP2802I-B-K9

ap_moves98.py - This script creates the configuration to migrate APs between 9800 IOS XE using the file data.txt with data from command "sh ap summary | inc <ap_name>". Run the command on your favorite ssh tool and copy the output into the data.txt file

Example data.txt:

ap-0000-uxx 2 AIR-AP1815W-B-K9 00ee.abxx.yyyy 00ee.abxx.yyyy US -B 10.x.x.x Registered  
ap-0000-uxxx 2 AIR-AP1815W-B-K9 00ee.abxx.yyyy 00ee.abxx.yyyy US -B 10.x.x.x Registered  
ap-0000-uxxxx 2 AIR-AP1815W-B-K9 00ee.abxx.yyyy 00ee.abxx.yyyy US -B 10.x.x.x Registered

ap_reset.py - This script creates the configuration to reset APs. It can be used on both AIREOS or IOS XE by changing the primary_command or old_command

#author: Dave Thomaz
