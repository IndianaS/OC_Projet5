import logging

import mysql.connector

from settings.settings import database, host, password, user

logging.basicConfig(filename='app.log', level=logging.INFO)


class Connection:
    """Class connection db"""

    def __init__(self):
        """Connection information"""
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        """Connection method"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

        except mysql.connector.Error as error:
            logging.warning(error)

    def create_cursor(self):
        return self.connection.cursor()

    def commit(self):
        return self.connection.commit()
