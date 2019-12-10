import mysql.connector


class DbCreate:
    """Db creation class"""

    def __init__(self, connection):
        self.connect = connection

    def create_database(self):
        """Method of creating db"""
        cursor = self.connect.create_cursor()
        create_query = """
                        CREATE DATABASE IF NOT EXISTS openfood CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
                        """

    def create_table(self):
        """Db table creation method"""
        cursor = self.connect.create_cursor()
        cursor.execute("USE `openfood`")

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`category` (
                        id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL UNIQUE,
                        PRIMARY KEY (id))
                        """

        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`product` (
                        id BIGINT UNSIGNED NOT NULL,
                        id_category SMALLINT UNSIGNED NOT NULL,
                        product_name_fr VARCHAR(500) NOT NULL,
                        brands VARCHAR(200) NOT NULL,
                        nutrition_grade_fr VARCHAR(10) NOT NULL,
                        PRIMARY KEY (id),
                        CONSTRAINT `fk_id_category`
                            FOREIGN KEY (`id_category`) REFERENCES `category` (`id`)
                        );
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`favorite` (
                        id_compared BIGINT UNSIGNED NOT NULL,
                        id_result BIGINT UNSIGNED NOT NULL,
                        PRIMARY KEY (id_compared),
                        CONSTRAINT `fk_id_compared`
                            FOREIGN KEY (`id_compared`) REFERENCES `product` (`id`),
                        CONSTRAINT `fk_id_result`
                            FOREIGN KEY (`id_result`) REFERENCES `product` (`id`)
                        );
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`store` (
                        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                        PRIMARY KEY (id),
                        name VARCHAR(100) NOT NULL UNIQUE
                        );
                        """
        cursor.execute(create_query)

        create_query = """
                        CREATE TABLE IF NOT EXISTS `openfood`.`product_has_store` (
                        id_store INT UNSIGNED NOT NULL,
                        id_product BIGINT UNSIGNED NOT NULL,
                        PRIMARY KEY (id_store, id_product),
                        CONSTRAINT `fk_id_store`
                            FOREIGN KEY (`id_store`) REFERENCES `store` (`id`),
                        CONSTRAINT `fk_id_product`
                            FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
                        );
                        """
        cursor.execute(create_query)
