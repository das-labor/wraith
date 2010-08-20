class RobotBasicInterface(Object):
    """
    Basic Funktionen die alle Roboter ausfuehren koennen muessen
    """
    def connect(self):
        """
        Verbinde dich mit dem Robot
        """
        pass

    def disconnect(self):
        """
        Verbindung zum Robot loesen (Die Verbindung kann nur konfiguriert werden
        wenn die Verbindung geschlossen wurde
        """
        pass

    def reconnect(self):
        """
        Verbindung zum Robot abbauen und wieder aufbauen. Dabei aendert
        sich die Konfiguration der Verbindung nicht
        """
        pass
    
    def configureConnection(self,options={}):
        """
        Der Driver hat eine Verbindung, die evt Parameter benoetigt
        """
        pass
        
    def moveToPos(self,engList=[]):
        """
        bewege Motoren zu einer spez. Position
        """
        pass

    def moveInc(self,engList=[]):
        """
        bewege Motoren von der aktuellen Position um die
        angegebenen Werte weiter
        """
        pass

    def getCurPos(self):
        """
        gebe aktuelle Position aus
        """
        pass

    def openClaw(self):
        """
        oeffne die Hand
        """
        pass

    def closeClaw(self):
        """
        schliesse die Hand
        """
        pass

    def rawCommand(self,cmd=""):
        """
        sende ein Kommando raw an das device
        """
        pass

    def reset(self):
        """
        sende Reset Command an den Bot und faehrt in sichere Position (NT)
        """
        pass

    def setSpeed(self,speed=0):
        """
        setzt die Geschwindigkeit des Roboters
        """
        pass

    def getSpeed(self):
        """
        liefert die aktuelle Geschwindigkeit des Roboters
        """
        pass

    def hasError(self):
        """
        wenn ein Fehler aufgetreten ist, liefert diese
        Funktion 'True' sonst 'False'
        """
        pass
