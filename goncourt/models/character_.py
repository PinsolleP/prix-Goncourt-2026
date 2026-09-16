# -*- coding: utf-8 -*-

"""
Classe character_, représentant un personnage d'un livre'.
"""

from dataclasses import dataclass

@dataclass
class character_:
    id_character: int
    name: str
    isbn: str

    def __str__(self) -> str:
        return self.name