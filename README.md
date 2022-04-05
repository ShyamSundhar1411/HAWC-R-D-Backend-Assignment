# How to Run The Project
1. Install poetry through pip
      *  ``` pip install poetry ```
 2. Install Dependencies in the project folder by running the following command(On the project folder)
      * ``` poetry install ```
 3. After Installing Dependencies inside the project folder Run migrations
     * ``` py manage.py makemigrations ```
 4. Load the sample data given with the repository
    * ``` py manage.py loaddata data.json ```
 5. Run the server in local environment
    * ``` py manage.py runserver ```
   
