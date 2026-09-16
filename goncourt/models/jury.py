# -*- coding: utf-8 -*-

"""
Classe Jury, représentant le jury du prix Goncourt'.
"""
from dataclasses import dataclass, field

from goncourt.models.person import Person


@dataclass
class Jury:
    id_jury: int
    president: Person
    members: list[Person] = field(default_factory=list)

    def __str__(self) -> str:
        return f"Jury présidé par {self.president}"