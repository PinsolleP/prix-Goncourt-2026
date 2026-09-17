# -*- coding: utf-8 -*-

"""
Classe SelectionDao, permettant la gestion des sélections en base de données.
"""

from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.selection import Selection


@dataclass
class SelectionDao(Dao[Selection]):
    """DAO permettant de gérer les sélections en base de données."""

    def create(self, selection: Selection) -> int:
        """Crée une sélection en base de données.
        """

        sql = "INSERT INTO selection (id_selection, date_selection, round) VALUES (%s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (selection.id_selection, selection.date_selection, selection.round))

        Dao.connection.commit()
        return selection.id_selection

    def read(self, id_selection: int) -> Optional[Selection]:
        """Récupère une sélection à partir de son identifiant.
        """

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM selection WHERE id_selection = %s"
            cursor.execute(sql, (id_selection,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Selection(
                id_selection=row["id_selection"],
                date_selection=row["date_selection"],
                round=row["round"]
            )

    def update(self, selection: Selection) -> bool:
        """Met à jour une selection en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE selection SET date_selection = %s, round = %s WHERE id_selection = %s"
            cursor.execute(sql, (selection.date_selection, selection.round, selection.id_selection))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, selection: Selection) -> bool:
        """Supprime une sélection de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM selection WHERE id_selection = %s"
            cursor.execute(sql, (selection.id_selection,))
            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
