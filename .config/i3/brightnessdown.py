import os
f = open("/sys/class/backlight/intel_backlight/brightness","r")
x = int(f.readlines()[0])
f.close()
if(x>=400):
	x=x-200
else:
	x=100
os.system("echo '" +str(x) +"' >> /sys/class/backlight/intel_backlight/brightness")



