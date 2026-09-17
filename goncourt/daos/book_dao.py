# -*- coding: utf-8 -*-

"""
Classe BookDao, permettant la gestion des livres en base de données.
"""

from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.book import Book
from goncourt.models.publisher import Publisher
from goncourt.models.author import Author
from goncourt.models.character_ import Character_


@dataclass
class BookDao(Dao[Book]):
    """DAO permettant de gérer les livres en base de données."""

    def create(self, book: Book) -> int:
        """Crée un livre en base de données.
        """

        sql = """INSERT INTO book (
               isbn,
               title,
               summary,
               publication_date,
               number_pages,
               publisher_price,
               id_publisher,
               id_author) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (
                book.isbn,
                book.title,
                book.summary,
                book.publication_date,
                book.number_pages,
                book.publisher_price,
                book.publisher.id_publisher,
                book.author.id_author)
                           )

        Dao.connection.commit()
        return book.isbn

    def read(self, isbn: int) -> Optional[Book]:
        """Récupère un livre à partir de son ISBN"""
        with Dao.connection.cursor() as cursor:
            sql = """SELECT 
            book.*,
            publisher.name AS publisher_name,
            author.biographie,
            person.id_person,
            person.first_name,
            person.last_name
            FROM book
            JOIN publisher
                ON book.id_publisher = publisher.id_publisher
            JOIN author
                ON book.id_author = author.id_author
            JOIN person
                ON author.id_person = person.id_person
            WHERE book.isbn = %s"""
            cursor.execute(sql, (isbn,))
            row = cursor.fetchone()

            if row is None:
                return None

            publisher = Publisher(
                id_publisher=row["id_publisher"],
                name=row["publisher_name"],
            )

            author = Author(
                id_person=row["id_person"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                id_author=row["id_author"],
                biographie=row["biographie"],
            )

            book = Book(
                isbn=row["isbn"],
                title=row["title"],
                summary=row["summary"],
                publication_date=row["publication_date"],
                number_pages=row["number_pages"],
                publisher_price=row["publisher_price"],
                publisher=publisher,
                author=author,
            )

            sql = "SELECT * FROM character_ WHERE isbn = %s"
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql, (book.isbn,))
                rows = cursor.fetchall()

            for row in rows:
                character = Character_(
                    id_character=row["id_character"],
                    name = row["name"],
                    isbn = row["isbn"]
                )
                book.characters.append(character)

            return book

    def update(self, book: Book) -> bool:
        """Met à jour un livre en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = """UPDATE book 
                    SET title = %s,
                        summary = %s,
                        publication_date = %s,
                        number_pages = %s,
                        publisher_price = %s,
                        id_publisher = %s,
                        id_author = %s
                        WHERE isbn = %s"""
            cursor.execute(sql, (
                book.title,
                book.summary,
                book.publication_date,
                book.number_pages,
                book.publisher_price,
                book.publisher.id_publisher,
                book.author.id_author,
                book.isbn)
                           )
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, book: Book) -> bool:
        """Supprime un livre de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM book WHERE isbn = %s"
            cursor.execute(sql, (book.isbn,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted