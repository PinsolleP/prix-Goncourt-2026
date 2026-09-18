# -*- coding: utf-8 -*-

"""
Classe Dao[Vote]
"""
from dataclasses import dataclass
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.jury_dao import JuryDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.models.vote import Vote


@dataclass
class VoteDao(Dao[Vote]):
    """DAO permettant de gérer un vote en base de données."""

    def create(self, vote: Vote) -> int:
        """Crée un vote en base de données.
        """

        sql = "INSERT INTO vote(isbn, id_Jury, id_selection, number_of_votes) VALUES (%s, %s, %s, %s)"

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (vote.book.isbn, vote.jury.id_jury, vote.selection.id_selection, vote.number_of_votes))

        Dao.connection.commit()
        return vote.book.isbn

    def read_by_key(self, isbn: int, id_jury: int, id_selection: int) -> Optional[Vote]:
        """Récupère un Vote à partir de sa clé primaire composée.
        """

        with Dao.connection.cursor() as cursor:
            sql = """SELECT isbn, id_Jury, id_selection, number_of_votes 
                     FROM vote
                     WHERE isbn = %s
                        AND id_Jury = %s
                        AND id_selection = %s
                  """
            cursor.execute(sql, (isbn, id_jury, id_selection))
            row = cursor.fetchone()

            if row is None:
                return None

            book = BookDao().read(row["isbn"])
            jury = JuryDao().read(row["id_Jury"])
            selection = SelectionDao().read(row["id_selection"])

            if book is None or jury is None or selection is None:
                return None

            vote = Vote(book=book, jury=jury, selection=selection, number_of_votes=row["number_of_votes"])
            return vote

    def update(self, vote: Vote) -> bool:
        """Met à jour un vote en base de données
        """
        with Dao.connection.cursor() as cursor:
            sql = """UPDATE vote 
                     SET number_of_votes = %s 
                     WHERE isbn = %s
                        AND id_Jury = %s
                        AND id_selection = %s"""
            cursor.execute(sql, (vote.number_of_votes, vote.book.isbn, vote.jury.id_jury, vote.selection.id_selection))
            updated = cursor.rowcount > 0
        Dao.connection.commit()
        return updated

    def delete(self, vote: Vote) -> bool:
        """Supprime un vote de la base de données.
        """
        with Dao.connection.cursor() as cursor:
            sql = """DELETE FROM vote 
                     WHERE isbn = %s
                        AND id_Jury = %s
                        AND id_selection = %s"""
            cursor.execute(sql, (vote.book.isbn, vote.jury.id_jury, vote.selection.id_selection))

            deleted = cursor.rowcount > 0
        Dao.connection.commit()
        return deleted
