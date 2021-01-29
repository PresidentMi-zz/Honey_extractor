from VFD_Control import VFD_Control


ADDRESS = 1
PORT = '/dev/ttyUSB0'


motor=VFD_Control()


motor.setup(PORT,ADDRESS)
motor.run('F')
change_frequency(39.6)
