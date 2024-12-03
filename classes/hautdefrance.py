import sqlite3


class HautDeFrance:

    def createTableHautDeFrance(self, cursor):
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS HautDeFrance AS SELECT * FROM Ville WHERE departement IN ('02','59','60','62','80')''')
        except sqlite3.Error as error:
            print('Error while creating HautDeFrance table', error)


    def deleteTableHautDeFrance(self, cursor):
        try:
            cursor.execute('''DROP TABLE IF EXISTS HautDeFrance''')
        except sqlite3.Error as error:
            print('Error while deleting HautDeFrance table', error)