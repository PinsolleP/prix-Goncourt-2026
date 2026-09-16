# -*- coding: utf-8 -*-

"""
Classe book, représentant un livre sélectionné pour le prix Goncourt'.
"""
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from goncourt.models.author import Author
from goncourt.models.character_ import Character_
from goncourt.models.publisher import Publisher


@dataclass
class Book:
    isbn: str
    title: str
    summary: str | None
    publication_date: date | None
    number_pages: int | None
    publisher_price: Decimal | None
    publisher: Publisher
    author: Author
    characters: list[Character_] = field(default_factory=list)

    def __str__(self) -> str:
        return self.title

