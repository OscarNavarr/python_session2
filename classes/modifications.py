import sqlite3
class Modifications:

    def createModificationsTrigger(self, cursor):
        try:
            cursor.execute(''''
                CREATE TRIGGER IF NOT EXIST modify_modifications
                AFTER UPDATE Villes BEGIN(INSERT INTO modifications (date, table_name) VALUES (datetime('now'), 'Villes'); END;
            ''')
        except sqlite3.Error as error:
            print('Error while creating trigger', error)