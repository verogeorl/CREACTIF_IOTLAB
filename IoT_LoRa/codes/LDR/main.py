# Measuring light with an LDR
from network import LoRa
import socket
import utime
import ubinascii
import pycom
import ustruct
import machine


adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin='P15')

# Light measurment
def light_measure():
    print("")
    print("Reading LDR Sensor...")
    value = apin()
    print("ADC count = %d" %(value))

    # LoPy  has 1.1 V input range for ADC
    light = value
    print("light = %5.1f" % (light))

    # returning integer
    return int(light)

light_measure()

"""
# Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('EFE2E2A8F7BA001DF112FABB92B742C6')  # to modify for each node !!

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

print('before loop')
##
# create data

result = light_measure()

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
