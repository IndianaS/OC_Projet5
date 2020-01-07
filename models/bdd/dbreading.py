from models.product import Product


class DbReading:

    def __init__(self, connection):
        self.connect = connection

    def get_all_categories(self):
        """Method of retrieving categories"""
        cursor = self.connect.create_cursor()
        cursor.execute('USE openfood')

        query = """SELECT * FROM category ORDER BY category.id"""

        cursor.execute(query)

        return cursor.fetchall()

    def get_category_products(self, id_category):
        """Method of recovering products from a category"""
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
        """Method of recovering a selected product"""
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
        """Method of selecting substitutes for a selected product"""
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

    def get_favorite(self):
        """Method of selecting favorites save"""
        cursor = self.connect.create_cursor()
        cursor.execute('USE openfood')
        query = """
                SELECT
                    compared.id,
                    compared.product_name_fr,
                    compared.nutrition_grade_fr,
                    compared.brands,
                    result.id,
                    result.product_name_fr,
                    result.nutrition_grade_fr,
                    result.brands
                FROM
                    openfood.favorite
                    JOIN product as compared ON favorite.id_compared = compared.id
                    JOIN product as result ON favorite.id_result = result.id
                """
        
        cursor.execute(query)
