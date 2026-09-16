# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de user_, author, et jury
"""

from dataclasses import dataclass


@dataclass
class Person:
    """Représente une personne du système Goncourt."""
    id_person: int
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

