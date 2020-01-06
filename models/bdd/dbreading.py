from models.product import Product


class DbReading:

    def __init__(self, connection):
        self.connect = connection

    def get_all_categories(self):
        cursor = self.connect.create_cursor()
        cursor.execute('USE openfood')

        query = """SELECT * FROM category ORDER BY category.id"""

        cursor.execute(query)

        return cursor.fetchall()

    def get_category_products(self, id_category):
        cursor = self.connect.create_cursor()
        query = """
            SELECT 
                product.id, 
                product.product_name_fr,
                product.id_category,
                product.brands,
                product.nutrition_grade_fr
            FROM 
                openfood.product 
            WHERE 
                product.id_category = %s LIMIT 50
                """

        cursor.execute(query, (id_category,))

        data = cursor.fetchall()

        products = []
        for id, name, id_category, brands, nutrition_grade_fr in data:
            products.append(
                Product(
                    product_name_fr=name,
                    nutrition_grade_fr=nutrition_grade_fr,
                    id=id,
                    brands=brands,
                    id_category=id_category,
                )
            )

        return products

    def get_product(self, id):
        cursor = self.connect.create_cursor()
        query = """
                SELECT 
                    product.id, 
                    product.product_name_fr,
                    product.id_category,
                    product.brands,
                    product.nutrition_grade_fr
                FROM 
                    openfood.product
                WHERE
                    product.id = %s
                """
        cursor.execute(query, (id,))
        id, name, id_category, brands, nutrition_grade_fr = cursor.fetchone()

        return Product(
                    product_name_fr=name,
                    nutrition_grade_fr=nutrition_grade_fr,
                    id=id,
                    brands=brands,
                    id_category=id_category,
                    )

    def get_substitute(self, product):
        cursor = self.connect.create_cursor()
        query = """
                SELECT 
                    product.id, 
                    product.product_name_fr,
                    product.id_category,
                    product.brands,
                    product.nutrition_grade_fr
                FROM
                    openfood.product
                WHERE
                    product.id_category = %s AND
                    product.nutrition_grade_fr < %s
                ORDER BY product.nutrition_grade_fr
                LIMIT 10
                """

        cursor.execute(query, (product.id_category, product.nutrition_grade_fr,))
        
        data = cursor.fetchall()

        products = []
        for id, name, id_category, brands, nutrition_grade_fr in data:
            products.append(
                Product(
                    product_name_fr=name,
                    nutrition_grade_fr=nutrition_grade_fr,
                    id=id,
                    brands=brands,
                    id_category=id_category,
                )
            )

        return products

    def get_favorite(self, product):
        cursor = self.connect.create_cursor()
        query = """
                SELECT
                    favorite.id_compared,
                    favorite.id_result
                FROM
                    openfood.favorite
                """
        
        cursor.execute(query)
        """
        data = cursor.fetchall()

        products = []
        for id, name, id_category, brands, nutrition_grade_fr in data:
            products.append(
                Product(
                    product_name_fr=name,
                    nutrition_grade_fr=nutrition_grade_fr,
                    id=id,
                    brands=brands,
                    id_category=id_category,
                )
            )

        return products
        """
