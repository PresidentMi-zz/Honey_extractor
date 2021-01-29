import minimalmodbus
import serial
import time


#----  DEFAUL ----#
    #ADDRESS = 1
    #PORT = '/dev/ttyUSB0'


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



class VFD_Control:
    def __init__(self,PORT,ADDRESS):
        self.vfd=self.setup(PORT,ADDRESS)

    def setup(self,PORT,ADDRESS):

        try:
            vfd = minimalmodbus.Instrument(PORT, ADDRESS)  # port name, slave address (in decimal)

        except:
            print("No connection!")
            return None

        vfd.serial.baudrate = 9600         # Baud
        vfd.serial.bytesize = 8
        vfd.serial.parity  = serial.PARITY_NONE
        vfd.serial.stopbits = 1
        vfd.serial.timeout  = 0.2

        # number_poles = vfd.read_register(213, 0)
        # print("Number of poles: ", number_poles)

        # vfd.write_register(101, 5, 0, 6)  #main frequency source 5: RS485
        # time.sleep(0.05)
        # vfd.write_register(102, 2, 0, 6)  #START signal select 2: RS485
        # time.sleep(0.05)
        vfd.write_register(104, 1, 0, 6)  #Allow reverse rotation
        time.sleep(0.05)

        vfd.write_register(213, 2, 0, 6)  #Number of poles
        time.sleep(0.05)

        vfd.write_register(700, 1, 0, 6)  #Boudrate 1:9600
        time.sleep(0.05)
        vfd.write_register(701, 3, 0, 6)  #8-N-1
        time.sleep(0.05)

        return vfd

    def change_frequency(self, freq): #frequency 0-60 Hz Moze i decimalni zapis npr 39.6

        freq_for_vfd = 10 * round(float(freq), 1)
        self.vfd.write_register(8193, freq_for_vfd, 0, 6)

    def run(self,direction):    #direction F-Forward, R-reverse

        if direction == 'F':
             self.vfd.write_register(8192, 10, 0, 6)
        elif direction == 'R':
             self.vfd.write_register(8192, 6, 0, 6)  # ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16

    def jog(self, direction):

        if direction == 'F':
            self.vfd.write_register(8192,int(0x0B), 0,6)

        elif direction == 'R':
            self.vfd.write_register(8192, 7, 0, 6)  # ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16
            print("Motor Stop")

    def stop(self):
        # STOP
        self.vfd.write_register(8192, 1, 0, 6)  # ADRESS, VALUE, DECIMAL PLACES, COMMAND 6 OR16

    def reverse_direction(self):
        self.vfd.write_register(119, 1, 0, 6)

    def read_outvoltage(self):
        out_voltage = self.vfd.read_register(5, 1)  # Registernumber, number of decimals
        print(out_voltage)




