# -*- coding: utf-8 -*-

"""
Classe PersonDao, permettant la gestion des Person en base de données.
"""

from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.person import Person


@dataclass
class PersonDao(Dao[Person]):
    """DAO permettant de gérer les Personnes en base de données."""

    def create(self, person: Person) -> int:
        """Crée un Publisher en base de données.
        """

        sql = "INSERT INTO person (id_person, first_name, last_name) VALUES (%s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (person.id_person, person.first_name, person.last_name))

        Dao.connection.commit()
        return person.id_person

    def read(self, id_person: int) -> Optional[Person]:
        """Récupère une personne à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person WHERE id_person = %s"
            cursor.execute(sql, (id_person,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Person(
                id_person=row["id_person"],
                first_name=row["first_name"],
                last_name=row["last_name"]
            )

    def update(self, person: Person) -> bool:
        """Met à jour une personne en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE person SET first_name = %s, last_name = %s WHERE id_person = %s"
            cursor.execute(sql, (person.first_name, person.last_name, person.id_person))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, person: Person) -> bool:
        """Supprime une personne de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM person WHERE id_person = %s"
            cursor.execute(sql, (person.id_person,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
