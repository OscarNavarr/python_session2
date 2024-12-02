def get_data_information():

    data_ville = open('./data/villes.txt', 'r')
    data_ville_content = data_ville.read()                  # Read the content of the file: data/villes.txt

    data_departement = open('./data/departements.txt', 'r')
    data_departement_content = data_departement.read()      # Read the content of the file: data/departements.txt


    #Transform the content of the file into a list
    data_ville_list = data_ville_content.split('\n')
    data_departement_list = data_departement_content.split('\n')

    # Delete the first element of the list
    data_ville_list.pop(0)
    data_departement_list.pop(0)

    # Split the list into a list of lists
    data_ville_list = [element.split(',') for element in data_ville_list]
    data_departement_list = [element.split(',') for element in data_departement_list]

    return data_ville_list, data_departement_list