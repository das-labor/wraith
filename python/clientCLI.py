import sys
import code
import xmlrpclib

r = xmlrpclib.ServerProxy(sys.argv[1])

bannertxt  = "===============================\n"
bannertxt += "available commands with r object: \n"
bannertxt += str(r.system.listMethods()) + "\n"
bannertxt += " for example: r.setSpeed(9)\n"
bannertxt += "===============================\n"

# launch interactive shell
code.interact(banner = bannertxt, local = locals())
