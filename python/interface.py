class RobotBasicInterface:
    """
    Basic Funktionen die alle Roboter ausfuehren koennen muessen
    """
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
