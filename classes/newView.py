import sqlite3

class NewView:

    # Create a view to show the Hauts-de-France region
    def create_view_hauts_de_france(self, cursor):
        try:
            cursor.execute('''
                CREATE VIEW IF NOT EXISTS HautsDeFrance AS
                SELECT * FROM Departement WHERE region = "Hauts-de-France"
                ''')
        except sqlite3.Error as error:
            print('Error while creating the view', error)