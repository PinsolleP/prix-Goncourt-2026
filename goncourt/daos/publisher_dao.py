# -*- coding: utf-8 -*-

"""
Classe Dao[Publisher]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.publisher import Publisher


@dataclass
class PublisherDao(Dao[Publisher]):
    """DAO permettant de gérer les Publisher en base de données."""

    def create(self, publisher: Publisher) -> int:
        """Crée un Publisher en base de données.
        """

        sql = "INSERT INTO publisher (id_publisher, name) VALUES (%s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (publisher.id_publisher, publisher.name))

        Dao.connection.commit()
        return publisher.id_publisher

    def read(self, id_publisher: int) -> Optional[Publisher]:
        """Récupère un Publisher à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM publisher WHERE id_publisher = %s"
            cursor.execute(sql, (id_publisher,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Publisher(
                id_publisher=row["id_publisher"],
                name=row["name"]
            )

    def update(self, publisher: Publisher) -> bool:
        """Met à jour un Publisher en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE publisher SET name = %s WHERE id_publisher = %s"
            cursor.execute(sql, (publisher.name, publisher.id_publisher))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, publisher: Publisher) -> bool:
        """Supprime un Publisher de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM publisher WHERE id_publisher = %s"
            cursor.execute(sql, (publisher.id_publisher,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
