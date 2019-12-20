from models.bdd.connection import Connection
from models.bdd.dbadd import DbAdd
from models.bdd.dbcreate import DbCreate
from models.bdd.dbreading import DbReading
from models.categorydownloader import CategoryDownloader
from models.productdownload import ProductDownloader
from settings.settings import category_list, keywords
from views.display import Display

from controller.interface import Interface

auth = Connection()
auth.connect()

"""
# Creation of the comic, creation of the tables
create_db = DbCreate(auth)
print('On crée la base de données !')
create_db.create_database()
print('On crée les tables !')
create_db.create_table()

# Download the categories then the ranges
category = CategoryDownloader()
print('On télécharge les catégories et les produits !')
all_categories = category.get_category()

add_db = DbAdd(auth)
# Add the categories to the database

print('On ajoute les catégories en base de données !')
add_db.add_category(all_categories)
print('On ajoute les produits de chaque catégorie en base de données !')
add_db.add_product(all_categories)

"""
test = Interface(auth)

test.loop()

"""
> L'utilisateur lance le programme:
$ Le programme propose un menu
- Choix d'une categorie 
- Choix voir les favoris
"""
