import sqlite3

def create_database():
    connection = None
    try:
        # Create a database connection
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Create a table Ville
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ville (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                departement INTEGER,
                ville TEXT,
                code_postal INTEGER,
                population INTEGER,
                superficie INTEGER
            )
        ''')

        # Create a table Departement
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Departement (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER,
                nom TEXT,
                region TEXT,
                superficie INTEGER,
                dec INTEGER,
                population INTEGER
            )
        ''')

        # Create a table Region
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Region (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                superficie INTEGER,
                population INTEGER
            )
        ''')

        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS newVille (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                departement INTEGER NOT NULL,
                ville TEXT,
                code_postal INTEGER,
                population INTEGER,
                superficie FLOAT
            );

            INSERT INTO newVille (departement, ville, code_postal, population, superficie)
            SELECT departement, ville, code_postal, hab, superficie FROM Villes;
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS MODIFICATIONS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE,
                table_name TEXT
                );
        ''')


        # Use vacuum to clean up the database
        cursor.execute('VACUUM')


        # Commit changes
        connection.commit()

    except sqlite3.Error as error:
        print("Error while creating the database:", error)

    finally:
        if connection:
            # Return the connection and cursor for further use
            return connection, cursor
        else:
            print("Failed to establish database connection.")
            return None, None
