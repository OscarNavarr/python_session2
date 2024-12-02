from SQL import create_db
from helpers import getDataInformation as data
from classes import villes
from classes import departements
import numpy as np

def main():
    connection, cursor = create_db.create_database()

    class_ville = villes.Villes()
    class_departement = departements.Departements()

    data_ville_list, data_departement_list = data.get_data_information()

    '''
        INSERT DATA INTO VILLES TABLE
    '''
    #for data_ville in data_ville_list:
        #if(len(data_ville) > 0):
            #class_ville.insertVille(cursor, connection, data_ville[0], data_ville[1], data_ville[2], data_ville[3], data_ville[4])

    '''
        INSERT DATA INTO DEPARTMENTS TABLE
    '''
    #for data_departement in data_departement_list:
        #if(len(data_departement) > 0):
            #class_departement.insertDepartements(cursor, connection, data_departement[0], data_departement[1], data_departement[2], data_departement[3], data_departement[4], data_departement[5])


    all_villes = class_ville.getAllVilles(cursor)                           # Get all the data from the Ville table
    all_departements = class_departement.getAllDepartements(cursor)         # Get all the data from the Departement table

    # UPDATE PEOPLE NUMBER BY DEPARTMENT
    class_ville.updateValueByDep(cursor, 'population', 8900, 62)

    # Get the data from the Ville table by departement
    villeDeLeforest = class_ville.getVilleByDep(cursor, 62)


    # Increase the population number in Paris and suburbs by 5%
        #class_ville.updatePopulationVilleParisTo5Percent(cursor)

    # Update the number of inhabitants of the department table from the sum of the number of inhabitants of the city table
        #class_departement.updatePopulationDepartements(cursor)

    # Duplicate the cities of Corsica (each city will be twice in the database)
        #class_ville.duplicateVillesCorse(cursor)

    # Delete duplicates (cities in double or more) from the city table
        #class_ville.deleteDuplicateVilles(cursor)

    # Update the number of inhabitants of the department table from the sum of the number of inhabitants of the city table
    class_departement.updatePopulationDepartements(cursor)

    connection.close()
if __name__ == '__main__':
    main()
