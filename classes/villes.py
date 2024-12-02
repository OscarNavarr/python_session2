import sqlite3


class Villes:

    def insertVille(self, cursor, connection, departement, ville, code_postal, population, superficie):
        status = False
        try:
           cursor.execute('''INSERT INTO Ville (departement, ville, code_postal, population, superficie) 
                            VALUES (?, ?, ?, ?, ?)''', (departement, ville, code_postal, population, superficie))
           connection.commit()

           status = True
        except sqlite3.Error as error:
            status = False
            print('Error while inserting data into Ville table', error)

        finally:
            return status

    def updateValueByDep(self, cursor, column_name, value, departement):
        try:
            cursor.execute(f'UPDATE Ville SET {column_name} = ? WHERE departement = ?', (value, departement))
        except sqlite3.Error as error:
            print('Error while updating data in Ville table by departement', error)


    def getAllVilles(self, cursor):
        try:
            cursor.execute('SELECT * FROM Ville')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Ville table', error)

    def getVilleByDep(self, cursor, departement):
        try:
            cursor.execute('SELECT * FROM Ville WHERE departement = ?', (departement,))
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Ville table by departement', error)

    # Aumenter le nom des habitants de la ville de Paris et banlieue
    def updatePopulationVilleParisTo5Percent(self, cursor):
        try:
            cursor.execute('''UPDATE Ville SET population = trunc(population*1.05) WHERE departement IN ('75','91','92','93','94','95') ''')
        except sqlite3.Error as error:
            print('Error while updating data in Ville table by departement', error)

    # dupliquer les villes de corse (chaque ville sera deux fois dans la base)
    def duplicateVillesCorse(self, cursor):
        try:
            cursor.execute('''INSERT INTO Ville (departement, ville, code_postal, population, superficie) 
                            SELECT departement, ville, code_postal, population, superficie FROM Ville WHERE departement IN  ('2A','2B')''')
        except sqlite3.Error as error:
            print('Error while duplicating data in Ville table', error)

    # supprimer les doublons (villes en double ou plus) de la table ville
    def deleteDuplicateVilles(self, cursor):
        try:
            cursor.execute('''DELETE FROM  Ville WHERE id NOT IN 
                                ( SELECT max(id) FROM Ville GROUP BY ville)''')
        except sqlite3.Error as error:
            print('Error while deleting duplicate data in Ville table', error)