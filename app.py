from controller.interface import Interface
from models.bdd.connection import Connection

def main():
    auth = Connection()
    auth.connect()

    application = Interface(auth)
    application.loop()

if __name__ == "__main__":
    main()
