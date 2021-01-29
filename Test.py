from VFD_Control import VFD_Control
import time


ADDRESS = 1
PORT = '/dev/ttyUSB0'


motor=VFD_Control(PORT,ADDRESS)


motor.setup(PORT,ADDRESS)
motor.read_outvoltage()

motor.change_frequency(40)
motor.run('F')
time.sleep(5)
motor.stop()