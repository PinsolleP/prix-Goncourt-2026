# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.character_ import Character_


@dataclass
class CharacterDao(Dao[Character_]):
    """DAO permettant de gérer les personnages en base de données."""

    def create(self, character: Character_) -> int:
        """Crée un Personnage en base de données.
        """

        sql = "INSERT INTO character_(id_character, name, isbn) VALUES (%s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (character.id_character, character.name, character.isbn))

        Dao.connection.commit()
        return character.id_character

    def read(self, id_character: int) -> Optional[Character_]:
        """Récupère un Publisher à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM character_ WHERE id_character = %s"
            cursor.execute(sql, (id_character,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Character_(
                id_character=row["id_character"],
                name=row["name"],
                isbn=row["isbn"]
            )

    def update(self, character: Character_) -> bool:
        """Met à jour un personnage en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE character_ SET name = %s WHERE id_character = %s"
            cursor.execute(sql, (character.name, character.id_publisher))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, character: Character_) -> bool:
        """Supprime un Personnage de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM character_ WHERE id_character = %s"
            cursor.execute(sql, (character.id_character,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
