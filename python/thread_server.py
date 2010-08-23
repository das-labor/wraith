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
        server.register_function(i.disconnect,i.getName() + ".disconnect")
        server.register_function(i.connect,i.getName() + ".connect")
        server.register_function(i.reconnect,i.getName() + ".reconnect")
        server.register_function(i.configureConnection,i.getName() + ".configureConnection")
        server.register_function(i.gotoHome,i.getName() + ".gotoHome")
        server.register_function(i.moveToPos,i.getName() + ".moveToPos")
        server.register_function(i.moveInc,i.getName() + ".moveInc")
        server.register_function(i.getCurPos,i.getName() + ".getCurPos")
        server.register_function(i.closeClaw,i.getName() + ".closeClaw")
        server.register_function(i.openClaw,i.getName() + ".openClaw")
        server.register_function(i.rawCommand,i.getName() + ".rawCommand")
        server.register_function(i.reset,i.getName() + ".reset")
        server.register_function(i.setSpeed,i.getName() + ".setSpeed")
        server.register_function(i.getSpeed,i.getName() + ".getSpeed")
        server.register_function(i.hasError,i.getName() + ".hasError")
        server.register_function(i.test,i.getName() + ".test")
        
    print "running"
    server.serve_forever()

if __name__ == "__main__":
    main()
    
    
            
        
    
