# -*- coding: utf-8 -*-

"""
Classe publisher, représentant une maison d'édition'.
"""
from dataclasses import dataclass

@dataclass
class publisher:
    id_publisher: int
    name: str

    def __str__(self) -> str:
        return self.name