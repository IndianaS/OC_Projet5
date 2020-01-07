from controller.interface import Interface
from models.bdd.connection import Connection


auth = Connection()
auth.connect()

application = Interface(auth)
application.loop()
