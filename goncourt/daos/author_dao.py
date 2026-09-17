# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.author import Author


@dataclass
class AuthorDao(Dao[Author]):
    """DAO permettant de gérer les auteurs en base de données."""

    def create(self, author: Author) -> int:
        """Crée un auteur en base de données.
        """

        sql = "INSERT INTO author(id_author, biographie, id_person) VALUES (%s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (author.id_author, author.biographie, author.id_person))

        Dao.connection.commit()
        return author.id_author

    def read(self, id_author: int) -> Optional[Author]:
        """Récupère un auteur à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = """SELECT author.*,
                            person.first_name,
                            person.last_name
                            FROM author
                            JOIN person
                                ON author.id_person = person.id_person
                            WHERE author.id_author = %s"""
            cursor.execute(sql, (id_author,))
            row = cursor.fetchone()
            if row is None:
                return None

            author = Author(
                id_person=row["id_person"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                id_author=row["id_author"],
                biographie=row["biographie"]
            )

            return author

    def update(self, author: Author) -> bool:
        """Met à jour un auteur en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE author SET biographie = %s WHERE id_author = %s"
            cursor.execute(sql, (author.biographie, author.id_author))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, author: Author) -> bool:
        """Supprime un auteur de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM author WHERE id_author = %s"
            cursor.execute(sql, (author.id_author,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted