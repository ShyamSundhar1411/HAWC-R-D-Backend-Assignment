# How to Run The Project
1. Install poetry through pip
      '''python
            pip install poetry
      '''
 2. Install Dependencies in the project folder by running the following command(On the project folder)
      '''
        poetry install
      '''
 3. After Installing Dependencies inside the project folder Run migrations
     '''
     python
     py manage.py makemigrations
     py manage.py migrate
     '''
 4. Load the sample data given with the repository
    '''
      py manage.py loaddata data.json
    '''
 5. Run the server in local environment
    '''
    py manage.py runserver
    '''
   
