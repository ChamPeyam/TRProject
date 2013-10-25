import socket
import sys
import time
import os.path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.close()
host = ''
port = 10001
s.bind((host,port))
s.listen(20)
conn, addr = s.accept()
print ('connected to', addr)

if os.path.exists("/sys/devices/bone_capemgr.7/slot-4/") == False:
	fw = file ("/sys/devices/bone_capemgr.7/slots", "w")
	fw.write("am33xx_pwm")
	fw.close()

if os.path.exists("/sys/devices/ocp.2/pwm_test_P8_13.9") == False: 
	fw = file ("/sys/devices/bone_capemgr.7/slots", "w")
	fw.write("bone_pwm_P8_13")
	fw.close()


if os.path.exists("/sys/devices/ocp.2/pwm_test_P8_19.10") == False: 
	fw = file ("/sys/devices/bone_capemgr.7/slots", "w")
	fw.write("bone_pwm_P8_19")
	fw.close()	

if os.path.exists("/sys/devices/ocp.2/pwm_test_P9_14.11") == False: 
	fw = file ("/sys/devices/bone_capemgr.7/slots", "w")
	fw.write("bone_pwm_P9_14")
	fw.close()

if os.path.exists("/sys/devices/ocp.2/pwm_test_P9_16.12") == False: 
	fw = file ("/sys/devices/bone_capemgr.7/slots", "w")
	fw.write("bone_pwm_P9_16")
	fw.close()

if os.path.exists("/sys/class/gpio/gpio34") == False:
	fw = file("/sys/class/gpio/export", "w")
	fw.write("%d" % (34))
	fw.close()

if os.path.exists("/sys/class/gpio/gpio35") == False:
	fw = file("/sys/class/gpio/export", "w")
	fw.write("%d" % (35))
	fw.close()

if os.path.exists("/sys/class/gpio/gpio38") == False:
	fw = file("/sys/class/gpio/export", "w")
	fw.write("%d" % (38))
	fw.close()

if os.path.exists("/sys/class/gpio/gpio39") == False:
	fw = file("/sys/class/gpio/export", "w")
	fw.write("%d" % (39))
	fw.close()
	

fw = file("/sys/class/gpio/gpio38/direction", "w")
fw.write("in")
fw.close()
fw = file("/sys/class/gpio/gpio39/direction", "w")
fw.write("in")
fw.close()
fw = file("/sys/class/gpio/gpio34/direction", "w")
fw.write("in")
fw.close()
fw = file("/sys/class/gpio/gpio35/direction", "w")
fw.write("in")
fw.close()
while 1:
	data = conn.recv(1024)
	test = data.decode('utf-8')
	print (test)
	sp = test.split(",")
	m1 = sp[0]
	s1 = float(m1)
	MS1 = 1444000 - (1444000*s1*0.01)
	PWM1 = int(MS1)
	strpwm1 = str(PWM1)
	
	dr1 = sp[1]	

	m2 = sp[2]
	s2 = float[m2]
	MS2 = 1444000 - (1444000*s2*0.01)
	PWM2 = int(MS2)
	strpwm2 = str(PWM2)

	dr2 = sp[3]	

	fw = file("/sys/class/gpio/gpio34/value", "w")
	fw.write("dr1")
	fw.close()

	fw = file("/sys/class/gpio/gpio35/value", "w")
	fw.write("dr1")
	fw.close()
	
	fw = file("/sys/class/gpio/gpio38/value", "w")
	fw.write("dr2")
	fw.close()

	fw = file("/sys/class/gpio/gpio39/value", "w")
	fw.write("dr2")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P8_13.9/period", "w")
	fw.write("1444000")
	fw.close
	
	fw = file("/sys/devices/ocp.2/pwm_test_P8_13.9/duty", "w")
	fw.write("strpwm1")
	fw.close()
	

	fw = file("/sys/devices/ocp.2/pwm_test_P8_19.10/period", "w")
	fw.write("1444000")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P8_19.10/duty", "w")
	fw.write("strpwm1")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P9_14.11/period", "w")
	fw.write("1444000")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P8_13.9/duty", "w")
	fw.write("strpwm2")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P8_14.12/period", "w")
	fw.write("1444000")
	fw.close()

	fw = file("/sys/devices/ocp.2/pwm_test_P8_13.9/duty", "w")
	fw.write("strpwm2")
	fw.close()
		


	if test == "Quit":
		s.close()
		fw = file("/sys/class/gpio/unexport", "w")
		fw.write("%d" % (34))
		fw.close()
		fw = file("/sys/class/gpio/unexport", "w")
		fw.write("%d" % (35))
		fw.close()
		fw = file("/sys/class/gpio/unexport", "w")
		fw.write("%d" % (38))
		fw.close()
		fw = file("/sys/class/gpio/unexport", "w")
		fw.write("%d" % (39))
		fw.close()
		print('Closing Socket')
		s.shutdown()
	if test == "LEDON":
		fw = file("/sys/class/leds/beaglebone:green:usr1/brightness", "w")
		fw.write("1")
		fw.flush()
	if test == "LEDOFF":
		fw = file("/sys/class/leds/beaglebone:green:usr1/brightness", "w")
		fw.write("0")
		fw.flush()
	if test == "high":
		fw = file("/sys/class/gpio/gpio38/value", "w")
		fw.write("1")
		fw.flush
	if test == "low":
		fw = file("/sys/class/gpio/gpio38/value", "w")
		fw.write("0")
		fw.flush
