# -*- coding: utf-8 -*-

"""
Classe Dao[Jury]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.jury import Jury
from goncourt.models.person import Person


@dataclass
class JuryDao(Dao[Jury]):
    """DAO permettant de gérer les membres du jury en base de données."""

    def create(self, jury: Jury) -> int:
        """Crée un Jury en base de données.
        """

        sql = "INSERT INTO jury(id_jury, president) VALUES (%s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (jury.id_jury, jury.president))

        Dao.connection.commit()
        return jury.id_jury

    def read(self, id_jury: int) -> Optional[Jury]:
        """Récupère un Jury à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = """SELECT jury.id_jury,
                            person.id_person,
                            person.first_name,
                            person.last_name
                            FROM jury
                            JOIN person
                                ON jury.president = person.id_person
                            WHERE jury.id_jury = %s"""
            cursor.execute(sql, (id_jury,))
            row = cursor.fetchone()
            if row is None:
                return None
            president = Person(
                id_person=row["id_person"],
                first_name=row["first_name"],
                last_name=row["last_name"]
            )
            jury = Jury(
                id_jury=row["id_jury"],
                president=president
            )
            sql = """SELECT 
                        person.id_person,
                        person.first_name,
                        person.last_name
                    FROM is_member
                    JOIN person
                        ON is_member.id_person = person.id_person
                    WHERE is_member.id_Jury = %s
                  """
            cursor.execute(sql, (id_jury,))
            rows = cursor.fetchall()

            for row in rows:
                member = Person(
                    id_person=row["id_person"],
                    first_name=row["first_name"],
                    last_name=row["last_name"]
                )
                jury.members.append(member)

            return jury

    def update(self, jury: Jury) -> bool:
        """Met à jour un jury en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE jury SET president = %s WHERE id_Jury = %s"
            cursor.execute(sql, (jury.president.id_person, jury.id_jury))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, jury: Jury) -> bool:
        """Supprime un Jury de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM is_member WHERE id_Jury = %s"
            cursor.execute(sql, (jury.id_jury,))
            sql = "DELETE FROM jury WHERE id_Jury = %s"
            cursor.execute(sql, (jury.id_jury,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
