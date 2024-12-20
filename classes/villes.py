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

    def createTrigger(self,cursor):
        try:
            cursor.execute('''CREATE TRIGGER IF NOT EXISTS modify_pop_ville
                        AFTER UPDATE OF population ON Ville BEGIN UPDATE Departement SET population = (
                            SELECT sum(population) FROM Ville WHERE departement = numero
                            ) WHERE numero = departement; END;''')
        except sqlite3.Error as error:
            print('Error while creating trigger', error)


    # Change the Ville
    def changeTableVilleToVilles(self, cursor, newTableName):
        try:
            query = f"ALTER TABLE Ville RENAME TO {newTableName}"
            cursor.execute(query)
            print(f"Table renamed to {newTableName}")
        except sqlite3.Error as error:
            print("Error while changing table name:", error)

    # Change the population column name
    def changePopulationColumnName(self, cursor, newColumnName):
        try:
            query = f"ALTER TABLE Villes RENAME COLUMN population TO {newColumnName}"
            cursor.execute(query)
            print(f"Column name changed to {newColumnName}")
        except sqlite3.Error as error:
            print('Error while changing column name', error)

    def getDataFromPasDeCalais(self, cursor):
        try:
            cursor.execute('SELECT * FROM Ville WHERE departement = 62')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Ville table by departement', error)

    def createIndexByDepartement(self, cursor):
        try:
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_departement ON Ville(departement)')
        except sqlite3.Error as error:
            print('Error while creating index', error)

    def showVillesThatHaveAWords(self, cursor, word):
        try:
            cursor.execute('SELECT * FROM Villes WHERE ville LIKE ?', (f'%{word}%',))
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Ville table by word', error)

    def getVilleByHisDepNameIgualToFourLetters(self, cursor):
        try:
            cursor.execute('SELECT * FROM Villes WHERE length(ville) = 4')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('Error while fetching data from Ville table by word', error)

    def createDateColumn(self, cursor):
        try:
            cursor.execute('ALTER TABLE Villes ADD COLUMN date TEXT DEFAULT "2012-01-01" ')
        except sqlite3.Error as error:
            print('Error while creating date column', error)