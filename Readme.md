# - Project 5 OC

# - Description:
- The program will display a product management system, operating from the terminal, without a graphical interface.

# - Menu:
- In a menu, the user will have several choices, display categories, display favorites or quit.
- After selection by the user the program will display a list of data stored in db.
- The user can select a product from a list, then display the substitutes for the product.
- The user will be able to register the products, then display the product sheet via a url link.

- At any time, when the program offers a choice menu, the user can return to the previous menu or exit the program.


# - Installation recommendations:
- MariaDB (or MySQL)
- Create a user for the project.

# - 1: Initializing a db:
- 1: To initialize the virtual environment: pipenv install
- 2: To position yourself in pipenv: pipenv shell
- 3: The user must rename settings.py.example to settings.py and indicate the login and password of the database.
- 4: For initializing a db: python installdb.py

# - 2: Project run:
- : If you have already initialized the virtual environment to download the data.
- 1: To run the app: python app.py
