import serial.tools.list_ports
import subprocess

all_devices=serial.tools.list_ports.comports()
possible_devices =[]
for x in all_devices:
	if x.vid==4292 and x.pid==60000:
		possible_devices.append(x)	
if len(possible_devices)==0:
	print ("Error: no Device avalibale!")
elif len(possible_devices)==1:
	print (possible_devices[0].device)
	subprocess.Popen("esptool.py --chip esp32 --port "+possible_devices[0].device+" --baud 921600 --before default_reset --after hard_reset write_flash -z \
 --flash_size detect 0x1000 ./bin/bootloader.bin 0x10000 ./bin/ft32.ino.doitESP32devkitV1.bin 0x291000 ./bin/spiffs.bin",shell=True)
elif len(possible_devices)>2:
	print ("Error: detected to many possible devices!")
