# -*- coding: utf-8 -*-

"""
Classe Selection, représentant une sélection du prix Goncourt'.
"""
from dataclasses import dataclass
from datetime import date


@dataclass
class Selection:
    id_selection: int
    date_selection: date
    round: int

    def __str__(self) -> str:
        return f"Sélection {self.round} - {self.date_selection}"