# -*- coding: utf-8 -*-

"""
Classe Vote, représentant le résultat d'un vote du jury'.
"""
from dataclasses import dataclass

from goncourt.models.book import Book
from goncourt.models.jury import Jury
from goncourt.models.selection import Selection


@dataclass
class Vote:
    book: Book
    jury: Jury
    selection: Selection
    number_of_votes: int

    def __str__(self) -> str:
        return f"{self.book.title} : {self.number_of_votes} votes"