class RobotBasicInterface(object):
    """
    Basic Funktionen die alle Roboter ausfuehren koennen muessen
    """
    def connect(self):
        """
        Verbinde dich mit dem Robot
        """
        print "connect called"
        pass

    def disconnect(self):
        """
        Verbindung zum Robot loesen (Die Verbindung kann nur konfiguriert werden
        wenn die Verbindung geschlossen wurde
        """
        print "disconnect called"
        pass

    def reconnect(self):
        """
        Verbindung zum Robot abbauen und wieder aufbauen. Dabei aendert
        sich die Konfiguration der Verbindung nicht
        """
        print "reconnect called"
        pass
    
    def configureConnection(self,options={}):
        """
        Der Driver hat eine Verbindung, die evt Parameter benoetigt.
        Ist der Driver gerade verbunden, wird die verbindung beendet
        und nicht wieder aufgebaut. Configure beendet also die
        Verbindung wenn sie offen ist
        """
        print "configure connection with args: " + str(options) + " called"
        pass
        
    def gotoHome(self):
        """
        bewege den Robot zu der definierten HomePostition
        """
        print "gotoHome called"
        pass
    
    def moveToPos(self,engList={}):
        """
        bewege Motoren zu einer spez. Position
        """
        print "moveToPos called with args: " + str(engList) + " called"
        pass

    def moveInc(self,engList={}):
        """
        bewege Motoren von der aktuellen Position um die
        angegebenen Werte weiter
        """
        print "moveInc called with args: " + str(engList) + " called"
        pass

    def getCurPos(self):
        """
        gebe aktuelle Position aus
        """
        print "getCurPos called"
        pass

    def openClaw(self):
        """
        oeffne die Hand
        """
        print "openClaw called"
        pass

    def closeClaw(self):
        """
        schliesse die Hand
        """
        print "closeClaw called"
        pass

    def rawCommand(self,cmd=""):
        """
        sende ein Kommando raw an das device
        """
        print "rawCommand with args: " + str(cmd) + " called"
        pass

    def reset(self):
        """
        sende Reset Command an den Bot und faehrt in sichere Position (NT)
        """
        print "reset called"
        pass

    def setSpeed(self,speed=0):
        """
        setzt die Geschwindigkeit des Roboters
        """
        print "setSpeed with args " + str(speed) + " called"
        pass

    def getSpeed(self):
        """
        liefert die aktuelle Geschwindigkeit des Roboters
        """
        print "getSpeed called"
        pass

    def hasError(self):
        """
        wenn ein Fehler aufgetreten ist, liefert diese
        Funktion 'True' sonst 'False'
        """
        print "hasError called"
        pass

    def test(self):
        """
        Fuehre eine testsquenz aus - Verbindung und Bewegung
        """
        print "test called"
        pass
