# Bluetooth LE 

TX data path integrity is not guaranteed during the Bluetooth LE handover.

Some instabilities may occur in demanding Bluetooth LE connection scenarios \(such as mutiple Bluetooth LE connection, very short Connection Intervals\), and in some Channel Sounding configurations.

#   Bluetooth LE controller:

Max number of connections supported : 8 
Potential instabilities particularly with short Connection Intervals  
Channel Sounding (CS) not supported: 
	Mode 3 steps 
	RTT with Random sequence 
	RTT Random sequence NADM 
	Antenna Diversity with CS 1xN / Nx1 (with N >1 and N<=4) 
	More than one CS procedure in parallel 

**Note:** Documentation may not be fully updated to refer to MCX W72 devices.

**Parent topic:**[Known issues](../topics/known_issues.md)

