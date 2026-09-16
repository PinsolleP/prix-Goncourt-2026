# -*- coding: utf-8 -*-

"""
Classe author, fille de la classe Person représentant un auteur d'un livre'.
"""
from dataclasses import dataclass

from goncourt.models.person import Person


@dataclass
class author(Person):
    id_author: int
    biographie: str | None = None