import serial
import sys
import time
import random

from interface import RobotBasicInterface

class MoveMasterDriver(RobotBasicInterface):
    joint={
        'body': { 'min': -12000, 'max': 0},
        'shoulder': {'min': -5200, 'max': 0},
        'elbow': {'min': 0, 'max': 3600},
        'writh_l': { 'min':-4800, 'max': 4800},
        'writh_r': { 'min': -4800, 'max': 4800}
        }

    # from nest - assumed need to verify that
    position={
        'body': 0,
        'shoulder': 0,
        'elbow': 0,
        'writh_l': 0,
        'writh_r': 0
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

    # have something to blacklist some positions
    blacklist=[]

    # the "SyntaxError: lambda cannot contain assignment"-Problem
    def __assignvalue(self,x,y):
        x=y
        
    def __sendCMD(self,CMD="TI 0"):
        """
        Function to send commands to the Robot
        if there is no command we send a command to wait 0.1 seconds
        to the Robot.
        """
        # debug
        print CMD
        if self.serial.isOpen():
            self.serial.write("%s"  % CMD[0])

        self.serial.write("%s\r\n" % CMD[1:])
        self.serial.flush()

        # wait to complete
        while not self.serial.getCTS():
            time.sleep(0.05)

        return True

    def __inrange(self,x,y,z):
        if (int(x) <= int(z)) and (int(y)>=int(z)):
            return True
        return False
        

    def moveInc(self,engList={}):
        """
        move relativ from the current position
        """
        #check for supplied engine names
        tmp=list(set(map(lambda x: self.position.has_key(x[0]),engList.items())))
        if len(tmp) >1:
            return False
        if not tmp[0]:
            return False

        # check for valid data - do we break any ranges?
        tmp=map(lambda x: (x[0],self.position[x[0]]+int(x[1])),engList.items())
        tmp=list(set(map(lambda x: self.__inrange(self.joint[x[0]]["min"],self.joint[x[0]]["max"],x[1]),tmp)))
        if len(tmp) >1:
            return False
        if not tmp[0]:
            return False
        
        # okay seams to be in range - constructing command
        engmove = {}
        for i in map(lambda x: (x[0],0),self.position.items()):
            engmove[i[0]]=i[1]

        for i in engList.items():
            engmove[i[0]]=i[1]
        cmd="MI %s, %s, %s, %s, %s, 0" % (str(engmove["body"]), str(engmove["shoulder"]), str(engmove["elbow"]),str(engmove["writh_l"]),str(engmove["writh_r"]))

        # sending command
        self.__sendCMD(cmd)

        # position update
        for i in engList.items():
            self.position[i[0]]+= int(i[1])


        return True

    def moveToPos(self,engList={}):
        """
        move to the defined position
        """
        # get the difference to the current position and move
        # via moveInc
        tmp=list(set(map(lambda x: self.position.has_key(x[0]),engList.items())))
        if len(tmp) >1:
            return False
        if not tmp[0]:
            return False

        tmp = map(lambda x: (x[0],str(int(x[1])-self.position[x[0]])),engList.items())
        diffmove = {}
        for i in tmp:
            diffmove[i[0]]=i[1]

        return self.moveInc(diffmove)

    def getCurPos(self):
        return self.position

    def rawCommand(self,cmd):
        return self.__sendCMD(cmd)

    def __init__(self):
        self.serial=serial.Serial()
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
        map(self.__assignvalue(configuration[x[0]],x[1]),options)
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


if __name__ == "__main__":
    driver=MoveMasterDriver()
#    driver.connect()
#    print driver.getCurPos()
#    driver.rawCommand("RS")
#    driver.rawCommand("SP 9")
#    driver.rawCommand("NT")
    driver.moveInc({'body': "-1000",'shoulder': '-300','elbow':'360','writh_l':'240','writh_r':'240'})
    driver.moveToPos({'body': "0",'shoulder': '0','elbow':'0','writh_l':'0','writh_r':'0'})

#    driver.disconnect()
