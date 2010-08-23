#!/usb/bin/env python

import sys
import time
import threading
import Queue
from types import *
from interface import RobotBasicInterface
from MoveMasterDriver import MoveMasterDriver
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RoboThread(threading.Thread):
    """
    thread object for Robots
    """
    def run(self):
        self.connect()
        while True:
            tmp=self.queue.get()
            if not tmp.has_key("args"):
                if tmp.has_key("function"):
                    tmp["function"]()
            else:
                if tmp.has_key("function"):
                    tmp["function"](tmp["args"])

    def __init__(self,robotinterface,queue_size=100):
        self.queue=Queue.Queue(queue_size)
        self.robot=robotinterface
        threading.Thread.__init__ ( self )

    # wrapper functions
    def disconnect(self):
        self.queue.put({'function':self.robot.disconnect})

    def connect(self):
        self.queue.put({'function':self.robot.connect})

    def reconnect(self):
        self.queue.put({'function':self.robot.reconnect})

    def configureConnection(self,options={}):
        self.queue.put({'function':self.robot.configureConnection, 'args':options})
    def gotoHome(self):
        self.queue.put({'function':self.robot.gotoHome})

    def moveToPos(self,engList={}):
        self.queue.put({'function':self.robot.moveToPos, 'args':engList})

    def moveInc(self,engList={}):
        self.queue.put({'function':self.robot.moveInc, 'args':engList})

    def getCurPos(self):
        self.queue.put({'function':self.robot.getCurPos})

    def closeClaw(self):
        self.queue.put({'function':self.robot.closeClaw})

    def openClaw(self):
        self.queue.put({'function':self.robot.openClaw})

    def rawCommand(self,cmd=""):
        self.queue.put({'function':self.robot.rawCommand,'args':cmd})

    def reset(self):
        self.queue.put({'function':self.robot.reset})

    def setSpeed(self,speed=5):
        self.queue.put({'function':self.robot.setSpeed,'args':speed})

    def getSpeed(self):
        self.queue.put({'function':self.robot.getSpeed})

    def hasError(self):
        self.queue.put({'function':self.robot.hasError})

    def test(self):
        self.queue.put({'function':self.robot.test})


def main ():

    dummy=RoboThread(RobotBasicInterface())
    dummy.setName("dummy")
    # configure MoveMasterDriver
    movemasterthread=RoboThread(MoveMasterDriver())
    movemasterthread.configureConnection({'port':'/dev/ttyUSB0'})
    movemasterthread.setName("MoveMasterII")

    # list all configured drivers
    worlddomination=[movemasterthread,dummy]

    # starting xml-rpc-Server
    server = SimpleXMLRPCServer(("0.0.0.0",8000), allow_none=True, logRequests=True)
    server.register_introspection_functions()

    # setting threads to background starting threads
    # and register them at XMLRPCServer
    for i in worlddomination:
        i.daemon=True
        i.start()
        # someone may write some metaprogramming for this block!
        for j in filter(lambda x: not (x.startswith("__") or x.endswith("__")),dir(RobotBasicInterface)):
            server.register_function(eval('i.'+j),i.getName()+"."+j)

    print "running"
    server.serve_forever()

if __name__ == "__main__":
    main()
    
    
            
        
    
