# -*- coding: utf-8 -*-

"""
Classe Dao[User_]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.user_ import User_


@dataclass
class UserDao(Dao[User_]):
    """DAO permettant de gérer les utilisateurs en base de données."""

    def create(self, user: User_) -> int:
        """Crée un auteur en base de données.
        """

        sql = "INSERT INTO user_(user_name, password, id_person) VALUES (%s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (user.user_name, user.password, user.id_person))
            id_user = cursor.lastrowid

        Dao.connection.commit()
        return id_user

    def read(self, id_user: int) -> Optional[User_]:
        """Récupère un utilisateur à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = """SELECT user_.*,
                            person.first_name,
                            person.last_name
                            FROM user_
                            JOIN person
                                ON user_.id_person = person.id_person
                            WHERE user_.id_user = %s"""
            cursor.execute(sql, (id_user,))
            row = cursor.fetchone()
            if row is None:
                return None

            user = User_(
                id_person=row["id_person"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                id_user=row["id_user"],
                user_name=row["user_name"],
                password=row["password"]
            )

            return user

    def update(self, user: User_) -> bool:
        """Met à jour un utilisateur en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE user_ SET user_name = %s, password = %s WHERE id_user = %s"
            cursor.execute(sql, (user.user_name, user.password, user.id_user))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, user: User_) -> bool:
        """Supprime un utilisateur de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM user_ WHERE id_user = %s"
            cursor.execute(sql, (user.id_user,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted