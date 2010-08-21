import serial
import sys
import time
import random

class MoveMasterDriver(RobotBasicInterface):
    joint={
        body: { min: 0, max: 12000},
        shoulder: {min: 0, max: 5200},
        elbow: {min: 0, max: 3600},
        writh_l: { min:-4800, max: 4800},
        writh_r: { min: -4800, max: 4800},
        }

    # from nest - assumed need to verify that
    position={
        body: -12000,
        shoulder: -5200,
        elbow: 0,
        writh_l: 0,
        writh_r: 0
        }

    # default-config only the port should change
    # since everything else must be set at the device as such
    # from the manual we assume your configuration is
    # sw:  d1  d2  d3 ...
    # sw3: OFF OFF OFF OFF
    # sw2: OFF ON  ON  ON  ON  ON  ON  OFF
    # sw1: ON  OFF OFF OFF OFF OFF OFF OFF
    configuration={
        'port': '/dev/ttyUSB0',
        'baudrate': 9600,
        'bytesize': serial.EIGHTBITS,
        'parity': serial.PARITY_EVEN,
        'stopbits': serial.STOPBITS_ONE,
        'timeout': 0,
        'xonxoff': True,
        'rtscts': True,
        'writeTimeout': 0}
        
    def __init__(self):
        self.serial=serial.Serial()
        self.axes[0] = 12000 # 12000
        self.axes[1] = 5200 # 5200
        self.axes[2] = -3600 # 3600
        self.axes[3] = -4800 # 4800
        self.axes[4] = -9600 # 9600
        # setting default connection
        self.__setConnection()


    def __setConnection(self):

        if self.serial.isOpen():
            self.serial.close()
        
        self.serial.setPort( self.configuration["port"])
        self.serial.setBaudrate(self.configuration["baudrate"])
        self.serial.setByteSize(self.configuration["bytesize"])
        self.serial.setParity(self.configuration["parity"])
        self.serial.setStopbits(self.configuration["stopbits"])
        self.serial.setTimeout(self.configuration["timeout"])
        self.serial.setWriteTimeout(self.configuration["writeTimeout"])
        self.serial.setXonXoff(self.configuration["xonxoff"])
        self.serial.setRtsCts(self.configuration["rtscts"])

    def configureConnection(self,options={}):
        self.disconnect()
        map(lambda x: self.configuration[x[0]]=x[1],options)
        self.__setConnection()

    def disconnect(self):
        if self.serial.isOpen():
            return self.serial.close()
        return True

    def reconnect(self):
        result=self.disconnect()
        if result:
            return self.connect()
        return result

    def connect(self):

        if self.serial.isOpen():
            print "we are open ... close me first"
            return False
        
        self.serial.open()
        if not self.serial.isOpen():
            print "failed to open port " + self.serial.portstr

        # ???
        self.serial.dsrdtr = 1
        self.serial.xonxoff = 1
        self.serial.write(serial.XON)
        self.serial.write(serial.XOFF)
        self.serial.setRTS(True)
        self.serial.setDTR(True)
        # /???
        return True
