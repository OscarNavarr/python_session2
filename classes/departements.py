import sqlite3

class Departements:

    def insertDepartements(self, cursor, connection, numero, nom, region, superficie, dec, population):
        status = False
        try:
            cursor.execute('''INSERT INTO Departement (numero, nom, region, superficie, dec, population) 
                            VALUES (?, ?, ?, ?, ?, ?)''', (numero, nom, region, superficie, dec, population))
            connection.commit()

            status = True
        except sqlite3.Error as error:
            status = False
            print('Error while inserting data into Departement table', error)

        finally:
            return status

    def getAllDepartements(self, cursor):
        try:
            cursor.execute('SELECT * FROM Departement')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Departement table', error)


    #  mettre à jour le nombre d'habitants de la table départements depuis la
    # somme des nombres d’habitants de la table ville
    def updatePopulationDepartements(self, cursor):
        try:
            cursor.execute('''UPDATE Departement SET population = (SELECT sum(population) FROM Ville WHERE departement = numero) ''')
        except sqlite3.Error as error:
            print('Error while updating data in Departement table', error)

    '''
        re-mettre à jour le nombre d'habitants de la table départements depuis la
        somme des nombres d’habitants de la table ville
    '''
    def updatePopulationDepartements(self, cursor):
        try:
            cursor.execute('''UPDATE Departement SET population = (SELECT sum(population) FROM Ville WHERE departement = numero) ''')
        except sqlite3.Error as error:
            print('Error while updating data in Departement table', error)