import os
f = open("/sys/class/backlight/intel_backlight/brightness","r")
x = int(f.readlines()[0])
f.close()
if(x<=1300):
	x=x+200
else:
	x=1500
os.system("echo '" +str(x) +"' >> /sys/class/backlight/intel_backlight/brightness")



