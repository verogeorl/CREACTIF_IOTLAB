from network import LoRa
import socket
import time
import ubinascii
import utime
import pycom
import struct
import machine


"""
# Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('xxxxxxxxxxxxxxxxx')  # to modify for each node !!

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)


# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)
"""
print('before loop')
##
# create data

adc = machine.ADC()
apin = adc.channel(pin='P16')

# make the average out of 5 measurements -> every 1 seconds
temp= 0

for i in range(0, 5):
  millivolts = apin.voltage()
  degC = (millivolts - 500.0) / 10.0
  #degF = ((degC * 9.0) / 5.0) + 32.0

  temp = temp + degC

  #print(millivolts)
  print('i= ', i+1)
  print('temperature (Code) : ', degC)
  #print(degF)

  time.sleep(1)


result = temp/5

print('mean temperature (C) : ', result)

"""
#multiply by 100 for byte transmission and int
result = int(100*result)

print('temp int times 100 : ', result)

##
# send data
s.send(result.to_bytes(2, 'big'))

print('after send')
# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)
"""
