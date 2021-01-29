import minimalmodbus
import serial
import time

try:
    vfd = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
except:
    print("No connection!")

vfd.serial.baudrate = 9600         # Baud
vfd.serial.bytesize = 8
vfd.serial.parity   = serial.PARITY_NONE
vfd.serial.stopbits = 1
vfd.serial.timeout  = 0.2

#-----------SETUP--------#

#Nubmer of poles
number_poles = vfd.read_register(213, 0)
print("Number of poles: ",number_poles)
vfd.write_register(213, 2, 0, 6)


#Read Output Voltage
out_voltage = vfd.read_register(5, 1)  # Registernumber, number of decimals
print(out_voltage)

#RUN Forward
vfd.write_register(8192, 10, 0,6)



while 1:
    freq=input("Unesite frekvenciju: ")

    if freq.lower() == 'n':
        break
    else:
        freq_for_vfd=10*round(float(freq),1)
        vfd.write_register(8193,freq_for_vfd , 0, 6)


# time.sleep(20)
# print("Stop!\n")

#STOP
vfd.write_register(8192, 1, 0,6)  #ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16

# write_register(registeraddress, value, number_of_decimals=0, functioncode=16, signed=False)[source]
# Write an integer to one 16-bit register in the slave, possibly scaling it.
#
# The slave register can hold integer values in the range 0 to 65535 (“Unsigned INT16”).
#
# Args:
# registeraddress (int): The slave register address (use decimal numbers, not hex).
# value (int or float): The value to store in the slave register (might be scaled before sending).
# number_of_decimals (int): The number of decimals for content conversion.
# functioncode (int): Modbus function code. Can be 6 or 16.
# signed (bool): Whether the data should be interpreted as unsigned or signed.

#RUN Reverse
# vfd.write_register(8192, 6, 0,6)  #ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16
# #JOG Forward
# vfd.write_register(8192,int(0B), 0,6)  #ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16
# #JOG Reverse
# vfd.write_register(8192, 7, 0,6)  #ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16
