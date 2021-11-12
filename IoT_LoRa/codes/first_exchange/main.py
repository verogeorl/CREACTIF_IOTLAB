from network import LoRa
import socket
import time
import ubinascii
import utime
import pycom
import struct
import machine

'''
See also:

https://www.geeksforgeeks.org/python-bit-functions-on-int-bit_length-to_bytes-and-from_bytes/

https://www.thethingsnetwork.org/docs/devices/lopy/usage/

https://forum.pycom.io/topic/5149/buffer-too-small-problem-lora-lopy-4/3

https://stackoverflow.com/questions/1708835/python-socket-receive-incoming-packets-always-have-a-different-size

https://alepycom.gitbooks.io/pycom-docs/content/chapter/firmwareapi/pycom/network/lora.html

https://www.semtech.com/products/wireless-rf/lora-core/sx1276

'''

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)


#//////////////// !! Change the app-key here !! ////////////////
# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('EFE2E2A8F7BA001DF112FABB92B742C6') #lopy'-1
#uncomment to use LoRaWAN application provided dev_eui
#dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')

# Uncomment for US915 / AU915 & Pygate
# for i in range(0,8):
#     lora.remove_channel(i)
# for i in range(16,65):
#     lora.remove_channel(i)
# for i in range(66,72):
#     lora.remove_channel(i)

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

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

# send some data
#s.send(bytes([0x01, 0x02, 0x03]))
result = 4
print('result: ', result)

# Convert to byte array for transmission
#raw = bytearray(struct.pack(">f", result))
#raw = bytes([result])
#print('raw: ', raw)

# z = result.to_bytes(2, byteorder="big") not working in upyth
# print('result in bytes: ', z )

#s.send(raw)
#s.send(bytes([result]))

'''
Convert to bytes:

 int.to_bytes(length, byteorder, *, signed=False)
 
Return an array of bytes representing an integer.If byteorder is “big”, 
the most significant byte is at the beginning of the byte array. 
If byteorder is “little”, the most significant byte is at the end of the byte array. 
The signed argument determines whether two’s complement is used to represent the integer.
'''
s.send(result.to_bytes(2, 'big')) # use 2 bytes to represent an integer and byteorder big endian

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
#cache line size (usually 64 bytes, but 128 is also used)
# hardware limitations: Packet engine up to 256 bytes with CRC -> Rx/Tx FIFO buffer
buffersize = 64  # this is the max size used to store the received data, 
data = s.recv(buffersize)  
print(data)


