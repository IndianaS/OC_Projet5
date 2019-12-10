
class DbReading:

    def __init__(self, connection):
        self.connect = connection

    def get_all_categories(self):
        cursor = self.connect.create_cursor()
        cursor.execute('USE openfood')

        query = """SELECT * FROM category"""

        cursor.execute(query)

        for category in cursor.fetchall():
            print(category)

    def get_category_products(self, id_category):
        cursor = self.connect.create_cursor()
        query = """SELECT product.id, product.product_name_fr FROM openfood.product WHERE product.id_category = %s LIMIT 30"""

        cursor.execute(query, (id_category,))

        rows = cursor.fetchall()

        product_infos = []
        for index, product in enumerate(rows):
            dico = {"index": index,
                    "product_name_fr": product[1], "id": product[0]}
            product_infos.append(dico)
            print(dico)
