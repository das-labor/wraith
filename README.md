# Wraith

Wraith is an xmlrpc server based on python - I may should drop in some words like multithread, queue, noneblocking blablabla ;). It consists of the server (thread_server.py) some drivers (*Driver.py) and a commandline client (clientCLI.py).

## getting it run

* edit the sources of `thread_server.py` to set the serialport for the drivers (currently its the only way to change the ports).
* Start the server `python thread_server.py` - every module should get initialized - the connected robots will go to their defaultposition (Home)
* connect the client to the server `pythen clientCLI.py http://localhost:8000`
* command the Robots (siehe 'Funktionsuebersicht')

## devel

* It sould be relativ easy to define new robots. Just implement a new driver (see MoveMasterDriver) - currently there is no backchannel for the robots.
* the gerneral Interface is located in `interface.py`
* the recent source is located at https://www.das-labor.org/usersvn/wraith (GPL v2+)
* to contact Asklepios or Tdev join the jabberchannel labor@conference.das-labor.org  or write a mail to the discuss@das-labor.org (mailinglist)

# Compiling

0. get dependencies shipped by OS:

 * Ogre >= 1.6

1. svn co
```
svn co https://www.das-labor.org/usersvn/wraith/trunk/ wraith-trunk
```

2. compile Bullet:
```
cd wraith-trunk/source/dependencies
cd bullet-2.77
sh autogen.sh
./configure
make -j3
sudo make install
cd ..
```

3. compile OgreBullet:
```
cd ogrebullet
sh autogen.sh
./configure
make -j3
sudo make install
cd ..
```

4. compile WRAITH-SIM
```
cd wraith-trunk/source/sim
cmake .
make -j3
```

5. run the sim
```
cd wraith-trunk/source/sim/bin
./wraith_sim
```

# Funktionsübersicht

Der Server wird mit Hilfe des Clients gesteuert. Folgende Funktionen werden fuer den einzelnen Roboter durch den Server erreichbar gemacht:

## connect
Server soll Verbindung mit dem Roboter aufnehmen - hierbei wird der Roboter (so noch nicht verbunden) in seine Homeposition gebracht
```
r.MoveMasterII.connect()
```
## disconnect ##
Server baut die Verbindung zum Roboter ab
```
r.MoveMasterII.disconnect()
```
## reconnect ##
Die Verbindung zum Roboter wird erst abgebaut und dann wieder aufgebaut
```
r.MoveMasterII.reconnect()
```

## configureConnection ##
Wenn die Verbindung abgebaut wurde, laesst sich hierdurch die Verbindung neu konfigurieren. Dies ist fuer jede Verbindungsart unterschiedlich. Ist der Server gerade mit dem Roboter verbunden, wird die verbindung voerher abgebaut und nach dem configure nicht wieder aufgebaut. Hier fuer ist dann ein Connect notwendig. Fuer die seriele Verbindung des MoveMasterII sind folgende Optionen moeglich:
 * port
 * baudrate
 * bytesize
 * parity
 * stopbits
 * timeout
 * writeTimeout
 * xonxoff
 * rtscts
 * dsrdtr
fuer genauer doku bitte in das serial-module von python schauen.

```
r.MoveMasterII.configureConnection({'port':'/dev/ttyUSB0'})
```

## gotoHome ##
Bringt den Roboter egal von welcher Position in seine Nulllage
```
r.MoveMasterII.gotoHome()
```

## moveToPos ##
bewegt den Roboter zu einer absoluten Position. Die Minimal und maximalwerte sind dabei von der eingestellten HomePosition abhaengig. Im moment ist dies folgede range
 * body: -6000 bis 6000
 * shoulder: -2600 bis 2600
 * elbow: -1800 bis 1800
 * writh_l: -6380 bis 3220
 * writh_r: -3980 bis 5620

```
r.MoveMasterII.moveToPos({'body':-3000,'shoulder':1000,'elbow':200})
```

## moveInc ##
bewegt den Roboter incrementel. Hierbei duerfen die Ranges nicht ueberschritten werden (s. moveToPos)

```
r.MoveMasterII.moveInc({'body':-3000,'shoulder':1000,'elbow':200})
```

## getCurPos ##
soll die aktuelle Position liefer - im moment nicht implementiert
```
r.MoveMasterII.getCurPos()
```

## openClaw ##
Macht die Hand auf
```
r.MoveMasterII.openClaw()
```

## closeClaw ##
Macht die Hand zu
```
r.MoveMasterII.closeClaw()
```

## rawCommand ##
sendet ein raw Command an den Robot. Hierfuer bitte /doku/MoveMaster2/Mitsubishi Robot Manual RM-501.pdf lesen - '''Warnung''' danach ist evt ein reconnect notwendig, weil diese Befehle nicht vom Treiber erfasst werden
```
r.MoveMasterII.rawCommand('NT')
```

## reset ##
resetet den Robot. Etwaige aufgetretene Fehler werden behoben (so moeglich) und der Robot wird in seine HomePosition gefahren.
```
r.MoveMasterII.reset()
```
## setSpeed ##
Die Geschwindigkeit einstellen mit der sich der Robot bewegen soll. Hierbei sind werte zwischen 0 und 9 moeglich
```
r.MoveMasterII.setSpeed(5)
```

## getSpeed ##
Liefert die aktuell eingestellte Geschwindigkeit - im moment nicht implementiert
```
r.MoveMasterII.getSpeed()
```

## hasError ##
Gibt info darueber, ob ein Fehler aufgetreten ist - im Moment nicht implementiert - beim MoveMasterII blinkt dann einfach die rote Lampe
```
r.MoveMasterII.hasError()
```

## test ##
Fuehrt einen Achsentest durch - '''Warnung''' hier fuer wird recht viel Platz benoetigt
```
r.MoveMasterII.test()
```

## Beispielsession1 ##
```
r.MoveMasterII.connect()
r.MoveMasterII.test()
r.MoveMasterII.gotoHome()
r.MoveMasterII.moveToPos({'body':200, 'shoulder': 4000})
```
der letzte Befehl wird nicht ausgefuehrt, da es ausserhalb der Range ist (s.O.) - der Robot bleibt aber Funktional

## Beispielsession2 ##
```
r.MoveMasterII.connect()
r.gotoHome()
r.MoveMasterII.moveToPos({'shoulder': -2500})
```
der letzte Befehl wird ausgefuehrt, der Roboter blockiert die ausfuehrung jedoch durch seinen eigenen Koerper (oder ein anderes geraet was im Weg ist) - hier kann reset ausgefuehrt werden - sollte dies nicht Helfen, muss der Roboter ausgeschaltet und wieder eingeschaltet werden.
```
r.MoveMasterII.reset()
```

## Anmerkung ##
 * Normal ist es nicht notwendig die verbindung zum Robot zu konfigurieren, da dies der server initial tut
 * wenn mehrere Robots angeschlossen sind, koennen diese nahezu gleichzeitig gesteuert werden. Man muss also nicht warten, bis ein Robot seinen Befehl beendet hat. Beispiel:
```
r.MoveMasterII.gotoHome()
r.BlueBot.gotoHome()
```
