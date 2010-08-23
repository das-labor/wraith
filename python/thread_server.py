#!/usb/bin/env python

import sys
import time
import threading
import Queue
from interface import RobotBasicInterface
from MoveMasterDriver import MoveMasterDriver
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RoboThread(threading.Thread):
    """
    thread object for Robots
    """
    def __init__ ( self, queue ):
        self.queue = queue
        threading.Thread.__init__ ( self )

    def run(self):
        while True:
            tmp=self.queue.get()
            if not tmp.has_key("args"):
                if tmp.has_key("function"):
                    tmp["function"]()
            else:
                if tmp.has_key("function"):
                    tmp["function"](tmp["args"])

    def __init__(self,queue_size=100,robotinterface=RobotBasicInterface()):
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
    server = SimpleXMLRPCServer(("0.0.0.0",8000), allow_none=True)
    server.register_introspection_functions()

    # connecting threads / queues / drivers
    worlddomination=[RoboThread(100,MoveMasterDriver())]

    # setting threads to background starting threads
    # and register them at XMLRPCServer
    for i in worlddomination:
        i.daemon=True
        i.start()
        server.register_instance(i)

    print "running"
    server.serve_forever()

if __name__ == "__main__":
    main()
    
    
            
        
    
